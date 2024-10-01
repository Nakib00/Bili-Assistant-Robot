import random
import numpy as np
import pickle
import json
import nltk
from nltk.tokenize import word_tokenize
from tensorflow.keras.optimizers import SGD
from keras.layers import Dense, Dropout
from keras.models import Sequential
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Initialize lists
words = []
classes = []
documents = []
ignore_words = ["?", "!"]

# Function to load intents and prepare data
def load_intents(file_name):
    try:
        with open(file_name, encoding="utf-8") as data_file:
            intents = json.load(data_file)
    except FileNotFoundError as e:
        print(f"Error: `{file_name}` file not found.", e)
        return [], [], []
    
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            w = word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent["tag"]))
            if intent["tag"] not in classes:
                classes.append(intent["tag"])
    return words, classes, documents

# Load English intents
english_words, english_classes, english_documents = load_intents("intents.json")
# Load Bengali intents
bengali_words, bengali_classes, bengali_documents = load_intents("intents_bengali.json")

# Combine words and classes from both languages, removing duplicates
words = sorted(list(set(words + bengali_words)))
classes = sorted(list(set(english_classes + bengali_classes)))  # Ensure all classes are included

# Combine documents from both languages
documents += bengali_documents  # Add Bengali documents to the existing list

# Check if documents, classes, and words are correctly prepared
print(f"{len(english_documents)} English documents loaded.")
print(f"{len(bengali_documents)} Bengali documents loaded.")
print(f"Total documents: {len(documents)}")
print(f"{len(classes)} classes: {classes}")
print(f"{len(words)} unique lemmatized words: {words}")

# Save words and classes as pickle files
pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))

# Create training data
training = []
output_empty = [0] * len(classes)

# Process English documents
for doc in english_documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Process Bengali documents
for doc in bengali_documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [word.lower() for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Shuffle the training data
random.shuffle(training)

# Create train_x and train_y
train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])

print(f"Training data created with shapes: train_x: {train_x.shape}, train_y: {train_y.shape}")

# Build the Sequential model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation="softmax"))
model.summary()

# Compile the model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

# Train the model
hist = model.fit(train_x, train_y, epochs=10000, batch_size=5, verbose=1)

# Save the model
model.save("model_combined.h5")
print("Combined model created and saved as `model_combined.h5`")
