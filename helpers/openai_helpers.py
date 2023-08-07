import openai
import sys

def article_summary_prompt_text(word_count, url_link):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="TLDR; Summarize the article in " + str(word_count) + " words. Link: " + str(url_link),
    temperature=0.7,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    return response

    