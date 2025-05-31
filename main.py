from agents.classifier_agent import detect_format, detect_intent
from agents.email_agent import process_email
from agents.json_agent import process_json
from memory.shared_memory import save_context

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Define sample files to process
    files = {
        "email": "samples/sample_email.txt",
        "json": "samples/sample_invoice.json",
    }

    for key, path in files.items():
        print(f"\n📂 Processing {path}")
        content = load_file(path)

        doc_id = path
        fmt = detect_format(content)
        intent = detect_intent(content)

        context = {"format": fmt, "intent": intent}

        if fmt == "Email":
            context.update(process_email(content))
        elif fmt == "JSON":
            context.update(process_json(content))
        else:
            context["note"] = "PDF parsing not implemented yet"

        save_context(doc_id, context)
        print(f"🧠 Saved context for `{doc_id}`:\n{context}")

if __name__ == "__main__":
    main()
