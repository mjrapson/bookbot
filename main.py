from stats import count_words
from stats import get_character_counts
from stats import get_sorted_count

import sys

def get_book_text(filepath):
    text = ""
    with open(filepath) as file:
        text = file.read()

    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_counts = get_character_counts(book_text)
    sorted_count = get_sorted_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
main()