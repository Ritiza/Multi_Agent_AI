# utils/intent_detector.py
import os
from dotenv import load_dotenv
from transformers import pipeline

load_dotenv()

# Load the Hugging Face model (you can replace this with a more suitable model)
model_name = os.getenv("HF_INTENT_MODEL", "SkolkovoInstitute/roberta-intent-classification")

# Create a pipeline for text classification
try:
    intent_classifier = pipeline("text-classification", model=model_name)
except Exception as e:
    intent_classifier = None
    print(f"Error loading model: {e}")

def detect_intent_llm(text):
    if not intent_classifier:
        return "Error: Intent classifier pipeline not initialized."
    
    try:
        results = intent_classifier(text[:1000])
        return results[0]['label']  # Return the label (intent)
    except Exception as e:
        return f"Error: {e}"
