# README for Intent Dataset

Welcome to the Intent Dataset repository! This dataset is designed for chatbot training and is structured in JSON format. It includes various intents, patterns, and responses in both Bengali and English languages.

## JSON Format Structure

The JSON file contains an array of `intents`. Each intent consists of the following fields:

- **tag**: A unique identifier for the intent. This should be a lowercase string without spaces.
- **patterns**: An array of strings that represent different ways users may express this intent. These patterns can be in any language (Bengali or English).
- **responses**: An array of strings that represent the bot's responses to the matched patterns.

### Example Structure (English)

```json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "Hi",
                "How are you?",
                "Is anyone there?",
                "Hello",
                "Good day"
            ],
            "responses": [
                "Hello, thanks for visiting",
                "Good to see you",
                "Hi dear, how can I help?"
            ]
        }
    ]
}
