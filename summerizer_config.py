def get_config_values(input):
    text = str(input)
    total_length = len(text.split())
    minimum_length = int(total_length / 6)
    maximum_length = minimum_length + 200
    print("Config returned...." + str(minimum_length) + " " + str(maximum_length))
    return minimum_length, maximum_length