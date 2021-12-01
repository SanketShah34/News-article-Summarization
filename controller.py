from implementation.BART import summarize_text_bart
from preprocessing.data_cleaning import clean_data
from preprocessing.data_extraction import extract_from_url, extract_from_textbox, extract_from_browse


def input_url(input_control):
    input: str = extract_from_url(input_control)
    result = clean_data(input)
    return result

def input_textbox(input_control):
    input: str = extract_from_textbox(input_control)
    result = clean_data(input)
    print(str(result))
    return summarize_text_bart(result)

def input_browse(input_control):
    input: str = extract_from_browse(input_control)
    result = clean_data(input)
    return result