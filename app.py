from flask import Flask, request, jsonify
from fast_whisper import WhisperModel

app = Flask(__name__)

# 初始化模型
model = WhisperModel("turbo", device="cpu")  # 可以选择 "base", "small", "medium", "large"

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']
    transcription = model.transcribe(audio_file)

    return jsonify({
        "text": transcription["text"],
        "segments": transcription.get("segments", [])
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089)
