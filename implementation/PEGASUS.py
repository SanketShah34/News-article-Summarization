from models.PEGASUS import generate_model, generate_summary
from summerizer_config import get_config_values

def summarize_text_pegasus(input):
    model, tokenize = generate_model()
    min, max = get_config_values(input)
    return generate_summary(input, model, tokenize, min, max)