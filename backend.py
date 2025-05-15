from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)
CORS(app)

# Environment variables for email configuration
EMAIL_ADDRESS = os.environ.get("info@integrapvtltd.com")
EMAIL_PASSWORD = os.environ.get("@Purchased1@integra")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.hostinger.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 465))

# Check if environment variables are set
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD must be set in environment variables")

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    project = data.get("project")
    message = data.get("message")

    try:
        msg = EmailMessage()
        msg["Subject"] = "New Contact Form Submission"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS
        msg.set_content(f"""
Name: {name}
Email: {email}
Phone: {phone}
Project Type: {project}
Message: {message}
""")

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # For local development only
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
