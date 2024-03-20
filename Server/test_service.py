import numpy as np

# Define possible sentiment values
SENTIMENTS = ['POSITIVE', 'NEGATIVE', 'NEUTRAL', 'MIXED']

# Define possible entity types
ENTITY_TYPES = ['PERSON', 'LOCATION', 'ORGANIZATION', 'DATE', 'QUANTITY', 'TITLE']

def get_sentiment(text=None):
    # Return a random sentiment value and score
    random_scores = np.array([np.random.rand() for _ in SENTIMENTS])
    random_scores = random_scores / sum(random_scores)
    sentiment_score = {senti: score for senti, score in zip(SENTIMENTS, random_scores)}
    sentiment = SENTIMENTS[random_scores.argmax()]
    return sentiment, sentiment_score

def get_entities(text):
    # Generate a random number of entities
    words = text.split()
    num_entities = np.random.randint(0, len(words))  # Adjust range as needed

    # Generate random entities
    entities = []
    for _ in range(num_entities):
        # Select a random word from the remaining words
        entity_text = np.random.choice(words)
        entity_type = np.random.choice(ENTITY_TYPES)
        entities.append({'Text': entity_text, 'Type': entity_type})
        
        # Remove the selected word from the list of words
        words.remove(entity_text)
    
    return entities

# Test the functions
# print(get_sentiment())
# print(get_entities('My name is Dhruv Yadav. I am a student'))
