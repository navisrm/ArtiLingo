from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from language_codes import language_codes

class LanguageTranslationHelpers:
    def __init__(self) -> None:
        self.model = None
        self.tokenizer = None
        self.language_codes = None

    def pretrained_model(self):
        self.model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
        return self.model

    def pretrained_tokenizer(self):
        self.tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
        return self.tokenizer




    def language_translation(self,model2, tokenizer2, text, target_language_code):
        print("text is: " + text)
        print("target_language code is: " + target_language_code)
        try:
            translator = pipeline('translation', model=model2, tokenizer=tokenizer2, src_lang="eng_Latn", tgt_lang=language_codes[target_language_code], max_length = 400)
        except Exception as e:
            print("Eception is: " + str(e))
        print("translator is done")
        translated = translator(str(text))

        print("transated out put is: " + str(translated))

        return translated


    
