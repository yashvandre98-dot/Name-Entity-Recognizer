import streamlit as st
import spacy

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Page config
st.set_page_config(
    page_title="NER with spaCy",
    page_icon="🧠",
    layout="centered"
)

# Title
st.title("🧠 Named Entity Recognition App")
st.markdown(
    "Extract **People, Places, Organizations, Dates**, and more using **spaCy NLP**."
)

# Text input
text = st.text_area(
    "✍️ Enter your text here:",
    height=120,
    placeholder="Virat Kohli was born in Delhi and plays cricket for India."
)

# Button
if st.button("🔍 Analyze Text"):
    if text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        doc = nlp(text)

        st.subheader("📌 Detected Entities")

        if doc.ents:
            for ent in doc.ents:
                st.markdown(
                    f"""
                    **Entity:** `{ent.text}`  
                    **Label:** `{ent.label_}`
                    ---
                    """
                )
        else:
            st.info("No entities found in the text.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using spaCy & Streamlit")
