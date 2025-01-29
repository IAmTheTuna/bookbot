def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    for char_dict in char_count:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")
    print("--- End of Report ---")

    
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lowered_text = text.lower()
    char_dict = {}
    char_list = []
    for l in lowered_text:
        if l.isalpha():
            if l in char_dict:
                char_dict[l] += 1
            else:
                char_dict[l] = 1
    for char, count in char_dict.items():
        char_list.append({"char": char, "num":count})
    char_list.sort(reverse = True, key = sort_on)
    return char_list


def sort_on(dict):
    return dict["num"]

main()