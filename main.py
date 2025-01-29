def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f'{num_words} words found in the document')
    print(char_count)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lowered_text = text.lower()
    char_dict = {}
    for l in lowered_text:
        if l in char_dict:
            char_dict[l] += 1
        else:
            char_dict[l] = 1
    return char_dict
main()