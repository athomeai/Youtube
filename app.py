import requests
import os

url = "http://localhost:11434/api/generate"
model = "dolphin"
prompt = input("Enter your prompt: ")
data = {
    "model": model,
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)

try:
    json_response = response.json()
    print(json_response['response'])
except Exception as e:
    print("Error parsing JSON:", e)
