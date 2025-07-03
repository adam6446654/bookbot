def number_of_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    return word_count

def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sorted_dictionary(d):
    char_list = []
    for char,count in d.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    char_list.sort(reverse=True,key=sort_on)
    return char_list