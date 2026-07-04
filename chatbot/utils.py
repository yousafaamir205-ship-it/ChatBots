import string

def clean_text(text):
    clean = ""

    for value in text:
        if value not in string.punctuation:
            clean = clean + value

    return clean.lower().strip()