import sys
from stats import get_num_words,new_func,sorting,sortnas

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = str(sys.argv[1])
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    pzar = new_func(text)
    newest = sorting(pzar)
   
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in newest:
        print (f"{i['char']}: {i['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()