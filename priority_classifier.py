def assign_priority(category):
    if category in ["Complaint", "Needs Review"]:
        return "High"
    if category == "Request":
        return "Medium"
    return "Low"