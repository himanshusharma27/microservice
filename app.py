import requests
from bs4 import BeautifulSoup
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

def extract_words(url):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract text content from HTML
    text = soup.get_text()
    
    # Split the text into individual words
    words = text.split()
    
    # Count the frequency of each word using Counter
    word_counts = Counter(words)
    
    return word_counts

@app.route('/analyze', methods=['POST'])
def analyze_website():
    # Get the URL from the request's JSON payload
    url = request.json['url']
    
    # Extract the words and their frequencies
    word_counts = extract_words(url)
    
    # Convert the word counts to a list of dictionaries
    results = [{'word': word, 'frequency': count} for word, count in word_counts.items()]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run()
