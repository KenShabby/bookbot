import sys
from stats import word_count, char_count, sort_dictionaries

def get_book_text(path):
    with open(path) as f:
        book = f.read()
    return book 


def main():

    # Handle input file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    infile = sys.argv[1]
    text = get_book_text(infile)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {infile}...")
    print("----------- Word Count ----------")

    num_words = word_count(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    num_chars = char_count(text)
    sorted_list = sort_dictionaries(num_chars)

    for item in sorted_list:
        print(f"{item.get('char')}: {item.get('count')}")

main()
