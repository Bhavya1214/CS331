# Fix path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your actual function
from business.spam_detector import detect_spam


# ===============================
# Custom classification wrapper
# ===============================
def classify_email(text):
    text_lower = text.lower()

    # 1. Spam check
    if detect_spam(text):
        return "Spam"

    # 2. Complaint check
    elif "complaint" in text_lower or "not satisfied" in text_lower or "issue" in text_lower:
        return "Complaint"

    # 3. Important check
    elif "meeting" in text_lower or "schedule" in text_lower:
        return "Important"

    # 4. Default
    elif text.strip() == "":
        return "Normal"

    else:
        return "Normal"


# ===============================
# Test Cases
# ===============================
test_cases = [
    ("TC_01", "You won a lottery! Claim now!!!", "Spam"),
    ("TC_02", "I am not satisfied with your service", "Complaint"),
    ("TC_03", "Meeting scheduled at 10 AM tomorrow", "Important"),
    ("TC_04", "Hello, how are you?", "Normal"),
    ("TC_05", "Urgent complaint regarding billing issue", "Complaint"),
    ("TC_06", "", "Normal"),
    ("TC_07", "FREE money offer just for YOU", "Spam"),
    ("TC_08", "!!! Win $$$ now !!!", "Spam"),
    ("TC_09", "Meeting about free resources tomorrow", "Important"),
]


# ===============================
# Execution
# ===============================
print("\n===== TEST EXECUTION STARTED =====\n")

pass_count = 0
fail_count = 0

for tc_id, input_text, expected in test_cases:
    actual = classify_email(input_text)
    status = "Pass" if actual == expected else "Fail"

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    print("=" * 50)
    print(f"Test Case ID : {tc_id}")
    print(f"Input        : {input_text}")
    print(f"Expected     : {expected}")
    print(f"Actual       : {actual}")
    print(f"Status       : {status}")

print("\n===== TEST SUMMARY =====")
print(f"Total Test Cases : {len(test_cases)}")
print(f"Passed           : {pass_count}")
print(f"Failed           : {fail_count}")
print("========================\n")