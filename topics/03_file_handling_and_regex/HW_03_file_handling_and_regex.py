# 03_file_handling_and_regex -------------------------------------------------------------------------------------------
# 1 [TI] Explain the difference between read(), readline(), and readlines(). In what situations would you use each?
# read() is best for smaller files or when you need to manipulate the whole text at once.
# readline() is optimal for reading a file line by line, particularly with large files.
# readlines() suits scenarios where you need the entire file read into a list for easy manipulation of line-based data within a list context, but be mindful of memory usage with larger files.
# 2 [TI] How does the with statement help in file handling, and why is it preferred over manually opening and closing files?
# with statement provides a much more readable, cleaner,
# and error-free way to handle files in Python,
# especially when compared to the traditional approach of manually opening
# and closing files. It makes your file handling safer and more consistent.
import os
file_dir = os.path.dirname(os.path.realpath('C:/Users/Olena_Smolianchuk/Downloads/'))
print(file_dir)
file_name = os.path.join(file_dir, 'Downloads/config.ini')
# 3 Write a script that reads a file test_data.txt and prints each line.
with open('test_data.txt', "r") as file:
    for line in file:
        print(line)
# 4 Modify the script from the previous exercise to append a new line to the file.
with open('test_data.txt', "a") as file:
    file.write ("This text should be added as new line to file")
# 5 Write a script that reads test_data.txt and counts the number of lines and words in the file. Print both counts at the end.
file_path = 'test_data.txt'
line_count = 0
word_count = 0
with open(file_path, 'r') as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
print(f"Total lines: {line_count}")
print(f"Total words: {word_count}")
# 6 Write a script that replaces a specific word (e.g., "error") in a file logs.txt with the word "fixed" and saves the changes.
with open('logs.txt', 'r') as file:
    data = file.readlines()

with open('logs.txt', 'w') as file:
    for line in data:
        new_line = line.replace('error', 'fixed')
        file.write(new_line)
# 7 Write a script that tries to read a file data.txt, handles the exception if the file does not exist, and prompts the user to create the file if it's missing.
def read_file():
    try:
        with open('data.txt', 'r') as file:
            data = file.read()
            print("File content:")
            print(data)
    except FileNotFoundError:
        print("The file 'data.txt' does not exist.")
        create_file = input("Would you like to create the file? (yes/no): ").strip().lower()
        if create_file == 'yes':
            with open('data.txt', 'w') as file:
                file.write("This is a new file.")
            print("'data.txt' has been created.")
        else:
            print("No file was created.")

# 8 Merging multiple files: Write a script that reads multiple files (file1.txt, file2.txt, file3.txt), merges their content, and writes the result to a new file called merged.txt.
file_paths = ['file1.txt', 'file2.txt','file3.txt']

with open('merged.txt', 'w', encoding="utf-8") as output_file:
    for file_path in file_paths:
        with open(file_path, 'r', encoding="utf-8") as input_file:
            for line in input_file:
                output_file.write(line)
# 9 Create a script that reads a configuration file (e.g., config.ini) and prints out the key-value pairs. Use the configparser library to handle the file.
import configparser
config = configparser.ConfigParser()
config.read(file_name)
for section in config.sections():
    print(f"[{section}]")
    for key, value in config.items(section):
        print(f"{key} = {value}")
    print()
 # 10 Write a script that reads a log file (e.g., server.log) and counts how many times a specific error message appears. Print the number of occurrences of that error.
def count_error_messages(logfile_path, error_prefix):
    # Initialize a counter to zero
    error_count = 0

    # Open and read the log file
    try:
        with open(logfile_path, 'r') as file:
            for line in file:
                # Check if the error prefix exists in the current line
                if error_prefix in line:
                    error_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{logfile_path}' does not exist.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Print the number of times the error message appears
    print(f"The message '{error_prefix}' appears {error_count} times in the log file.")

    # Specify the path to the log file and the error prefix


log_file_path = 'C:/Users/Olena_Smolianchuk/Downloads/server.log'
error_message_prefix = 'ERROR '

# Call the function
count_error_messages(log_file_path, error_message_prefix)

if __name__ == "__main__":
#    read_file()
    count_error_messages(log_file_path, error_message_prefix)

# REGEX----------------------------------------------------------------------------------
# 1 Define the regex pattern for validating an email address
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# 2 Write a regex to find all words that start with a capital letter.
import re

# Sample text for demonstration
text = "Here are Some words that Start With capital Letters and some that do not."

# Regex pattern to match words that start with a capital letter
pattern = r'\b[A-Z][a-zA-Z]*\b'

# Find all matching words in the text
capital_words = re.findall(pattern, text)

# Print the list of words
print(capital_words)
# 3 Write a regex to match a phone number in the format (123) 456-7890.
import re

phone_pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
def is_valid_phone_number(phone):
    if re.match(phone_pattern, phone):
        return True
    return False
phone_numbers = ["(123) 456-7890", "(123)456-7890", "123-456-7890", "(123) 456-789"]

for number in phone_numbers:
    print(f"Phone Number: {number}, Valid: {is_valid_phone_number(number)}")

# 4 Write a regex to find all dates in the format DD/MM/YYYY.
import re

date_pattern = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d\d\b'
text = "Important dates include 01/01/2022, 12/12/2025,  33/13/2023  23/10/1999."

dates = re.findall(date_pattern, text)

formatted_dates = ['/'.join(date) for date in dates]
print("Valid dates found:", formatted_dates)
# 5 Write a regex to match a URL.
import re

url_pattern = r'\b(?:http|https|ftp):\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

text = "Visit our website at https://www.example.com or http://test.example.co.uk. Don't forget our FTP site at ftp://files.example.com."
urls = re.findall(url_pattern, text)
print("URLs found:", urls)
# 6 [TI] Find a max number in a string: abc123def456
import re
input_string = "abc123def456"
numbers = re.findall(r'\d+', input_string)
numbers = [int(num) for num in numbers]
max_number = max(numbers)
print("The maximum number in the string is:", max_number)