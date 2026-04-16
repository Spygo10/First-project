

export GEMINI_API_KEY="AQ.Ab8RN6I06NcyJ7RZxiLOe1yVilzSMBIpIkkXa94mpwVhsndLzQ"


from google import genai
import os

client = genai.client(api_key=os.environ["GEMINI_API_KEY"])

from google.genai import types 
config = types.GenerateContentConfig(    
    temperature=0.2,         # 0=deterministico, 1=creativo    
    max_output_tokens=1024,  # Lunghezza massima risposta 
    )

from google.genai import types
config = types.GenerateContentConfig(
    system_instruction="""Sei un esperto Cyber Security Analyst. Analizza i dati forniti e rispondi in modo tecnico ma comprensibile.    
    Se non sei sicuro, dillo esplicitamente."""
)

response = client.models.generate_content(    
model="gemini-flash-latest",    
contents="Analizza questo log...",    
config=config )


while True:
    domanda = input("Tu: ")
    if domanda.lower() == "Esci":
        print("Arrivederci!")
        break

    response = client.generate_content(
        model="gemini-2.0-flash",
        config=config,
    )
    print(f"AI: {response.text}\n")