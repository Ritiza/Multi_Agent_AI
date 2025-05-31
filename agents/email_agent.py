import re

def process_email(content):
    try:
        sender_match = re.search(r"From:\s*(.*@gmail\.com)", content)
        subject_match = re.search(r"Subject:\s*(.*)", content)
        urgency_match = re.search(r"\burgent\b|\basap\b|\bimmediate\b", content, re.IGNORECASE)

        if not sender_match:
            return {"error": "Only gmail.com emails are supported."}

        sender = sender_match.group(1).strip()
        subject = subject_match.group(1).strip() if subject_match else "No Subject"
        urgency = "High" if urgency_match else "Normal"

        return {
            "sender": sender,
            "subject": subject,
            "urgency": urgency
        }

    except Exception as e:
        return {"error": str(e)}
