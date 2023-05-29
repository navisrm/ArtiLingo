from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

def language_translation(text, target_language_code):

    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
    tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    print("text is: " + text)
    print("target_language code is: " + target_language_code)
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="eng_Latn", tgt_lang="tel_Telu", max_length = 400)

    translated = translator(str(text))

    return translated

sample_text="Rainfall to hit northern India."
print(language_translation(sample_text, "dummy"))


