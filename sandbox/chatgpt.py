import requests
import os
import google.generativeai as genai

API_KEY= "AIzaSyD2C7OANbPonIaqiDPTFVsS8MWQbpQbPqE"
genai.configure(api_key=API_KEY)

prompt = """traduis "je suis en DEV IA" en anglais"""


model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

#hearders = {
#   "Content-Type": "application/json",
#   "Authorization": f"Bearer {api_key}"
#}
#parameters= {
#    "model": model,
#    "prompt": prompt,
#   "max_tokens": 100
#}
#response = requests.post(f"https://api.openai.com/v1/completions", headers=hearders, json=parameters).json()
print(response.text)