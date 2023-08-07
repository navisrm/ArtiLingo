Certainly! Below is a README.md file for the `ArticleSummarization` project:

---

# ArtiLingo

## Overview

The `ArticleSummarization` project provides a Flask web application that allows users to input a URL link to an article, specify a word count, and select a target language. The application then summarizes the article based on the provided word count and translates the summary to the selected target language.

## Prerequisites

- Python 3.x
- Flask
- OpenAI
- Transformers

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
```

2. Navigate to the project directory:

```bash
cd ArticleSummarization
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Set up the OpenAI API key:

Ensure you have your OpenAI API key. You can set it as an environment variable or directly in the `flask_app.py` file.

2. Run the Flask application:

```bash
python flask_app.py
```

3. Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

4. Provide the required inputs (word count, URL link, target language) and click "Submit" to get the summarized and translated content.

## Features

- **ArtiLingo**: Uses OpenAI's `text-davinci-003` model to generate a concise summary of an article based on the provided word count.
  
- **Language Translation**: Uses the pretrained model `facebook/nllb-200-distilled-600M` from the Transformers library to translate the summary to a variety of supported languages.

- **Web Interface**: Provides an easy-to-use web interface for inputting the article URL, desired word count, and target language.

## Files and Directories

- `flask_app.py`: The main Flask application file.
  
- `helpers`: Contains helper scripts for OpenAI and language translation functionalities.
  
  - `openai_helpers.py`: Functions related to the OpenAI API.
  
  - `translation_helpers.py`: Functions related to translating text using the Transformers library.

- `templates`: Contains the HTML template for the web interface.

- `language_codes.py`: Contains mappings between language names and their respective codes.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

You can now save this content to a `README.md` file in the root directory of your project. Adjustments can be made based on specific project details or any additional sections you'd like to include.