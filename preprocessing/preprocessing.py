import re
from num2words import num2words


def text_processing(text):

    # lowecase
    text = str(text)
    text = text.lower()

    # change number to word ex: 42 --> forty two
    number_detected = re.findall('[0-9.]+', str(text))
    number_detected = list(set(number_detected))
    number_detected.sort(reverse = True)
    
    try:
        for number in number_detected:
            word = num2words(number)

            text = text.replace(f"{number}", f"{number} ")
            # if f"{number}" in text:
            text = text.replace(f"{number}", word)
                
    except Exception as e:
        print(f"[Error] {e} : {text}")
        return ""

    # remove punctuations with space
    replace_punctuation = re.compile('[%s]' % re.escape('''!()—-[]{}…;:'“”’",<>./?@#$%^&*_~'''))
    text = replace_punctuation.sub(' ', text)

    # strip words
    text = " ".join(text.split())

    # remove all non alphabet
    regex_p = re.compile("[^a-z' ]")
    text = regex_p.sub('', text)

    return text
