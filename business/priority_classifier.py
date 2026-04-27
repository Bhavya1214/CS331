def assign_priority(category):

    if category == "Complaint":
        return "High"

    elif category == "Request":
        return "Medium"

    elif category == "Inquiry":
        return "Low"

    else:
        return "Low"