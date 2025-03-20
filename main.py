import sys
from stats import (
    get_num_words,
    get_chars_dict,
    sort_chars_dict
)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path = sys.argv[1]

    book_path = path
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = sort_chars_dict(get_chars_dict(text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Print each character and it's count on a separate line
    for char, count in char_count:
        print(f"{char}: {count}")
    print("============= END ===============")


main()
