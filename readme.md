Flask Logrotate Project
Project Description

This project demonstrates how to configure Logrotate for a Flask application, generate large amounts of log data, perform manual log rotation, and verify archived log files.

Project Structure
text
flask-logrotate/
│
├── app.py
├── requirements.txt
├── generate_logs.py
├── flask_app.conf
├── README.md


Requirements
Python 3
Flask
Linux (Ubuntu)
Logrotate
Installation
Step 1: Install dependencies
bash
sudo apt update
sudo apt install logrotate -y
pip install -r requirements.txt

Step 2: Run Flask application
bash
python3 app.py


Open your browser:

http://127.0.0.1:5000/

Step 3: Generate log entries

Open another terminal and run:

bash
python3 generate_logs.py


This generates 10,000 log entries in logs/flask_app.log.

Step 4: Configure Logrotate

Update the log file path in flask_app.conf.

Copy the configuration:

bash
sudo cp flask_app.conf /etc/logrotate.d/flask_app

Step 5: Run Logrotate manually
bash
sudo logrotate -f /etc/logrotate.d/flask_app

Step 6: Verify archived files
bash
ls -lh logs/


Check compressed archive:

bash
gzip -t logs/flask_app.log.1.gz

Expected Output
text
logs/
├── flask_app.log
└── flask_app.log.1.gz

Project Tasks Completed
Created /etc/logrotate.d/flask_app configuration.
Generated 10,000 log entries using a load test.
Executed Logrotate manually.
Verified archived and compressed log files.
Conclusion

Successfully configured Logrotate for a Flask application, simulated log growth, performed manual log rotation, and verified the archived log files.