
def main():
    text_loc = 'books/frankenstein.txt'
    with open(text_loc, 'r') as f:
        book = f.read()

    words = word_count(book)
    print(words)

    char_dict = char_quantity(book)
    print(char_dict)

    report = f'''
--- Begin report of {text_loc} ---
{words} words found in the document
        
'''

    for char, count in char_dict.items():
        report = report + f"\nThe '{char}' character was found {count} times"
    report = report + '\n--- End report ---'

    print(report)


def word_count(text):
    words = text.split()
    return len(words)

def char_quantity(text):
    text_lower = text.lower()
    char_dict = {}
    for char in text_lower:
        if not char.isalpha():
            continue
        elif char in char_dict:
           char_dict[char] += 1
        else:
            char_dict[char] = 1
    char_dict = {k: v for k, v in sorted(char_dict.items(), key=lambda item: item[1], reverse=True)}
    return char_dict


main()