from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
from service import get_sentiment

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():     
    return render_template('index.html')
 
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        sentiment, sentiment_score = get_sentiment(text)
        return render_template('index.html', text=text, sentiment=sentiment, sentiment_score=sentiment_score)
      
if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=False) 
    print('====SERVER LIVE====')
    http_server = WSGIServer(('0.0.0.0', 80), app)
    http_server.serve_forever()
