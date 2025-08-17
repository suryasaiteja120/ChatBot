from fastapi import FastAPI, Query
import spacy
import re

app = FastAPI(title="Simple API Router with spaCy NLP")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def getWeather(location: str):
    return f"The weather in {location} is sunny with a high of 25°C."

def getJoke():
    return "Why don’t skeletons fight each other? They don’t have the guts."

def addNumbers(num1: float, num2: float):
    return f"The sum of {num1} and {num2} is {num1 + num2}."

def extract_numbers(text: str):
    return [float(num) for num in re.findall(r"\b\d+(?:\.\d+)?\b", text)]

@app.get("/process_query")
def process_query(query: str = Query(..., description="User query text")):
    doc = nlp(query.lower())

    if "weather" in query.lower():
        location = None
        for ent in doc.ents:
            if ent.label_ == "GPE":
                location = ent.text
                break
        if location:
            return {"query": query, "intent": "getWeather", "location": location, "result": getWeather(location)}
        else:
            return {"query": query, "intent": "getWeather", "error": "No location found."}

    elif "joke" in query.lower():
        return {"query": query, "intent": "getJoke", "result": getJoke()}

    elif "add" in query.lower() or "sum" in query.lower():
        nums = extract_numbers(query)
        if len(nums) >= 2:
            return {"query": query, "intent": "addNumbers", "numbers": nums[:2], "result": addNumbers(nums[0], nums[1])}
        else:
            return {"query": query, "intent": "addNumbers", "error": "Need two numbers to add."}

    return {"query": query, "intent": "unknown", "error": "Intent not recognized."}

@app.get("/")
def home():
    return {"message": "Welcome to the Simple API Router. Use /process_query?query=your_text"}
