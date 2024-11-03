import base64
import json

from flask import Flask, request, render_template, jsonify
from googletrans import Translator
from gtts import gTTS

from core.ai_answer import get_gigachat_answer

app = Flask(__name__, static_folder='static')

with open('faq.json', 'r', encoding='utf-8') as f:
    faq_list = json.load(f)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/texttospeech", methods=["POST"])
def hello_world():
    query = request.json.get("text", "")
    answer = "Задай мне какой-то вопрос"

    if query:
        for faq in faq_list:
            if faq['question'].strip().lower() == query.strip().lower():
                answer = faq['answer']
                break
        else:
            answer = get_gigachat_answer(query)

    gTTS(text=answer, lang="ru", slow=False).save("output.mp3")

    with open("output.mp3", "rb") as file:
        audio_bytes = file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()

    return jsonify({"audio_base64": audio_base64, "answer": answer})

if __name__ == "__main__":
    app.run()
