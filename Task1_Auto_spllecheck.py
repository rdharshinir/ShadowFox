from textblob import TextBlob


def correct_sentence_spelling(sentence):
    
    sentence = TextBlob(sentence)
    
    result = sentence.correct()
    
    print(result)
correct_sentence_spelling("A sentencee to checkk!")


from spellchecker import SpellChecker

# Initialize the spell checker
# It uses a default word list, but you can add your own dictionary if needed.
spell = SpellChecker()

def autocorrect_sentence(sentence_input):
    """
    Identifies misspelled words in a sentence and provides a corrected version.
    """
    # 1. Split the input sentence into individual words for processing
    words = sentence_input.split()
    corrected_words = []

    # 2. Iterate through each word to check and correct
    for word in words:
        # Pyspellchecker automatically finds unknown words
        if word in spell.unknown(words):
            # Get the most likely correction suggestion
            # The 'correction' method returns the best guess
            corrected_word = spell.correction(word)
            
            # If a suggestion is found, use it; otherwise, keep the original word
            if corrected_word:
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        else:
            # If the word is known/spelled correctly, keep it as is
            corrected_words.append(word)
    
    # 3. Reassemble the corrected words back into a sentence
    return " ".join(corrected_words)

# --- Example Usage ---

# Example 1: Standard typos
input_text_1 = "Ths is a sentnce with some comon mispelled words."
corrected_text_1 = autocorrect_sentence(input_text_1)

print(f"Original 1: {input_text_1}")
print(f"Corrected 1: {corrected_text_1}\n")

# Example 2: More deliberate misspellings
input_text_2 = "I luv programing in Pythn it is fun."
corrected_text_2 = autocorrect_sentence(input_text_2)

print(f"Original 2: {input_text_2}")
print(f"Corrected 2: {corrected_text_2}")
