# 🎓 Student-Focused Fake News Detection System

An AI-powered web application developed to help students verify the authenticity of news related to education, examinations, job opportunities, scholarships, and viral academic updates.

The system uses Natural Language Processing (NLP) and Machine Learning techniques to classify textual content as Fake, Real, or Uncertain.

🔗 Live Demo:
https://fakenews-detector-for-students.streamlit.app/

------------------------------------------------------------

🚀 Project Overview

Due to the rapid spread of misinformation on social media platforms, students often face confusion regarding exams, results, admissions, scholarships, and employment notifications.

This project provides a simple and intelligent tool that analyzes news text and categorizes it into:

❌ Fake  
✅ Real  
⚠️ Uncertain (requires verification)

------------------------------------------------------------

🧠 How the System Works

1. The user enters education-related news text into the application.
2. The text undergoes NLP preprocessing and transformation.
3. A trained Machine Learning model calculates probability scores for:
   - Fake
   - Real
4. The final classification is determined using a 60% confidence threshold.

------------------------------------------------------------

⚠️ Disclaimer

This system predicts the likelihood of misinformation based on learned language patterns.
It should be used as a supportive tool and does not replace official fact-checking sources or verified announcements.

------------------------------------------------------------

🛠️ Technology Stack

- Python  
- Streamlit (Web Interface)  
- Scikit-learn  
- Natural Language Processing (NLP)  
- Pickle (for model and vectorizer storage)

------------------------------------------------------------

📊 Dataset Information

The model was trained using datasets sourced from Kaggle, focusing primarily on education-related news.

Initially, international datasets were explored. However, final training was conducted using India-specific education news data to improve contextual relevance.

Dataset Source: Kaggle (Indian education-related dataset)

------------------------------------------------------------

🎯 Prediction Logic

Fake → Fake probability ≥ 60%  
Real → Real probability ≥ 60%  
Uncertain → If neither probability crosses 60%

------------------------------------------------------------

🖥️ Application Features

- Clean and user-friendly interface  
- Real-time prediction  
- Confidence-based classification  
- Handles ambiguous cases as “Uncertain”  
- Designed specifically for student-related news

------------------------------------------------------------

▶️ How to Run Locally

Install dependencies:
pip install -r requirements.txt

Run the application:
streamlit run app.py

Project Structure:

├── app.py  
├── model.pkl  
├── vectorizer.pkl  
├── requirements.txt  
└── README.md  

------------------------------------------------------------

📌 Limitations

- Model accuracy depends on dataset quality  
- Limited availability of high-quality Indian education datasets  
- Predictions are probabilistic and cannot guarantee 100% correctness  

------------------------------------------------------------

🔮 Future Improvements

- Larger and more diverse Indian datasets  
- Multilingual support (Hindi, Marathi, etc.)  
- URL-based news analysis  
- Deep learning-based models for improved accuracy  