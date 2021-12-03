from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import constants

def generate_model():
    print("Model generation starting.....")
    training_dataset = constants.PRETRAINED_MODEL_PEGASUS
    model = PegasusForConditionalGeneration.from_pretrained(training_dataset)
    tokenize = PegasusTokenizer.from_pretrained(training_dataset)
    print("Model generated...")
    return model, tokenize

def generate_summary(input: str, model, tokenize, minimum: int, maximum: int):
    # Referred from:
    print("Summarization starting...")
    input = [input]
    result = tokenize.prepare_seq2seq_batch(input, truncation=True, padding='longest', return_tensors="pt")
    print(result)
    summerized_text = model.generate(result, num_beams=6, num_return_sequences=1, no_repeat_ngram_size = 2, length_penalty = 1, min_length = minimum, max_length = maximum, early_stopping = True)
    print("Summarization ended...")
    return [tokenize.batch_decode(summerized_text, skip_special_tokens=True, clean_up_tokenization_spaces=False)]
