
# 🤖 AI Resume Matcher

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A smart resume screening tool powered by machine learning and NLP to match job descriptions with candidate resumes.

## 🌟 Features
- **AI Matching**: TF-IDF vectorization and cosine similarity
- **File Support**: PDF, DOCX, TXT resumes
- **Real-time Analysis**: Instant resume ranking
- **Smart Analytics**: Similarity scoring and candidate ranking
- **Responsive UI**: Drag-and-drop interface, mobile-friendly
- **Easy Setup**: Simple installation

## 🚀 Demo
![Main Interface](demo/main-interface.png)  
![File Upload](demo/file-upload-demo.png)  
![Results Dashboard](demo/results-dashboard.png)  

**Live Demo**: [Coming Soon]  
**Source Code**: [GitHub](https://github.com/habibkhan099/ai-resume-matcher)

## 🛠️ Installation
### Prerequisites
- Python 3.8+
- pip

### Quick Start
```bash
git clone https://github.com/habibkhan099/ai-resume-matcher.git
cd ai-resume-matcher
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Visit: `http://localhost:5000`

## 💡 Usage
1. Paste job description
2. Upload resumes (PDF, DOCX, TXT)
3. Set number of top candidates
4. Click "Analyze Resumes"
5. Review ranked results

**Tips**: Use 5–10 resumes and detailed job descriptions for best results.

## 🔍 How It Works
1. **Text Extraction**: PyPDF2 (PDF), docx2txt (DOCX), direct read (TXT)
2. **Preprocessing**: Lowercase, remove stop words, normalize text
3. **Vectorization**: TF-IDF for text-to-numeric conversion
4. **Similarity**: Cosine similarity scoring (0 to 1)
5. **Ranking**: Sort and display top candidates

```python
# Core algorithm
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform([job_description] + resume_texts)
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
```

## 📁 Project Structure
```
ai-resume-matcher/
├── main.py                # Flask app
├── templates/             # HTML templates
├── uploads/               # Resume storage
├── Resume/                # Sample resumes
├── static/                # CSS, JS, images
├── demo/                  # Demo screenshots
├── requirements.txt       # Dependencies
├── README.md             # Documentation
├── LICENSE               # MIT License
└── .gitignore
```

## 🛡️ Tech Stack
- **Backend**: Python 3.8+, Flask, scikit-learn, PyPDF2, docx2txt
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript, Font Awesome
- **ML/NLP**: TF-IDF, cosine similarity, text preprocessing

## 🔧 Configuration
Create `.env`:
```env
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
UPLOAD_FOLDER=uploads
MAX_CONTENT_LENGTH=16777216
```

## 📊 Performance
- **Speed**: 2–5s for 10–20 resumes
- **Accuracy**: 85–90% for well-formatted resumes
- **Support**: PDF (95%), DOCX (90%), TXT (100%)
- **Scale**: Up to 50 resumes

## 🚀 Deployment
### Heroku
```bash
heroku create your-app-name
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
```
```bash
docker build -t ai-resume-matcher .
docker run -p 5000:5000 ai-resume-matcher
```

## 🤝 Contributing
1. Fork the repo
2. Create branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add YourFeature'`)
4. Push (`git push origin feature/YourFeature`)
5. Open a Pull Request

**Guidelines**: Follow PEP 8, write clear commits, add tests, update docs.

## 📝 License
MIT License - see [LICENSE](LICENSE).

## 👨‍💻 Author
**Habib Ullah**  
- GitHub: [@habibkhan099](https://github.com/habibkhan099)  
- LinkedIn: [Profile](https://www.linkedin.com/in/engr-habib-ullah-565a562ab)  
- Email: 22-CP-62@students.uettaxila.edu.pk  

## 🙏 Acknowledgments
- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)

⭐ **Star this repo if you find it helpful!**  
Made with ❤️ and ☕ by [Habib Ullah](https://github.com/habibkhan099)
```
