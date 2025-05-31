# classifier.py

import re

def clean_text(text):
    """Clean input text: remove signatures, extra whitespace, etc."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # collapse multiple spaces
    text = re.sub(r'[-_*]{3,}', '', text)  # remove signature lines
    text = re.sub(r'\b(sent from my .+?)\b', '', text)  # remove mobile footers
    return text.strip()

def classify_file(content, file_type=None):
    content = clean_text(content)

    # Define keyword groups for intents
    intent_keywords = {
        "Invoice": ["invoice", "billing", "payment", "amount due", "due date", "tax", "total"],
        "RFQ": ["request for quote", "quotation", "rfq", "pricing", "cost estimate", "quote required"],
        "Complaint": ["complaint", "issue", "problem", "not working", "damaged", "poor service", "return"],
        "Regulation": ["regulation", "compliance", "policy", "law", "legal", "audit", "standards"],
        "Feedback": ["feedback", "suggestion", "recommendation", "your opinion", "review"],
        "Job Application": ["resume", "cv", "cover letter", "application for", "job opportunity"],
        "General Inquiry": ["hello", "hi", "inquiry", "need help", "how to", "support", "question"]
    }

    scores = {intent: 0 for intent in intent_keywords}

    for intent, keywords in intent_keywords.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', content):
                scores[intent] += 1

    top_intent = max(scores, key=scores.get)
    highest_score = scores[top_intent]

    # Threshold: If no strong keyword match, fall back
    if highest_score == 0:
        top_intent = "Unknown"
    elif highest_score == 1:
        # Weak signal, possible ambiguity
        top_intent = f"Possible {top_intent}"

    detected_type = file_type or "Unknown"

    return detected_type, top_intent
