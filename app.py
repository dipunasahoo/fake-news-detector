import streamlit as st
import pickle
import re

# ==================================
# Load trained model and vectorizer
# ==================================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==================================
# Text cleaning (SAME as training)
# ==================================
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

# ==================================
# Streamlit UI
# ==================================
st.set_page_config(
    page_title="Fake News Detector for Students",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Fake News Detector for Students")

st.write(
    "This tool helps students identify **fake, real, or uncertain news** related to "
    "education, jobs, exams, and viral social media messages."
)

st.info(
    "⚠️ Disclaimer: This system predicts the likelihood of misinformation based on "
    "language patterns. It does not replace official fact-checking."
)

# ==================================
# Input box
# ==================================
news_text = st.text_area(
    "Paste the news text below to analyze:",
    height=220,
    placeholder="Example: A viral message claims that all students will get jobs without exams..."
)

# ==================================
# Prediction logic (FINAL FIX – 60% THRESHOLD)
# ==================================
if st.button("Analyze News"):
    if news_text.strip() == "":
        st.warning("Please enter some news text.")
    else:
        cleaned = clean_text(news_text)
        vec = vectorizer.transform([cleaned])
        probs = model.predict_proba(vec)[0]

        class_map = dict(zip(model.classes_, probs))

        fake_prob = class_map.get(1, 0) * 100   # 1 = FAKE
        real_prob = class_map.get(0, 0) * 100   # 0 = REAL


        st.write(f"Fake Probability: {fake_prob:.2f}%")
        st.write(f"Real Probability: {real_prob:.2f}%")

        # FINAL DECISION LOGIC
        if fake_prob >= 60:
            st.error(
                f"❌ FAKE News\n\nConfidence: {fake_prob:.2f}%"
            )

        elif real_prob >= 60:
            st.success(
                f"✅ REAL News\n\nConfidence: {real_prob:.2f}%"
            )

        else:
            st.warning(
                f"🤔 UNCERTAIN / NEEDS VERIFICATION\n\n"
                f"Fake: {fake_prob:.2f}% | Real: {real_prob:.2f}%"
            )

# ==================================
# Footer
# ==================================
st.markdown("---")
st.caption(
    "Fake News Detector for Students | NLP & Machine Learning | Streamlit"
)
