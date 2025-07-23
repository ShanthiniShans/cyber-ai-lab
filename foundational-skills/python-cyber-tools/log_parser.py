# This simple parser reads log entries from a file, extracts key information, and optionally performs basic NLP (e.g., summarization with spaCy).

# log_parser.py

import re
import spacy

# Load small English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_log_line(line):
    """Extract timestamp, log level, and message using regex."""
    pattern = r'^(\w{3} \d+ \d{2}:\d{2}:\d{2}) ([\w\-]+) (.+)$'
    match = re.match(pattern, line)
    if match:
        timestamp, source, message = match.groups()
        return {"timestamp": timestamp, "source": source, "message": message}
    return None

def summarize_log_message(message):
    """Use spaCy to summarize the message (basic noun chunk extraction)."""
    doc = nlp(message)
    return " | ".join(chunk.text for chunk in doc.noun_chunks)

def process_log_file(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            parsed = parse_log_line(line.strip())
            if parsed:
                summary = summarize_log_message(parsed["message"])
                print(f"[{parsed['timestamp']}] ({parsed['source']})")
                print(f"  ➜ Message: {parsed['message']}")
                print(f"  ➜ Summary: {summary}")
                print("-" * 50)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <log_file>")
    else:
        process_log_file(sys.argv[1])
