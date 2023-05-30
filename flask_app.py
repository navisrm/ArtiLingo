from flask import Flask, redirect, url_for, render_template, request
import openai
from helpers import openai_helpers, translation_helpers

# Retrieve values from environment variables
openai.api_key = "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"

app = Flask(__name__)
app.config['TIMEOUT'] = 120

print("Does the control go through this everytime?")

@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = None
    
    if request.method == 'POST':
        word_count_input = request.form.get('word_count_input', '')
        url_link_input = request.form.get('url_link_input', '')
        language_selection = request.form.get('language_select','')
        
        # Process inputs and generate output
        output_text = process_inputs( word_count_input, url_link_input, language_selection)
    
    return render_template('index.html', output_text=output_text)

@app.route("/home/")
def home():
    return "Hello this is HomePage. <h1>HOME PAGE<h1>"

def process_inputs(word_count, url_link, language_selected):
    try:
        response = openai_helpers.article_summary_prompt_text(word_count, url_link)

        # Extract the text from the JSON object
        text = response["choices"][0]["text"]
        translated_output = translation_helpers.language_translation(text,language_selected)
        return translated_output
    except Exception as e:
        print(e)

    

if __name__ == '__main__':
    app.run(debug=True)
