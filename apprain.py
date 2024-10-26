from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Khởi tạo database
def init_db():
    conn = sqlite3.connect('rain_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rain_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  value TEXT,
                  timestamp DATETIME)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/api/rain-data', methods=['POST'])
def receive_rain_data():
    data = request.json
    rain_value = data['rain_value']
    timestamp = datetime.now()

    conn = sqlite3.connect('rain_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO rain_data (value, timestamp) VALUES (?, ?)",
              (rain_value, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 200

@app.route('/')
def index():
    conn = sqlite3.connect('rain_data.db')
    c = conn.cursor()
    c.execute("SELECT value, timestamp FROM rain_data ORDER BY timestamp DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
