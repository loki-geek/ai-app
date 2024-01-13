#!/usr/bin/python
import google.generativeai as genai

inputMsg = input("Enter your prompt: ")

API_KEY = 'AIzaSyBLAuKEfR5QsUMpn8SANRUMcc8gNQZQstU'
gemini_api_key = API_KEY
genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(inputMsg)
print(response.text)
