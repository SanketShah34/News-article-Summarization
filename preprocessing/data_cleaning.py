import nltk.corpus
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# It involves cleaning of input string. It undergoes the following steps:
# Removing all non-ascii characters.
# Convert everything to lower case.
# Removing all non-english words.
# Remove all special characters.
# Remove excessive spaces.
# Tokenize words
# Remove stop words.

def remove_non_ascii_characters(input: str) -> str:
    # Example:
    # Input: "àa string withé fuünny charactersß."
    # Output: a string with funny characters.

    # Referred from: https://www.kite.com/python/answers/how-to-remove-non-ascii-characters-in-python

    encoded_string = input.encode("ascii", "ignore")
    return encoded_string.decode()

def convert_to_lower_case(input: str) -> str:
    # Example:
    # Input: "NLP IS FUN"
    # Output: "nlp is fun"

    return input.lower()

def remove_special_characters(input: str) -> str:
    result = re.sub('\W+',' ', input)
    return result

def remove_non_english_characters(input: str) -> str:
    # Fetch the list of all english words
    words = set(nltk.corpus.words.words())

    return " ".join(w for w in nltk.wordpunct_tokenize(input) if w.lower() in words or not w.isalpha())

def remove_excessive_space(input: str) -> str:
    return " ".join(input.split())

def tokenize_words(input: str) -> []:
    return word_tokenize(input)

def remove_stop_words(word_tokens) -> []:
    stop_words = set(stopwords.words('english'))
    return [w for w in word_tokens if not w.lower() in stop_words]

def clean_data(input: str) -> str:
    result = remove_non_ascii_characters(input)
    result = convert_to_lower_case(result)
    result = remove_special_characters(result)
    # result = remove_non_english_characters(result)
    result = remove_excessive_space(result)
    result = tokenize_words(result)
    # result = remove_stop_words(result)
    final_resultl = " ".join(word for word in result)
    return final_resultl

if __name__ == "__main__":
    input = "àA String withé      fuünny's asdefa    # charactersß."
    print(clean_data(input))


