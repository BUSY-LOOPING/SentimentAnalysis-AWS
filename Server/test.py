import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:80/analyze'
data = {'text': 'This is a great day!'}
response = requests.post(url, data=data)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    sentiment = soup.find('p')
    sentiment_scores = soup.find_all('li')
    print(f"{sentiment.text}")
    print(f'Sentiment Scores: \n {[senti_score.text for senti_score in sentiment_scores]}')
    
else:
    print("Error occurred while making the request.")