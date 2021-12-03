from transformers import BartTokenizer, BartForConditionalGeneration
import constants

def generate_model():
    print("Model generation starting.....")
    training_dataset = constants.PRETRAINED_MODEL_BART
    training_dataset = training_dataset.replace(".", "-")
    print(training_dataset)
    model = BartForConditionalGeneration.from_pretrained(training_dataset)
    tokenize = BartTokenizer.from_pretrained(training_dataset)
    print("Model generated...")
    return model, tokenize

def generate_summary(input: str, model, tokenize, minimum: int, maximum: int):
    # Referred from:
    print("Summarization starting...")
    input = [input]
    result = tokenize.batch_encode_plus(input, max_length=1024, return_tensors='pt')
    summerized_text = model.generate(result['input_ids'], attention_mask=result['attention_mask'], num_beams=4, min_length=minimum, max_length=maximum)
    print("Summarization ended...")
    return [tokenize.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summerized_text][0]

