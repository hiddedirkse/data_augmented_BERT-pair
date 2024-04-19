from transformers import MarianMTModel, MarianTokenizer


def translate_text(text, model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize the text
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))

    # Decode the tokenized text
    translated_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

    return translated_text[0]


# Original sentence
english_text = "This is a test sentence."

# Translate from English to French
model_name_en_to_fr = "Helsinki-NLP/opus-mt-en-fr"
french_translation = translate_text(english_text, model_name_en_to_fr)
print(f"Translated to French: {french_translation}")

# Translate back from French to English
model_name_fr_to_en = "Helsinki-NLP/opus-mt-fr-en"
back_to_english_translation = translate_text(french_translation, model_name_fr_to_en)
print(f"Translated back to English: {back_to_english_translation}")