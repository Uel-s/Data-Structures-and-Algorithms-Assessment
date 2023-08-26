def word_frequency(sentence):
    import re  # Import the regular expression module
    # Use regex to find all words and convert them to lowercase
    words = re.findall(r'\w+', sentence.lower())
    # Create a dictionary with words as keys and their frequency as values
    word_freq = {word: words.count(word) for word in set(words)}
    return word_freq  # Return the word frequency dictionary

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

