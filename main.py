

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = get_word_count(file_contents)
        char_count = get_char_count(file_contents)
        # print(word_count)
        print(char_count)
        print(
            """--- Begin report of books/frankenstein.txt ---
77986 words found in the document"""
        )
        char_report(char_count)
        print('--- End report ---')
        

def get_word_count(file_contents):
    words = file_contents.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def sort_keys(dict):
    return dict["char"]

def get_char_count(file_contents):
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    char_dict_list = [{'char':key,'num':value} for key, value in char_count.items()]
    char_dict_list.sort(reverse=False, key=sort_keys)
    return char_dict_list

def char_report(char_count):
    for entry in char_count:
        char = entry['char']
        num = entry['num']
        print(f"The '{char}' character was found {num} times")
    

if __name__ == '__main__':
    main()