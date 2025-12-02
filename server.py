from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "TTS server đang chạy!"

@app.route("/tts")
def tts():
    text = request.args.get("text", "").strip()
    lang = request.args.get("lang", "vi")

    if not text:
        return "Missing text", 400

    params = {
        "ie": "UTF-8",
        "q": text,
        "tl": lang,
        "client": "tw-ob"
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://translate.google.com/"
    }

    r = requests.get(
        "https://translate.google.com/translate_tts",
        params=params,
        headers=headers,
        stream=True
    )

    return Response(r.iter_content(1024),
                    content_type="audio/mpeg")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
