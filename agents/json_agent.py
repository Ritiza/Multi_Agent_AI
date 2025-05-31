import json

def process_json(text):
    try:
        parsed = json.loads(text)
        return {"json_data": parsed}
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON: {e}"}
