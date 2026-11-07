from flask import Flask
import logging
import os

app = Flask(__name__)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/flask_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Home page visited")
    return "Flask Application Running!"

@app.route("/log")
def generate():
    for i in range(100):
        logging.info(f"Log entry number {i}")
    return "100 log entries generated!"

if __name__ == "__main__":
    app.run(debug=False)