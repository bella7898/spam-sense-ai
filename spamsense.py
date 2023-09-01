from pip._vendor import requests

API_URL = "https://api-inference.huggingface.co/models/BW7898/spam_message_classification"

headers = {"Authorization": "Bearer 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"}


def query(payload):
  response = requests.post(API_URL, headers=headers, json=payload)
  return response.json()