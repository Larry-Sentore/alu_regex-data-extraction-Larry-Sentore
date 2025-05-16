import re
#we will use regex to extract emails, phone numbers, hashes, and credit card numbers from a string

#Importing the sample text from the file
with open('sample.txt', 'r') as file:
    text = file.read()

email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_regex = r'\+?[0-9]{1,4}?[-. ]?\(?[0-9]{1,3}?\)?[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}'
hash_regex = r'#\w+'
credit_card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b(?:\d{4}[- ]?){3}\d{4}\b|\b(?:\d{4}[- ]?){3}\d{4}\b'

def extract_info(text):
    emails = re.findall(email_regex, text)
    phones = re.findall(phone_regex, text)
    hashes = re.findall(hash_regex, text)
    credit_cards = re.findall(credit_card_regex, text)

    print("Search Results:")
    print("----------------")
    print("Emails: ", emails)
    print("Phones: ", phones)
    print("Hashes: ", hashes)
    print("Credit Cards: ", credit_cards)

    return

extract_info(text)
