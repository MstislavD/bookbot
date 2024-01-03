def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")

    count_by_letter = count_letters(file_contents)
    letter_counts = get_values(count_by_letter)
    letter_counts.sort()
    letter_by_count = reverse_dictionary(count_by_letter)

    for count in letter_counts[-1::-1]:
        for letter in letter_by_count[count]:
            print(f"The '{letter}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(str):
    words = str.split()
    return len(words)

def count_letters(str):
    count_by_letter = {}
    for char in str.lower():
        if not char.isalpha():
            pass
        elif char in count_by_letter:
            count_by_letter[char] += 1
        else:
            count_by_letter[char] = 1
    return count_by_letter

def reverse_dictionary(dictionary):
    reversed_dictionary = {}
    for key in dictionary:
        value = dictionary[key]
        if value in reversed_dictionary:
            reversed_dictionary[value].append(key)
        else:
            reversed_dictionary[value] = {key}
    return reversed_dictionary

def get_values(dictionary):
    values = []
    for key in dictionary:
        values.append(dictionary[key])
    return values


main()
