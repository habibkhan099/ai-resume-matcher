# 🤖 AI Resume Matcher

An intelligent resume screening system that matches job descriptions with candidate resumes using **TF-IDF** and **cosine similarity**.

---

## 🌟 Features
- 🎯 AI-Powered Resume Matching
- 📁 Supports PDF, DOCX, TXT formats
- ⚡ Instant processing and ranking
- 📊 Similarity scoring with top candidate ranking
- 🎨 Simple Flask web interface

---

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Steps
```bash
# Clone this repository
git clone https://github.com/your-username/ai-resume-matcher.git
cd ai-resume-matcher

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python main.py
Then open in browser: 👉 http://127.0.0.1:5000

📂 Project Structure
bash
Copy code
ai-resume-matcher/
├── main.py              # Flask app
├── templates/
│   └── matchresume.html # Web interface
├── uploads/             # Uploaded resumes
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
💡 Usage
Enter a job description in the text box

Upload resumes (PDF/DOCX/TXT)

Click Submit

View the top matches with similarity scores

⚙️ Tech Stack
Python 3.8+

Flask (backend web framework)

scikit-learn (TF-IDF, cosine similarity)

PyPDF2 (PDF parsing)

docx2txt (DOCX parsing)

HTML + Bootstrap (frontend UI)

📈 Future Improvements
Add advanced NLP models (spaCy, BERT, etc.)

Improve preprocessing (stopword removal, lemmatization)

Deploy on Heroku/Vercel for public use

Add a dashboard for recruiters

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Habib Ullah

GitHub: @habibkhan099

LinkedIn: LinkedIn Profile

Email: 22-CP-62@students.uettaxila.edu.pk

University: UET Taxila

⭐ If you find this project useful, don’t forget to star the repo!
