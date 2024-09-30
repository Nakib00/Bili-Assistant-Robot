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
```
### Example Structure (Bangla)
```json
{
    "intents": [
        {
            "tag": "bangla_greeting",
            "patterns": [
                "হাই",
                "তুমি কেমন আছ?",
                "কেউ আছেন?",
                "হ্যালো",
                "শুভ দিন"
            ],
            "responses": [
                "হ্যালো, আপনাকে স্বাগতম",
                "আপনাকে দেখে ভালো লাগছে",
                "হাই প্রিয়, আমি কিভাবে সাহায্য করতে পারি?"
            ]
        },
        {
            "tag": "location_query",
            "patterns": [
                "অডিটোরিয়াম কোথায়?",
                "অডিটোরিয়ামে কিভাবে যাব?",
                "DMK বিল্ডিং কোথায়?",
                "সুইমিং পুলে কিভাবে যাব?",
                "মাল্টিপারপাস হলে যাওয়ার পথ দেখাও"
            ],
            "responses": [
                "মানচিত্রে দেখছি...",
                "আপনার জন্য মানচিত্র খুলছি...",
                "মানচিত্রে রিডিরেক্ট করছি..."
            ]
        }
    ]
}
