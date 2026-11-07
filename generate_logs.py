import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/flask_app.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

for i in range(10000):
    logging.info(f"Test log entry number {i}")

print("10000 log entries generated successfully!")