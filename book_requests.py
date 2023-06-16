import requests

url = "http://127.0.0.1:8070/api/books"
response = requests.get(url)

if response.status_code == 200:
    # Request was successful
    data = response.json()
    print(data)
else:
    # Request was unsuccessful
    print("Error:", response.status_code)
    print(response.text)

**********************************************************


import requests
from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d")

url = "http://127.0.0.1:8070/api/books/"

# Data to be sent in the request body
data = {
    "title": "Book Title",
    "author": "John Doe",
    "publication_date": current_date,
    "price": 10.5
}

response = requests.post(url, json=data)

if response.status_code == 201:
    # Request was successful
    print("Book created successfully!")
    book_id = response.json()["id"]
    print("Book ID:", book_id)
else:
    # Request was unsuccessful
    print("Error:", response.status_code)
    print(response.text)


**********************************************************

import requests

url = "http://127.0.0.1:8070/api/books/1"
response = requests.get(url)

if response.status_code == 200:
    # Request was successful
    data = response.json()
    print(data)
else:
    # Request was unsuccessful
    print("Error:", response.status_code)
    print(response.text)


**********************************************************

import requests
from datetime import datetime
url = "http://127.0.0.1:8070/api/books/1/"  
data = {
    "title": "Updated Book Title",
    "author": "Jane Smith",
    "publication_date": current_date,
    "price": 10.5}

response = requests.put(url, json=data) 

if response.status_code == 200:
    # Request was successful
    print("Book updated successfully!")
    print("Response:", response.json())
else:
    # Request was unsuccessful
    print("Error:", response.status_code)
    print(response.text)


**********************************************************

import requests

url = "http://127.0.0.1:8070/api/books/1"  

response = requests.delete(url)

if response.status_code == 204:
    # Request was successful
    print("Book deleted successfully!")
else:
    # Request was unsuccessful
    print("Error:", response.status_code)
    print(response.text)


