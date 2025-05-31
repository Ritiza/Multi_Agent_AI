import streamlit as st
from agents.email_agent import process_email
from agents.json_agent import process_json
from utils.file_loader import read_pdf
from classifier import classify_file
import os

st.set_page_config(page_title="Multi-Agent AI System", layout="centered")
st.title("🤖 Multi-Agent AI Processor")

# Upload input file
uploaded_file = st.file_uploader("Upload PDF / JSON / Paste Email Text", type=["pdf", "json", "txt"])

input_text = ""
file_type = None

if uploaded_file:
    file_ext = os.path.splitext(uploaded_file.name)[1].lower()
    if file_ext == ".pdf":
        file_type = "PDF"
        bytes_data = uploaded_file.read()
        with open("temp.pdf", "wb") as f:
            f.write(bytes_data)
        input_text = read_pdf("temp.pdf")

    elif file_ext == ".json":
        file_type = "JSON"
        input_text = uploaded_file.read().decode("utf-8")

    elif file_ext == ".txt":
        file_type = "Email"
        input_text = uploaded_file.read().decode("utf-8")

elif st.checkbox("Or paste email manually"):
    input_text = st.text_area("Paste email content (must be from @gmail.com)")
    file_type = "Email"

if input_text:
    st.subheader("📄 Detected Content")
    st.code(input_text, language="text")

    if st.button("🔍 Process"):
        st.info("Classifying file...")

        # Detect format + intent
        format_detected, intent = classify_file(input_text, file_type)

        st.success(f"✅ Format: {format_detected}, Intent: {intent}")

        if format_detected == "Email":
            st.subheader("📧 Email Agent Output")
            email_result = process_email(input_text)
            if "error" in email_result:
                st.error(email_result["error"])
            else:
                st.json(email_result)

        elif format_detected == "JSON":
            st.subheader("🔧 JSON Agent Output")
            json_result = process_json(input_text)
            st.json(json_result)

        elif format_detected == "PDF":
            st.subheader("📜 PDF Detected")
            st.text("No specific agent assigned to PDF text in this app demo.")

else:
    st.warning("Upload a file or paste email content to begin.")
