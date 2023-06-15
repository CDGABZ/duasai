from flask import Flask, request, render_template
import openai

openai.api_key = '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'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    response = ""
    if request.method == 'POST':
        message = request.form.get('message')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=60
        )
        response = response['choices'][0]['text'].strip()
    return render_template('chat.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
