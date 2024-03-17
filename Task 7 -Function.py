# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lMIQv0JBVrwlkzAUJYPXUdA1Mng1FAKI

1.) Write a Python program using Function to which will do the following:-
a.) The function will create a text file with the current timestamp.

b.) The file content should have the content of the current timestamp.
"""

import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a file with the current timestamp as the file name
    file_name = current_timestamp.replace(":", "-") + ".txt"

    # Write the current timestamp to the file
    with open(file_name, "w") as file:
        file.write(current_timestamp)

    print("File '{}' created with current timestamp.".format(file_name))

# Call the function to create the timestamp file
create_timestamp_file()

"""2. Write another Python function to read from a text file. The function will take the name of
the text file and display the content of the file into the console.
"""

def read_text_file(file_name):
    try:
        # Open the file in read mode
        with open(file_name, "r") as file:
            # Read the content of the file
            file_content = file.read()
            # Display the content in the console
            print("Content of the file '{}':\n{}".format(file_name, file_content))
    except FileNotFoundError:
        print("Error: File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", e)

# Example usage
file_name = input("Enter the name of the text file: ")
read_text_file(file_name)