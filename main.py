from stats import number_of_words
from stats import count_characters
from stats import sorted_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    result = get_book_text("books/frankenstein.txt")
    sorted_dict = sorted_dictionary(count_characters(result))
    count_characters(result)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(result)} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()