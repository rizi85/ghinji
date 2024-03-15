import google.generativeai as genai
import os

# Get API key from environment variable GEMINI_API_KEY
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# List available models
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Use Gemini model
model = genai.GenerativeModel('gemini-pro')

# Query model
response = model.generate_content("What is the meaning of life?")

# Get response
print(response.text)