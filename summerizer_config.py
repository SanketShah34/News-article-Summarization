def get_config_values(input):
    text = str(input)
    total_length = len(text.split())
    minimum_length = int(total_length / 6)
    maximum_length = minimum_length + 200
    return minimum_length, maximum_length