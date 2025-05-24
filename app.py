from flask import Flask, request, jsonify
from llama_cpp import Llama

# تحميل النموذج مع إعدادات مخصصة
llm = Llama(
    model_path="/models/model.gguf",
    n_ctx=512,
    n_threads=4  # حسب عدد الأنوية المتاحة على الخادم
)

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_prompt = data.get("prompt", "").strip()

    # تنسيق prompt بأسلوب chat-style (instruction / response)
    formatted_prompt = f"### Instruction:\n{user_prompt}\n\n### Response:\n"

    output = llm(formatted_prompt, max_tokens=80)

    # استخراج النص الناتج
    response_text = output["choices"][0]["text"].strip()

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=11434)
