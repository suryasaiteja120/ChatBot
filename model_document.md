# Model Document – NLP Approach

## Objective
The goal is to detect user intent from natural language queries and route them to the appropriate function.

## Approach
We used a **keyword + Named Entity Recognition (NER)** approach:
1. **Keyword Matching** – Check if the query contains words like `"weather"`, `"joke"`, `"add"`, `"sum"` to determine intent.
2. **Named Entity Recognition** – Use spaCy's `en_core_web_sm` model to detect city names (GPE entities) for weather queries.
3. **Regex Number Extraction** – Use a regular expression to extract numbers for the addition function.

## Why this approach?
- **Simplicity** – Keywords and NER are lightweight and easy to implement for a prototype.
- **Extensibility** – Additional intents can be added by extending keyword sets and/or using more advanced NER models.
- **Performance** – Avoids the overhead of a heavy ML model while maintaining reasonable accuracy for structured queries.

## Example
- Input: `"What's the weather in Paris?"`
  - Keyword: `"weather"` → Intent: getWeather
  - NER: `"Paris"` → Location
- Input: `"Add 12 and 45"`
  - Keyword: `"add"` → Intent: addNumbers
  - Regex: `12`, `45` → Numbers
- Input: `"Tell me a joke"`
  - Keyword: `"joke"` → Intent: getJoke
