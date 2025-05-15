from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.environ.get("info@integrapvtltd.com")
EMAIL_PASSWORD = os.environ.get("@Purchased1@integra")
SMTP_SERVER = "smtp.hostinger.com"
SMTP_PORT = 465

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    try:
        msg = EmailMessage()
        msg['Subject'] = 'New Contact Form Submission'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"""\
Name: {data.get("name")}
Email: {data.get("email")}
Phone: {data.get("phone")}
Project: {data.get("project")}
Message: {data.get("message")}
""")
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# for gunicorn
if __name__ == "__main__":
    app.run()
