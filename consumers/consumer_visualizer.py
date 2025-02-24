import sqlite3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Load environment variables
database_path = os.getenv("DATABASE_FILE", "./data/buzzline_data.db")

def fetch_data():
    """Fetch keyword counts from the SQLite database."""
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT keyword, count FROM keyword_counts ORDER BY count DESC LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return data

def update(frame):
    """Update function for Matplotlib animation."""
    ax.clear()
    
    # Fetch latest keyword data
    data = fetch_data()
    if not data:
        return

    keywords, counts = zip(*data)

    # Plot bar chart
    ax.barh(keywords, counts, color='blue')
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Keywords")
    ax.set_title("📊 Real-Time Keyword Tracking")

# Set up Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 5))
ani = animation.FuncAnimation(fig, update, interval=2000)  # Update every 2 seconds

# Show the animated visualization
plt.show()
