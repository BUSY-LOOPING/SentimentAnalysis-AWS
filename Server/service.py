import boto3

def get_sentiment(text):
    comprehend = boto3.client(service_name='comprehend', region_name='ca-central-1')
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    sentiment_score = response['SentimentScore']
    sentiment = response['Sentiment']
    return sentiment, sentiment_score

# def get_entities(text):
#     comprehend = boto3.client(service_name='comprehend', region_name='ca-central-1')
#     response = comprehend.detect_entities(Text=text, LanguageCode='en')
#     entities = response['Entities']
#     return entities
    
# text = 'I am very sad.'
# print(get_sentiment(text))
# print(get_entities(text))