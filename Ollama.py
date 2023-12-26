import requests

# API endpoint and payload data
url = 'http://192.168.1.17:11434/api/chat'
payload = {
    "model": "llama2",
    "messages": [
        {
            "role": "user",
            "content": "why is the sky blue?"
        }
        # Add more messages if needed in the chat
    ]
}

# Send the POST request
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    # Process the response
    print(response.json())  # Print the response JSON data
else:
    print("Error:", response.status_code, response.text)  # Print the error status and response text
