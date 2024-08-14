def main():
    '''This is the main entry point to the application.
    It's called at the bottom of this file.'''

    # Save file path of text file to variable
    text_file_path = 'text_files/frankenstein.txt'

    # Calls get_file_text function to obtain the text from the file
    text = get_file_text(text_file_path)

    # Count the words in the text file
    word_number = count_words(text)

    # Count all the characters in the file
    char_dict = count_chars(text)

    # Count the alphanumeric and non-alphanumeric characters seperately
    alpha_char_dict, non_alpha_char_dict = split_char_types(char_dict)

    # Sort the alphanumeric characters
    alpha_chars_sorted = 'insert func'

    # Sort the non-alphanumeric characters
    non_alpha_chars_sorted = 'insert func'

    # Print a report of the analysis to the console
    print_report(word_number, char_dict)


def split_char_types(char_dict):
    '''Take in the char_dict dictionary with all chars in the original txt
    file and retuns a dictionary of the 26 alphabet characters'''

    alpha_char_dict = {}
    non_alpha_char_dict = {}
    for k, v in char_dict.items():
        if k.isalpha():
            alpha_char_dict[k] = v
        else:
            non_alpha_char_dict[k] = v
    return alpha_char_dict, non_alpha_char_dict


def print_report(word_number, char_dict):
    '''Print a report analyzing the text file'''

    print('-- book analysis --')
    print(f'{word_number} words found in the book')

    list_of_dicts = []
    for k,v in char_dict.items():
        # list_of_dicts.append({k[0]: v})
        list_of_dicts.append({'char':k, 'num':v})

    list_of_alpha_char_dicts = []
    for k,v in alpha_char_dict.items():
        # list_of_dicts.append({k[0]: v})
        list_of_alpha_char_dicts.append({'char':k, 'num':v})

    def sort_on(dict):
        return dict['num']

    list_of_alpha_char_dicts.sort(reverse=True, key=sort_on)

    sorted_alpha = {}

    for ii in list_of_alpha_char_dicts:
        # for k,v in dict.items():
        count = 0
        for key in ii:
            if count == 0:
                new_key = ii[key]
                count += 1
            else:
                new_val = ii[key]
        sorted_alpha[new_key] = new_val
    
    for ii in sorted_alpha:
        print(f'the {ii} char was found {sorted_alpha[ii]} times.')

    print('--- end report ---')


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


# call the main function
main()
