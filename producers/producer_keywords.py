import json
import os
import time
import random
from datetime import datetime

# Load environment variables
live_data_path = os.getenv("LIVE_DATA_FILE", "./data/project_live.jsonl")

# Ensure data folder exists
os.makedirs(os.path.dirname(live_data_path), exist_ok=True)

# Sample data generation
ADJECTIVES = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS = ["found", "saw", "tried", "shared", "loved"]
TOPICS = ["Python", "JavaScript", "AI", "recipe", "travel", "game"]
AUTHORS = ["Alice", "Bob", "Charlie", "Eve"]

def generate_message():
    adjective = random.choice(ADJECTIVES)
    action = random.choice(ACTIONS)
    topic = random.choice(TOPICS)
    author = random.choice(AUTHORS)
    message_text = f"I just {action} {topic}! It was {adjective}."
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    json_message = {
        "message": message_text,
        "author": author,
        "timestamp": timestamp,
        "keyword_mentioned": topic
    }

    return json_message

def main():
    print("Starting Producer...")
    while True:
        message = generate_message()
        with open(live_data_path, "a") as f:
            f.write(json.dumps(message) + "\n")
        print(f"Generated message: {message}")
        time.sleep(3)  # Simulating real-time streaming

if __name__ == "__main__":
    main()
