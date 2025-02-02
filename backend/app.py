from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your-api-key-here"

@app.route('/generate', methods=['POST'])
def generate_resume():
    data = request.json
    prompt = f"Створи професійне резюме для {data['name']} на позицію {data['position']}"
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )

    return jsonify({"resume": response["choices"][0]["text"].strip()})

if __name__ == '__main__':
    app.run(debug=True)
