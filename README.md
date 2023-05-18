# microservice

Website Word Frequency Microservice
This microservice is built in Python and allows you to retrieve the unique words and their frequency of occurrence from a static website. Simply provide the URL of the website, and the microservice will extract the words, count their frequencies, and return the results in JSON format.

How to Use
Install the necessary dependencies by running the following command:

bash
Copy code
pip install -r requirements.txt
Start the microservice by running the following command:

bash
Copy code
python app.py
Once the microservice is running, you can send a POST request to the /analyze endpoint with the URL in the JSON payload. The microservice will extract the words and their frequencies from the webpage and return the results in JSON format.

Example request using cURL:

bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://localhost:5000/analyze
The response will be a JSON object containing the list of words along with their frequencies.

API Endpoint
Analyze Website
Endpoint: /analyze
Method: POST
Request Payload:

json
Copy code
{
  "url": "https://example.com"
}
Response Format: JSON

Response Example
json
Copy code
[
  {
    "word": "the",
    "frequency": 10
  },
  {
    "word": "example",
    "frequency": 5
  },
  {
    "word": "website",
    "frequency": 2
  },
  {
    "word": "is",
    "frequency": 7
  },
  ...
]
Dependencies
Flask: A micro web framework for building the API endpoints.
Requests: A library for making HTTP requests to fetch the website content.
BeautifulSoup: A library for parsing HTML content and extracting text.
Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
