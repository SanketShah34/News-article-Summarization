from implementation.BART import summarize_text_bart
from implementation.PEGASUS import summarize_text_pegasus
from models.ROUGE import eval_rouge
from preprocessing.data_cleaning import clean_data
from preprocessing.data_extraction import extract_from_url, extract_from_textbox, extract_from_browse


def input_url(input_control):
    input: str = extract_from_url(input_control)
    result = clean_data(input)
    output = summarize_text_bart(result)
    eval_rouge(input, str(output))
    return output

def input_textbox(input_control):
    input: str = extract_from_textbox(input_control)
    result = clean_data(input)
    output = "BART:\n"
    bart_output = summarize_text_bart(result)
    pegasus_output = summarize_text_pegasus(result)
    output += bart_output + "\n"
    output += "PEGASUS:\n"
    output += pegasus_output
    eval_rouge(input, str(bart_output), str(pegasus_output))
    return output

def input_browse(input_control):
    input: str = extract_from_browse(input_control)
    result = clean_data(input)
    output = summarize_text_bart(result)
    eval_rouge(input, str(output))
    return output