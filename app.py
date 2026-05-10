import streamlit as st
from rag_pipeline import create_rag_pipeline
from utils import clean_text

st.title("AI Fake News Detector")

# User Input
news_input = st.text_area("Paste News Article Here")

if st.button("Analyze News"):

    if news_input == "":
        st.warning("Please enter news text")
    else:
        with st.spinner("Analyzing..."):

            text = clean_text(news_input)

            # Create RAG system
            qa = create_rag_pipeline(text)

            # Prompt
            prompt = f"""
            You are an expert fact-checker.

            Analyze the following news and determine:
            1. Is it FAKE or REAL?
            2. Confidence score (0-100%)
            3. Explanation (why)
            4. Any suspicious patterns

            News:
            {text}
            """

            result = qa.run(prompt)

            st.subheader("Result")
            st.write(result)