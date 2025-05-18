import re
#we will use regex to extract emails, phone numbers, hashes, and credit card numbers from a string

#Importing the sample text from the file
with open('sample.txt', 'r',  encoding='utf-8') as file:
    text = file.read()

#assigning regex patterns to their respective variables
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_regex = r'\+?[0-9]{1,4}?[-. ]?\(?[0-9]{1,3}?\)?[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,4}[-. ]?[0-9]{1,9}'
hash_regex = r'#\w+'
credit_card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b(?:\d{4}[- ]?){3}\d{4}\b|\b(?:\d{4}[- ]?){3}\d{4}\b'

#Function to extract information
def extract_info(text):
    
    #Using the findall command from the re module to extract the information
    #Saving the results in lists
    emails = re.findall(email_regex, text)
    phones = re.findall(phone_regex, text)
    hashes = re.findall(hash_regex, text)
    credit_cards = re.findall(credit_card_regex, text)

    #Printing the results
    print("Search Results:")
    print("----------------")
    print("Emails: ", emails)
    print("Phones: ", phones)
    print("Hashes: ", hashes)
    print("Credit Cards: ", credit_cards)
    print("----------------")

    return

#Calling the function to extract information
extract_info(text)
