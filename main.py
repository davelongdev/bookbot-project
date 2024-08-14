def main():
    '''This is the main entry point to the application.
    It's called at the bottom of this file.'''

    # Save file path of text file to variable
    text_file_path = 'text_files/frankenstein.txt'

    # Calls get_file_text function to obtain the text from the file
    text = get_file_text(text_file_path)

    # Count the words in the text file
    word_number = count_words(text)

    # Create a dict where k is the char and v is the number of times it appears
    char_dict = count_chars(text)

    # Create dicts to count the alphabet and non-alphabet characters
    alpha_char_dict, non_alpha_char_dict = split_char_types(char_dict)

    # sort all the characters
    sorted_chars = dict_to_sorted_list(char_dict)

    # Sort the alphanumeric characters
    sorted_alpha_chars = dict_to_sorted_list(alpha_char_dict)

    # Sort the non-alphanumeric characters
    sorted_non_alpha_chars = dict_to_sorted_list(non_alpha_char_dict)

    # Print a report of the analysis to the console
    print_report(
        word_number,
        sorted_chars,
        sorted_alpha_chars,
        sorted_non_alpha_chars
    )


def get_file_text(path):
    '''Opens a text file and returns the text as a string'''
    with open(path) as f:
        return f.read()


def count_words(text):
    '''counts the words in a string and returns a number'''

    # set counter
    counter = 0

    # return list of words
    words = text.split()

    # loop over words and incriment counter
    for word in words:
        counter += 1

    # return number of words
    return counter


def count_chars(text):
    '''counts the characters in a string and returns a dictionary of characters
    and how many times they appear'''

    string_lower = text.lower()
    dict = {}
    for ii in string_lower:
        if ii not in dict:
            dict[ii] = 0
        if ii in dict:
            dict[ii] += 1
    return dict


def split_char_types(char_dict):
    '''Take in the char_dict dictionary with all chars in the original txt
    file and retun a dictionary of the 26 alphabet characters and a dictionary
    of all the non-alphabet characters'''

    alpha_char_dict = {}
    non_alpha_char_dict = {}
    for k, v in char_dict.items():
        if k.isalpha():
            alpha_char_dict[k] = v
        else:
            non_alpha_char_dict[k] = v
    return alpha_char_dict, non_alpha_char_dict


def sort_on(dict):
    '''A function to pass to the python's sort function
    to control the sorting'''

    return dict['num']


def dict_to_sorted_list(dict):
    '''Sort characters in a dict and return a sorted list of dicts'''

    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def print_report(
        word_number,
        sorted_chars,
        sorted_alpha_chars,
        sorted_non_alpha_chars
):
    '''Print a report analyzing the text file'''

    # print opening info
    print('')
    print('-- book analysis --')
    print(f'{word_number} words found in the book')

    # print info for all chars sorted
    print('')
    print('-- All Characters Sorted --')
    print('')
    for item in sorted_chars:
        if item["char"] == '\n':
            print(f"The '\\n' character was found {item} times")
        else:
            print(f"The '{item['char']}' character was found {item} times")

    print('')
    print('-- Alphabet Characters Sorted --')
    print('')

    # print info for alpha chars sorted
    for item in sorted_alpha_chars:
        print(f"The '{item['char']}' character was found {item} times")

    # print info for non-alpha chars sorted
    print('')
    print('-- Non-Alphabet Characters Sorted --')
    print('')
    for item in sorted_non_alpha_chars:
        if item["char"] == '\n':
            print(f"The '\\n' character was found {item} times")
        else:
            print(f"The '{item['char']}' character was found {item} times")

    # print closing info
    print('')
    print('--- end report ---')
    print('')


# call the main function
main()
