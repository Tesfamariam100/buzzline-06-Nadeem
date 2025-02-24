🚀 Final README.md for Buzzline-06-Nadeem
md
Copy
Edit
# 📢 Buzzline 06 - Real-Time Keyword Tracking  
🚀 **Streaming Data Pipeline using Python, SQLite & Matplotlib**  

## **📌 Project Overview**  
This project **tracks keyword mentions** in real-time from a live data stream, stores them in an SQLite database, and **visualizes keyword trends dynamically** using Matplotlib.  

### **💡 How It Works**  
1️⃣ **Producer** → Generates messages and writes them to `project_live.jsonl`  
2️⃣ **Consumer** → Reads messages, extracts keywords, and tracks frequency in `buzzline_data.db`  
3️⃣ **Visualizer** → Displays **real-time keyword trends** using an animated bar chart  

---

## **📁 Project Structure**  
buzzline-06-Nadeem/ ├── producers/ │ ├── producer_keywords.py # Generates messages and writes to JSON ├── consumers/ │ ├── consumer_keyword_tracker.py # Reads and processes keyword mentions │ ├── consumer_visualizer.py # Displays real-time keyword trends ├── utils/ │ ├── utils_database.py # Database operations │ ├── utils_visualizer.py # Matplotlib animations ├── data/ │ ├── project_live.jsonl # Live streaming messages │ ├── buzzline_data.db # SQLite storage ├── .gitignore ├── .env ├── README.md ├── requirements.txt └── venv/

yaml
Copy
Edit

---

## **⚙️ How to Run the Project**  

### **1️⃣ Set Up the Environment**  
Activate Virtual Environment  
```sh
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
Install Dependencies

sh
Copy
Edit
pip install -r requirements.txt
2️⃣ Start the Producer
Generates and writes messages to data/project_live.jsonl.

sh
Copy
Edit
python producers/producer_keywords.py
3️⃣ Start the Consumer
Reads messages from project_live.jsonl, processes keyword mentions, and updates buzzline_data.db.

sh
Copy
Edit
python consumers/consumer_keyword_tracker.py
4️⃣ View Real-Time Keyword Trends
Runs the visualization script to track keyword mentions dynamically.

sh
Copy
Edit
python consumers/consumer_visualizer.py
📸 Live Visualization Preview

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