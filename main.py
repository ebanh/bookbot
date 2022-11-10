def count_words(contents):
    words = contents.split()
    return len(words)

def num_characters(contents):
    text = {}
    for letter in contents:
        let = letter.lower()
        if let not in text:
            text[let] = 1
        else:
            text[let] += 1
    return text


with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    # pull information from text file
    word_count = count_words(file_contents)
    char_list = list(num_characters(file_contents).items())

    # extract only alpha characters and sort the list
    char_only = []
    for char in char_list:
        if char[0].isalpha():
            char_only.append(char)
    char_only.sort()

# Print report
    print("--- Being report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    for char in char_only:
        print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")
