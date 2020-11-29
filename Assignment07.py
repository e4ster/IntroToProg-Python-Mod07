# ------------------------------------------------- #
# Title: Assignment07.py
# Version: 3.9
# Description: Pickling and error handling demo.
# ChangeLog: (Who, When, What)
#   e4ster, 11.28.2020, Created Script
# ------------------------------------------------- #

import pickle


# Data -------------------------------------------- #
strFileName = 'AppData.pickle'


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ Function that writes the list data to a binary file.

    :param file_name: String of the binary file name.
    :param list_of_data: List of lists.
    :return: Nothing
    """

    file = open(file_name, "wb")
    pickle.dump(list_of_data, file)
    file.close()


def read_data_from_file(file_name):
    """ Function that reads the binary data.

    :param file_name: String of the binary file name.
    :return: List of data from the binary.
    """

    try:
        initial_list = [["ID", "Name"]]
        binary_file = open(file_name, "xb")
        pickle.dump(initial_list, binary_file)
        binary_file.close()
    except FileExistsError:
        pass

    try:
        file = open(file_name, "rb")
        list_of_data = pickle.load(file)
        file.close()
        return list_of_data
    except Exception as e:
        print("There was a random error!")
        print("Python's explanation: ")
        print(e, e.__doc__, type(e), sep='\n')


class NameInputError(Exception):
    """ Handles non-letter inputs. """
    def __str__(self):
        return "The name can only be letters (no spaces)."


# Presentation ------------------------------------ #
def get_input():
    """ Function that gets the user input.

    :return: A list with two elements.
    """

    while True:
        try:
            int_id = int(input("Enter an Id: ").strip())
            break
        except (ValueError, TypeError):
            print("The ID can only be integers. Try again!")
    while True:
        str_name = str(input("Enter a First Name: ").strip().lower())
        if str_name.isalpha() is True:
            break
        else:
            raise NameInputError()
    lst_row = [int_id, str_name]
    return lst_row


def print_data(file_name):
    """ Function that prints the list to the user.

    :param file_name: String of the binary file name.
    :return: Nothing
    """

    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    for element in list_of_data:
        print(element[0], ",", element[1])
    file.close()


# Main Body --------------------------------------- #

# Step 1: Read data from file and store in a list.
lstCustomer = read_data_from_file(strFileName)

# Step 2: Get user input and add it to the list.
lstCustomer.append(get_input())

# Step 3: Save the list data to the binary file.
save_data_to_file(strFileName, lstCustomer)

# Step 4: Gather new data in file, print out to user.
print_data(strFileName)
