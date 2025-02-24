📢 Buzzline 06 - Keyword Tracking & Visualization
🚀 Real-time keyword tracking pipeline using Python & SQLite

📌 Project Overview
This project tracks keyword mentions from a live data stream, stores them in an SQLite database, and visualizes trends in real-time using Matplotlib. The pipeline consists of:

🔵 Producer → Generates messages and writes them to project_live.jsonl
🟢 Consumer → Reads messages, tracks keyword frequency, and updates a database
📊 Visualization → Displays keyword trends in real-time
📁 Project Structure
bash
Copy
Edit
buzzline-06-Nadeem/
├── producers/
│   ├── producer_keywords.py  # Generates and writes messages to file
├── consumers/
│   ├── consumer_keyword_tracker.py  # Reads messages, updates database
│   ├── consumer_visualizer.py  # Plots real-time keyword trends
├── utils/
│   ├── utils_database.py  # Handles database operations
│   ├── utils_visualizer.py  # Manages Matplotlib animations
├── data/
│   ├── project_live.jsonl  # Live data file
│   ├── buzzline_data.db  # SQLite database
├── .gitignore
├── .env
├── README.md  # You are here
├── requirements.txt
└── venv/
⚙️ How to Run the Project
🔹 1. Setup the Environment
✅ Activate Virtual Environment

sh
Copy
Edit
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
✅ Install Dependencies

sh
Copy
Edit
pip install -r requirements.txt
🔹 2. Start the Producer
Generates and writes messages to data/project_live.jsonl.

sh
Copy
Edit
python producers/producer_keywords.py
🔄 This will keep running and continuously generate messages.

🔹 3. Start the Consumer
Reads messages from project_live.jsonl, processes keyword mentions, and stores them in the SQLite database.

sh
Copy
Edit
python consumers/consumer_keyword_tracker.py
🔹 4. View the Keyword Trend Visualization
Runs the visualization script to track keyword trends dynamically.

sh
Copy
Edit
python consumers/consumer_visualizer.py
🛠️ Configuration & Environment Variables
The project uses a .env file to store file paths.
Example .env file:

env
Copy
Edit
LIVE_DATA_FILE=./data/project_live.jsonl
DATABASE_FILE=./data/buzzline_data.db
🔍 Sample Message Format
json
Copy
Edit
{
    "message": "I just learned Python! It's amazing.",
    "author": "Alice",
    "timestamp": "2025-02-20 14:35:20",
    "category": "tech",
    "sentiment": 0.85,
    "keyword_mentioned": "Python",
    "message_length": 42
}
🚀 Next Steps
✅ Optimize message processing
✅ Improve visualization animations
✅ Add alerting for high-frequency keywords

📌 Created by Huzaifa Nadeem

