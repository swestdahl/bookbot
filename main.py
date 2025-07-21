import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]

from stats import count_words
from stats import count_characters
from stats import sort_char

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def main():
    text = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")
    sorted_chars = sort_char(text)
    for char_info in sorted_chars:
        print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ================")

if __name__ == "__main__":
    main()

