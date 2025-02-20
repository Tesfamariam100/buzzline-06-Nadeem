import json
import sqlite3
import time

# Define file paths
LIVE_DATA_FILE = "./data/live_data.jsonl"
DATABASE_FILE = "./data/buzzline_data.db"

# Create SQLite table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS keyword_trends (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            keyword TEXT,
            count INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Insert keyword data into the database
def insert_keyword(keyword):
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Check if keyword already exists
    cursor.execute("SELECT count FROM keyword_trends WHERE keyword=?", (keyword,))
    result = cursor.fetchone()

    if result:
        new_count = result[0] + 1
        cursor.execute("UPDATE keyword_trends SET count=? WHERE keyword=?", (new_count, keyword))
    else:
        cursor.execute("INSERT INTO keyword_trends (keyword, count) VALUES (?, ?)", (keyword, 1))

    conn.commit()
    conn.close()

# Process each message
def process_message(message):
    keyword = message.get("keyword_mentioned")
    if keyword:
        insert_keyword(keyword)
        print(f"Processed keyword: {keyword}")

# Read the JSONL file and process messages in real-time
def consume_data():
    print("Starting consumer: Tracking keyword mentions...")
    while True:
        try:
            with open(LIVE_DATA_FILE, "r") as file:
                lines = file.readlines()
                for line in lines:
                    message = json.loads(line.strip())
                    process_message(message)
            time.sleep(5)  # Wait for new data
        except FileNotFoundError:
            print("Waiting for live data file...")
            time.sleep(5)

# Run the consumer
if __name__ == "__main__":
    init_db()
    consume_data()
