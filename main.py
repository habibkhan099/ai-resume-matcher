from flask import Flask, request, render_template, flash, jsonify
import os
import PyPDF2
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging
from werkzeug.utils import secure_filename
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Allowed file extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(file_path):
    """Extract text from different file types with error handling."""
    try:
        if file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    page_text = page.extract_text() or ''
                    text += page_text
                if not text.strip():
                    logger.warning(f"No text extracted from PDF: {file_path}")
                return text
        elif file_path.lower().endswith('.docx'):
            text = docx2txt.process(file_path)
            if not text.strip():
                logger.warning(f"No text extracted from DOCX: {file_path}")
            return text
        elif file_path.lower().endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return file.read()
        return ''
    except Exception as e:
        logger.error(f"Error extracting text from {file_path}: {str(e)}")
        return ''

@app.route("/")
def matchresume():
    return render_template('matchresume.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    """Handle resume matching with enhanced error handling and logging."""
    try:
        start_time = time.time()
        
        # Get form data
        job_description = request.form.get('job_description', '').strip()
        resume_files = request.files.getlist('resumes')
        shortlist_count = int(request.form.get('shortlist_count', 5))
        
        # Validation
        if not job_description:
            return render_template('matchresume.html', 
                                 message="Please provide a job description.",
                                 error=True)
        
        if not resume_files or len(resume_files) == 0:
            return render_template('matchresume.html', 
                                 message="Please upload at least one resume.",
                                 error=True)
        
        # Check for valid files
        valid_files = [f for f in resume_files if f and f.filename and allowed_file(f.filename)]
        
        if not valid_files:
            return render_template('matchresume.html', 
                                 message="Please upload valid resume files (PDF, DOCX, or TXT).",
                                 error=True)
        
        logger.info(f"Processing {len(valid_files)} resume files")

        # Process files
        resume_texts = []
        uploaded_filenames = []
        
        for file in valid_files:
            try:
                # Secure the filename
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                # Save file
                file.save(filepath)
                
                # Extract text
                text = extract_text(filepath)
                
                if text.strip():  # Only add if text was extracted
                    resume_texts.append(text)
                    uploaded_filenames.append(filename)
                else:
                    logger.warning(f"No text extracted from {filename}")
                
                # Clean up uploaded file
                try:
                    os.remove(filepath)
                except OSError:
                    pass
                    
            except Exception as e:
                logger.error(f"Error processing file {file.filename}: {str(e)}")
                continue

        if not resume_texts:
            return render_template('matchresume.html', 
                                 message="No text could be extracted from the uploaded files. Please check file formats and content.",
                                 error=True)

        # Categorize filenames by type
        txt_files = [f for f in uploaded_filenames if f.lower().endswith('.txt')]
        pdf_files = [f for f in uploaded_filenames if f.lower().endswith('.pdf')]
        docx_files = [f for f in uploaded_filenames if f.lower().endswith('.docx')]

        # Vectorization and similarity calculation
        try:
            tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
            tfidf_matrix = tfidf.fit_transform([job_description] + resume_texts)
            similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        except Exception as e:
            logger.error(f"Error in text vectorization: {str(e)}")
            return render_template('matchresume.html', 
                                 message="Error analyzing resumes. Please try again with different files.",
                                 error=True)

        # Sort resumes by similarity score in descending order
        resume_scores = list(zip(uploaded_filenames, similarity_scores))
        resume_scores.sort(key=lambda x: x[1], reverse=True)

        # Get total number of uploaded resumes and top N based on shortlist_count
        total_uploaded = len(uploaded_filenames)
        effective_count = min(shortlist_count, total_uploaded)
        top_resumes = [f for f, _ in resume_scores[:effective_count]]
        top_similarity_scores = [score for _, score in resume_scores[:effective_count]]

        # Log processing time
        processing_time = time.time() - start_time
        logger.info(f"Processed {total_uploaded} resumes in {processing_time:.2f} seconds")

        # Return results
        return render_template('matchresume.html', 
                             message="Analysis Complete - Top Matching Candidates:", 
                             top_resumes=top_resumes, 
                             similarity_scores=top_similarity_scores, 
                             total_uploaded=total_uploaded, 
                             txt_files=txt_files, 
                             pdf_files=pdf_files, 
                             docx_files=docx_files,
                             processing_time=f"{processing_time:.2f}")
    
    except Exception as e:
        logger.error(f"Unexpected error in matcher: {str(e)}")
        return render_template('matchresume.html', 
                             message="An unexpected error occurred. Please try again.",
                             error=True)

@app.errorhandler(413)
def too_large(e):
    return render_template('matchresume.html', 
                         message="File too large. Please upload files smaller than 16MB.",
                         error=True), 413

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)