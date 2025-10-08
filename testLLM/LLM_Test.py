import requests

url = "http://localhost:12434/engines/v1/chat/completions"

data= {
    "model": "ai/smollm2:latest",
    "messages": [
        {"role": "system", 
         "content": "Hello, how are you today?"
         },
        {"role": "user", 
         "content": "I'm doing well, thank you! How can I assist you today?"
         }
    ],
    }


response = requests.post(url, json=data)
response.raise_for_status()  # Raise an error for bad responses

print(response.json()["choices"][0]["message"]["content"])