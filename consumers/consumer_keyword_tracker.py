import json
import sqlite3
import os
import time

# Load environment variables
live_data_path = os.getenv("LIVE_DATA_FILE", "./data/project_live.jsonl")
database_path = os.getenv("DATABASE_FILE", "./data/buzzline_data.db")

# Connect to SQLite database
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS keyword_counts (
        keyword TEXT PRIMARY KEY,
        count INTEGER
    )
""")
conn.commit()

def update_keyword_count(keyword):
    cursor.execute("SELECT count FROM keyword_counts WHERE keyword=?", (keyword,))
    result = cursor.fetchone()
    
    if result:
        new_count = result[0] + 1
        cursor.execute("UPDATE keyword_counts SET count=? WHERE keyword=?", (new_count, keyword))
    else:
        cursor.execute("INSERT INTO keyword_counts (keyword, count) VALUES (?, ?)", (keyword, 1))

    conn.commit()

def main():
    print("Starting Consumer...")
    while True:
        if os.path.exists(live_data_path):
            with open(live_data_path, "r") as f:
                lines = f.readlines()
            
            with open(live_data_path, "w") as f:
                f.truncate()  # Clear file after reading
            
            for line in lines:
                message = json.loads(line)
                keyword = message.get("keyword_mentioned")
                if keyword:
                    update_keyword_count(keyword)
                    print(f"Processed keyword: {keyword}")

        time.sleep(5)  # Process every 5 seconds

if __name__ == "__main__":
    main()
