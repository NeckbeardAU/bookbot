import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    wc = get_word_count(text)
    char_cnt = char_count(text)
    bookreport(wc, char_cnt)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    print(counter)

def char_count(words):
    alphanumeric_set = set(string.ascii_lowercase)
    char_dict = {}
    for char in alphanumeric_set:
        counter = 0
        for chara in words:
            if chara == char:
                counter += 1
                char_dict[char] = counter
    return char_dict
            
def book_report(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document.")
    for k, v in char_dict:
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

main()