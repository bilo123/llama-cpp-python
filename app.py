from flask import Flask, request, jsonify
from llama_cpp import Llama

llm = Llama(model_path="/models/model.gguf", n_ctx=512)

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    output = llm(prompt, max_tokens=10)
    return jsonify({"response": output["choices"][0]["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=11434)
