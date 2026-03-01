from data.db import get_connection

def generate_response(category):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT template FROM templates WHERE category=%s", (category,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]

        if category == "Needs Review":
            return "Your email has been forwarded for manual review."

        if category == "Spam":
            return "This email has been marked as spam."

        return "Thank you for contacting us."

    except:
        return "System error."