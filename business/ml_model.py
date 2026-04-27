from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [

# Complaint
"I am unhappy with your service",
"My order is damaged",
"This service is terrible",
"My product is defective",
"I want to file a complaint",
"The support team is very bad",
"My delivery is late",
"I received a broken item",
"Very poor service experience",

# Request
"I want a refund",
"Please help me reset my password",
"I need support for my account",
"Please process my refund",
"Can you assist me with my order",
"I need help with login",
"Please update my order",
"I want to change my address",

# Inquiry
"What are your pricing plans",
"Can you give more details",
"I need information about the product",
"Please explain this feature",
"Tell me more about your services",
"What services do you offer",
"Can you share product details",

# Spam / Promotion
"Congratulations you won money",
"You have won a lottery",
"Click this link to win prize",
"Earn money quickly online",
"Claim your free reward now",
"Limited time offer buy now",
"Huge discount available",
"Special deal just for you"
]

labels = [

"Complaint","Complaint","Complaint","Complaint","Complaint","Complaint","Complaint","Complaint","Complaint",

"Request","Request","Request","Request","Request","Request","Request","Request",

"Inquiry","Inquiry","Inquiry","Inquiry","Inquiry","Inquiry","Inquiry",

"Spam","Spam","Spam","Spam","Spam","Spam","Spam","Spam"
]

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,2))

X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=200)
model.fit(X, labels)


def predict_category(text):

    vec = vectorizer.transform([text])
    return model.predict(vec)[0]