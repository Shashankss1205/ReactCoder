from flask import Flask, request, render_template, jsonify
import openai
import re
import requests
import json

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        print(f"Write code to make React web app with {input}")
        messages.append({"role": "user", "content": f"Write a single file code to make React web app with all information given as {input} and make sure that code works"})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(reply)
        pattern1 = r'```jsx(?:\w+)?\n([\s\S]*?)\n```'
        pattern2 = r'```javascript(?:\w+)?\n([\s\S]*?)\n```'
        code_blocks = re.findall(pattern1, reply) or re.findall(pattern2, reply)
        messages.append({"role": "assistant", "content": reply})
        return code_blocks[0]

#Routes for Website
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/editor")
def editor():
    return render_template('editor.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    input = request.form["msg"]
    responses = chatbot(input)
    print(responses)
    return responses

if __name__ == '__main__':
    app.run(debug=True,port = 5002)