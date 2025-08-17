# Simple API Router with FastAPI and spaCy

## Overview
This project implements a simple API router that detects user intent using basic NLP (via spaCy) and routes requests to different functions like weather lookup, jokes, and addition.

## Features
- **getWeather(location)** → Simulated weather forecast for a given city.
- **getJoke()** → Returns a pre-written joke.
- **addNumbers(num1, num2)** → Returns the sum of two numbers.
- Basic **Intent Recognition** using keywords + Named Entity Recognition (NER) for location extraction.
- Number extraction via regex.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- spaCy
- English model for spaCy (`en_core_web_sm`)

## Installation
```bash
pip install fastapi uvicorn spacy
python -m spacy download en_core_web_sm
```

## Running the API
```bash
uvicorn main:app --reload
```
The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Example Queries
```bash
# Weather
curl "http://127.0.0.1:8000/process_query?query=What's%20the%20weather%20in%20London"

# Joke
curl "http://127.0.0.1:8000/process_query?query=Tell%20me%20a%20joke"

# Addition
curl "http://127.0.0.1:8000/process_query?query=Add%2012%20and%2034"
```

## Project Structure
```
.
├── main.py
├── README.md
└── model_doc.md
```

## License
MIT
