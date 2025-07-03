def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def number_of_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1
    print(f"{word_count} words found in the document")

def main():
    result = get_book_text("books/frankenstein.txt")
    number_of_words(result)

if __name__ == "__main__":
    main()