from fastapi import FastAPI
import random

app = FastAPI()

# Sample Captions & Hashtags Data
sample_data = {
    "travel": {"caption": "Exploring new places! ✈️🌍", "hashtags": ["#wanderlust", "#travelgram", "#adventure"]},
    "fitness": {"caption": "Sweat, smile, repeat! 💪🔥", "hashtags": ["#fitlife", "#workout", "#motivation"]},
    "food": {"caption": "Delicious moments! 🍕🍔", "hashtags": ["#foodie", "#yummy", "#delish"]},
}

@app.get("/")
def home():
    return {"message": "Caption & Hashtag API is running!"}

@app.get("/generate")
def generate(topic: str):
    topic = topic.lower()
    if topic in sample_data:
        return sample_data[topic]
    else:
        return {"caption": "Stay positive, keep shining! 🌟", "hashtags": ["#positivevibes", "#happy", "#inspiration"]}
