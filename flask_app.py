from flask import Flask, redirect, url_for, render_template, request
import openai
from helpers import openai_helpers, translation_helpers
from helpers.translation_helpers import LanguageTranslationHelpers
from language_codes import language_selectors

# Retrieve values from environment variables
openai.api_key = "OPENAI_API_KEY"

app = Flask(__name__)
app.config['TIMEOUT'] = 120

languagetranslator = LanguageTranslationHelpers()
model = languagetranslator.pretrained_model()
tokenizer = languagetranslator.pretrained_tokenizer()


@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = None
    
    if request.method == 'POST':
        word_count_input = request.form.get('word_count_input', '')
        url_link_input = request.form.get('url_link_input', '')
        language_selection = request.form.get('language_select','')
        
        # Process inputs and generate output
        output_text = process_inputs( model, tokenizer ,word_count_input, url_link_input, language_selection)
    
    return render_template('index.html', output_text=output_text, languages=language_selectors)

@app.route("/home/")
def home():
    return "Hello this is HomePage. <h1>HOME PAGE<h1>"

def process_inputs(model1, token1, word_count, url_link, language_selected):
    try:
        response = openai_helpers.article_summary_prompt_text(word_count, url_link)

        # Extract the text from the JSON object
        text = response["choices"][0]["text"]
        translated_output = languagetranslator.language_translation(model1, token1, text,language_selected)
        translated_text = translated_output[0]['translation_text']
        return translated_text
    except Exception as e:
        print(e)

    

if __name__ == '__main__':
    app.run(debug=True)
