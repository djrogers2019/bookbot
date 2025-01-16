def main():
    book_path = "github.com/DJROGERS2019/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_characters(text)
    print(f"{num_words} words found in the document")
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    characters = {}
    all_lowercase = text.lower()
    for char in all_lowercase:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    new_list = list(characters.items())
    sorted_list = sorted(new_list)

    for entry in sorted_list:
        print(f"The '{entry[0]} character was found {entry[1]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()