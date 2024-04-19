import json
import requests


def chat_with_edenai():

    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNTdmYzhjYjQtMGYyNS00NTU1LWJjZGItYjQ0NmFkMGQ5YTZiIiwidHlwZSI6ImFwaV90b2tlbiJ9.cOiJ-UUpZjQVcup2RNdQr-YV6vRAf1zIsrfrFzwXJ9U"}

    url = "https://api.edenai.run/v2/text/chat"

    provider = "meta"

    payload = {
        "providers": provider,
        # "model": "llama2-13b-chat-v1",
        "text": "",
        "chatbot_global_action": "Act as an assistant, and answer in less than 100 words",
        "previous_history": [],
        "temperature": 0.8,
        "max_tokens": 150,
        "fallback_providers": ""
    }

    while True:
        prompt = input("q:")
        payload["text"] = prompt

        if prompt in ["quit", "logout", "exit", "bye"]:
            break

        response = requests.post(url, json=payload, headers=headers)
        result = json.loads(response.text)
        rp = result[provider]
        print(rp['generated_text'])

        payload["previous_history"].append({"role":"user", "message": prompt})
        # print(rp['generated_text'])
        payload["previous_history"].append({"role":"assistant", "message":rp['generated_text']})
        print(payload["previous_history"])

chat_with_edenai()




