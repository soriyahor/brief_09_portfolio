import json
import requests
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
from openai import AzureOpenAI
from config import API_PY, API_AZURE

# Fetch the HTML content from the URL
response = requests.get("http://soriyab09portfolio-front.francecentral.azurecontainer.io:8001")
soup = BeautifulSoup(response.content, "html.parser")

app = FastAPI()

headers = {"Authorization": f"Bearer {API_PY}"}


origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/test/{prompt}", description="test!")
def test(prompt):
    return "cc"

@app.post("/{prompt}")
async def chat(prompt):
        data = soup.get_text().strip()
        # provider = "meta"
        # url = "https://api.edenai.run/v2/text/chat"
        # payload = {
        #     "providers": provider,
        #     "text": "",
        #     "chatbot_global_action": f"You are Soriya, the owner of the website of which here is the content : {data}",
        #     "previous_history": [],
        #     "temperature": 0.0,
        #     "max_tokens": 150,
        #     "fallback_providers": ""
        # }
        # payload["text"] = prompt
        # response = requests.post(url, json=payload, headers=headers)
        # result = json.loads(response.text)
        # rp = result[provider]
        # print(rp)
        # answer = rp['generated_text']
        # return(answer)



        client = AzureOpenAI(
            azure_endpoint = "https://openai-lok.openai.azure.com/", 
            api_key= {API_AZURE},  
            api_version="2024-02-15-preview"
        )

        message_text = [{"role":"system","content":"You are an AI assistant that helps people find information. You know this :{data}."},{"role": "user", "content": f"{prompt}"}]

        completion = client.chat.completions.create(
            model="gpt35-latest", # model = "deployment_name"
            messages = message_text,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        completion_text = completion.choices[0].message.content

        return completion_text



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
