import random
import requests
import json

api_token = "eyJjdHkiOiJqd3QiLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIiwiYWxnIjoiUlNBLU9BRVAtMjU2In0.GEAwqoTmzqar5_cmI_RCI4zbelIT-Fvc4zmAQi4wJlVxTCjWKSsJfhwkaxOxM4NKKghFPBYHRK2_yWlNZJJotUHYOCbOoPMK8xyj3EUqktfoR37WSGdNxe-ZSlaChYEDIKlHxJ99riO1BGo0-v0G6hTwgANBFAg2Ab6CkqGJZuDYlihd5fLx5bp7AQ5UarAEsd0asZxH8NdBqylr6h90Jdfl0_aJiBIlKUAQYsrh9D7YXb05oF7cMt7GjbPrZchmhdCYioZG1DrAQcqkVFohtNeAAqpG54-uRk6ljAC7wfxVJ-qfPeObSkRSyOC_ZSON0VYaNOGBYzBvfv-WsYT95w.Q49gXFhWgnU-S1RZV_gBsg.Eu4evb7wMW_FQyBOBbbnP4Y7JpjO67YOCAgVe3UuwPj_cfwJ1sjyFH_klmbiEhsXuT0xhiqVsswBhjz7ewIbQVpCJGzNO-p-LYNeIIqgqzgLq074akHQPk1CmFG3by4bZ0KDN7NNLeBfsYXpsDx5vABaF1slPlGoaXEj-CiwxidpI-e4vT9TIkdf2fZd-m-A_4y-djg8z7iHrt08c4PibkJguNRHm_2pIkEKDVgO7UIbEOa4MMi0oE1sgd0EnrSlLEEYqjArpqsIqf0XGzvUfQqHXXi0Vhdxgi0ih3v-3IggaV_cAZtFtZdmj6jVqm2-ZyE0_eqoU5XEt-DhJOdRTe6I_KiJP29VC_JSLcMS8UU-YhUP2R_DkRLwZfGNA-3paCled7uuAI1bSy5OoSE9lFqvDX1JnSLTvfIWPSK5dfLoupOQhAD2uDSUnW_GSy6wGaPdOTjk7LOoil8GgARgsCrKEtvPYD2kdTHX9KdJu2ID61yS52zR37g5eVQjYKIi9B8uHi608RMnt6UoCcyVAKwMCgtfUvZW45IFj71nwgFiTGeUO7M4mhCJ5p4XF-IZD1-1FgfyrIdhSuelrpR1NX2JD3mA58FbV99P72RqPJF6ZccpKd9IHeS1QjcGdamm-jmTBbe9YoBCOB1-mAR4iJSzBQfFN-mY3LeXfJHfZMmkm4ZZ8ASBm8LefNhuFPZ9aAsasegrKfGQlUD9OtQqj_07PVsDQ0dNj4DeSmKxPz8.rrDBJqy6cy1MyaL_AsYV22pU090atHXAOfYn0x1kYMI"
url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"




def clean_text(text: str) -> str:
    result = ""
    for char in text:
        if any([char.isalpha(), char.isdigit(), char.isspace()]):
            result += char

    return result


def get_gigachat_answer(query: str) -> str:
    try:
        payload = json.dumps({
            "model": "GigaChat",
            "messages": [
                {
                    "role": "system",
                    "content": "Отвечай как преподаватель Сургутского Государственного университета. И знаешь все ответы на базовые вопросы студентов. Говори о себе в женском роде."
                },
                {
                    "role": "user",
                    "content": query
                }
            ],
            "stream": False,
            "update_interval": 0
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {api_token}',
            'X-Client-ID': 'ac68c253-d4c9-48c5-8001-44d1c251160c',
            'X-Session-ID': 'b6874da0-bf06-410b-a150-fd5f9164a0b2',
            'X-Request-ID': '79e41a5f-f180-4c7a-b2d9-393086ae20a1'
        }

        response = dict(requests.request("POST", url, headers=headers, data=payload, verify=False).json())
        if not response.get("choices", []):
            return "Увы, я не могу ответить на этот вопрос"

        return response.get("choices", [{}])[0].get("message", {}).get("content")

    except Exception as e:
        return "Упс, кажется произошла ошибка"
