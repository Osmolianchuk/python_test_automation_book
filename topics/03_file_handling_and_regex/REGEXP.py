
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