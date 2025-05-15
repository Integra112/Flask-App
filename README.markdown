# Flask Email Backend

This is a Flask backend application that handles contact form submissions and sends emails using SMTP.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Set environment variables in Railway:
   - `EMAIL_ADDRESS`: Your email (e.g., `info@integrapvtltd.com`)
   - `EMAIL_PASSWORD`: Your email password (e.g., `@Purchased1@integra`)
   - `SMTP_SERVER`: `smtp.hostinger.com` (default)
   - `SMTP_PORT`: `465` (default)
3. Deploy on Railway and check logs.

## Usage
Send a POST request to `/send-email` with JSON data:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "1234567890",
  "project": "Website",
  "message": "Hello, I need help!"
}
```