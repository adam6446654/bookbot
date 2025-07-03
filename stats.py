def number_of_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    print(f"{word_count} words found in the document")

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count