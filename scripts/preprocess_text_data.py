import re
import string
import pandas as pd

# Function to remove emojis
def remove_emojis(text):
    emoji_pattern = re.compile(
        "[\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "\U0001F1E6-\U0001F1FF]"  # Flags
        "+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Function to clean text (removing emojis and special characters)
def clean_text(text):
    text = remove_emojis(text)

    # Remove English letters
    text = re.sub(r'[a-zA-Z]+', '', text)

    # Remove punctuation (both English and Amharic punctuation)
    amharic_punctuation = '።፡፣፤፥፦'
    all_punctuation = string.punctuation + amharic_punctuation
    
    # Remove all punctuation using translate
    text = text.translate(str.maketrans('', '', all_punctuation))

    return text

# Function to normalize Amharic text (basic whitespace tokenization)
def normalize_amharic_text(text):
    # Convert to lowercase (though Amharic is case-insensitive)
    text = text.lower()

    # Split into tokens based on whitespace
    tokens = text.split()

    # Join the tokens back into a single string (if needed)
    normalized_text = ' '.join(tokens)

    return normalized_text

# Combined preprocessing function
def preprocess_text(text):
    if pd.isnull(text):
        return ""

    # Clean text (remove emojis, numbers, special characters)
    cleaned_text = clean_text(text)

    # Normalize the cleaned text
    normalized_text = normalize_amharic_text(cleaned_text)

    return normalized_text
