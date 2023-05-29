import os
import openai
from helpers import openai_helpers

# Retrieve values from environment variables
openai.api_key = "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"

try:
    response = openai_helpers.prompt_text_example(60, "https://www.indiatoday.in/world/story/pm-modi-australia-sydney-australian-pm-albanese-joint-statement-indian-community-2383428-2023-05-24")
except Exception as e:
    print(e)

# Extract the text from the JSON object
text = response["choices"][0]["text"]

# # Print the extracted text
print(text)