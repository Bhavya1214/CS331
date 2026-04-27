from db import get_connection

def classify_email(content):
    content = content.lower()
    if "win" in content or "lottery" in content:
        return "Spam"
    elif "complaint" in content or "issue" in content:
        return "Complaint"
    else:
        return "Important"


def save_email(sender, content):
    conn = get_connection()
    cursor = conn.cursor()

    category = classify_email(content)

    query = """
    INSERT INTO emails (sender, content, cleaned_text, category, priority, response)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    cleaned_text = content.lower()
    priority = "Medium"
    response = "Auto-generated response"

    cursor.execute(query, (sender, content, cleaned_text, category, priority, response))

    conn.commit()
    cursor.close()
    conn.close()


def get_emails_by_category(category):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM emails WHERE category=%s"
    cursor.execute(query, (category,))

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result