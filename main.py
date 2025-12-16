import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    content = get_book_text(path)
    wc = get_word_count(content)
    char_list = sort_char_count(get_char_count(content))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")

    for item in char_list:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()

