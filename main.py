from stats import number_of_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    result = get_book_text("books/frankenstein.txt")
    number_of_words(result)
    print(count_characters(result))

if __name__ == "__main__":
    main()