import spacy
nlp = spacy.load('./model')
from preprocessing.preprocessing import text_processing



def get_salary(text):
    preprocess_text = text_processing(text)
    doc = nlp(preprocess_text)
    
    salary_str = ''
    for token in doc:
        if token.ent_type_ == 'amount':
            salary_str+= ' '+token.text
    return salary_str.strip()



# result = get_salary('my salary is 44 k a month')
# print(result)