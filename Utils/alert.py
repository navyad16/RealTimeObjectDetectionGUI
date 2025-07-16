import smtplib
from email.mime.text import MIMEText

""""## ❌ **Direct Gmail password ఉపయోగించడం ఇకపై సహించబడదు**

Google ఇప్పుడు **direct login using email+password** ను అనుమతించదు unless you use:

## ✅ **App Password (Safe way to use SMTP with Gmail)**
### ☑️ Step-by-step:
### 🔐 1. **Enable 2-Step Verification on your Gmail account**
➡️ Login into your Gmail and visit:
**🔗 [https://myaccount.google.com/security](https://myaccount.google.com/security)**
➡️ "Signing in to Google" సెక్షన్ లో
👉 **Turn ON 2-Step Verification**

### 🔑 2. **Generate an App Password**
➡️ Same security settings page లోకి వెళ్ళండి:
🔗 [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
* App: **Mail**
* Device: **Other (Custom name)** → `PythonScript`
* Click **Generate**

👉 మీరు 16-digit password ను పొందుతారు: ఉదా:xxyy zzww aabb ccdd
"""
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
TO_EMAIL = "receiver_email@gmail.com"

def send_email_alert(label):
    subject = f"Alert: {label.upper()} detected!"
    msg = MIMEText(f"The object '{label}' was detected in the camera feed.")
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    except Exception as e:
        print("Email error:", e)
