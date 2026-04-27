from flask import Flask, request, jsonify, render_template
from business.preprocessor import clean_text
from business.spam_detector import detect_spam
from business.ml_model import predict_category
from business.priority_classifier import assign_priority
from business.response_generator import generate_response
from business.workflow import process_email
from flask import render_template
from data.db import get_connection
from business.email_fetcher import fetch_emails
from flask import session, redirect, url_for


app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route("/")
def home():
    return "Email Automation System Running"


@app.route("/test")
def test():
    text = "Hello!!! Visit https://example.com NOW!!!"
    cleaned = clean_text(text)
    return cleaned


@app.route("/spamtest")
def spamtest():

    text = "You win a free prize click here now"

    cleaned = clean_text(text)

    spam = detect_spam(cleaned)

    return f"Spam detected: {spam}"

@app.route("/mltest")
def mltest():

    text = "I want refund for my order"

    cleaned = clean_text(text)

    category = predict_category(cleaned)

    return f"Predicted Category: {category}"

@app.route("/prioritytest")
def prioritytest():

    text = "I want refund for my order"

    cleaned = clean_text(text)

    category = predict_category(cleaned)

    priority = assign_priority(category)

    return f"Category: {category} | Priority: {priority}"


@app.route("/responsetest")
def responsetest():

    text = "I want refund for my order"

    cleaned = clean_text(text)

    category = predict_category(cleaned)

    priority = assign_priority(category)

    response = generate_response(category)

    return f"Category: {category} | Priority: {priority} | Response: {response}"

@app.route("/process_email", methods=["POST"])
def process_email_api():

    data = request.json
    content = data["content"]

    result = process_email(content)

    return jsonify(result)

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")


@app.route("/stats")
def stats():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM emails")
    total = cursor.fetchone()[0]

    conn.close()

    return {"total": total}


@app.route("/category_stats")
def category_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*)
        FROM emails
        GROUP BY category
    """)

    rows = cursor.fetchall()
    conn.close()

    stats = {
        "Request": 0,
        "Complaint": 0,
        "Inquiry": 0,
        "Spam": 0
    }

    for category, count in rows:
        stats[category] = count

    return stats


@app.route("/fetch_emails")
def fetch_emails_api():

    emails = fetch_emails()

    results = []

    for email_data in emails:

        content = email_data["subject"]
        sender = email_data["from"]

        import re
        match = re.findall(r'<(.+?)>', sender)
        if match:
            sender = match[0]

        result = process_email(content, sender)

        results.append({
            "from": sender,
            "result": result
        })

    return {"processed_emails": results}




@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # simple login (demo purpose)
        if username == "admin" and password == "admin123":

            session["user"] = username
            return redirect("/dashboard")

        else:
            return "Invalid Credentials"

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.pop("user", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)