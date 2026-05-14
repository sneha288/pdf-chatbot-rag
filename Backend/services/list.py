import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

models = genai.list_models()

for model in models:

    print("MODEL NAME:", model.name)

    print("SUPPORTED METHODS:")

    for method in model.supported_generation_methods:
        print("-", method)

    print("-" * 50)