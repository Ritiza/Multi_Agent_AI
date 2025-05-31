# Multi-Agent AI System for Intelligent Document Processing

## Overview & Architecture

This is a modular AI system designed to process inputs in **PDF**, **JSON**, or **Email** formats. It uses a **Classifier Agent** to determine both the format and intent (e.g., Invoice, RFQ, Complaint), then routes the input to the appropriate processing agent.

### Core Components

- **Classifier Agent**: Detects input format & intent using heuristics + LLMs.
- **JSON Agent**: Validates structured JSON against a schema and reformats it.
- **Email Agent**: Extracts sender, intent, urgency, and structures content for CRM systems.
- **Shared Memory**: Redis or SQLite-based context store for all metadata, extracted values, and conversation IDs.

- 
---

## How to Install Dependencies

### Prerequisites

- Python 3.8+
- Redis (optional; fallback is SQLite)
- OpenAI API key (or replace with open-source LLM)

### Installation

```bash
git clone https://github.com/yourusername/multi-agent-ai-system.git
cd multi-agent-ai-system
pip install -r requirements.txt
multi_agent_system/
├── agents/
│   ├── classifier_agent.py     # Classifies input format & intent
│   ├── json_agent.py           # Handles structured JSON inputs
│   └── email_agent.py          # Processes email content
├── memory/
│   └── shared_memory.py        # Redis/SQLite interface
├── utils/
│   ├── intent_detector.py
│            
├── sample_inputs/
│   ├── sample_invoice.json
│   ├── sample_email.txt
├── outputs/
│   └── snippets # Extraction logs
├── README.md
└── requirements.txt


