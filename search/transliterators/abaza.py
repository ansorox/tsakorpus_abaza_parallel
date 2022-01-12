import re

def abaza_input_normal(field,text):
    """
    Prepare a string from one of the query fields for subsequent
    processing: replace common shortcuts with valid Abaza characters."""
    
    if field not in ('wf', 'lex', 'lex2', 'trans_ru', 'trans_ru2'):
        return text

    text = re.sub('(?<=[а-яА-ЯёЁ])[I1i]', 'Ӏ', text)
    text = re.sub('[I1i](?=[а-яА-ЯёЁ])', 'Ӏ', text)
    return text

def abaza_input_strict(field,text):
    return text
