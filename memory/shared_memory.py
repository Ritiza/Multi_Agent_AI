# memory/shared_memory.py
memory_store = {}

def save_context(doc_id, data):
    memory_store[doc_id] = data

def get_context(doc_id):
    return memory_store.get(doc_id, {})
