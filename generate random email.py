"""
Exercises:
Create a file with list of randomly generated email addresses.
The email addresses must have domain name from the
given list of domains.
* Domain list is provided as variable 'list_of_domains'

HINT:
To generate random string with all lower case you can use this code
import random
import string
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(length))

V1:
- Create 20 emails for each domain
- Output a csv file with one email on each line and each line ending with a comma
- Output file name: out_generate_random_email_with_list_of_domains_v1.csv
"""


import random
import string

list_of_domains = ['supersqa.com', 'gmail.com', 'yahoo.com', 'outlook.com', 'msn.com']

len_of_email = 10 # 10 characters in email
letters = string.ascii_lowercase
output_path = '/Users/anna/Desktop/txt/out_generate_random_email_with_list_of_domains_v1.csv'

# generate random emails and store in the list
all_emails = []
for domain in list_of_domains:
    for i in range(20):
        random_string = ''.join(random.choice(letters) for i in range(len_of_email))
        # email = random_string + '@' + domain
        email = f'{random_string}@{domain}'
        #email = "{}@{}".format(random_string, domain)
        print(email)
        all_emails.append(email)
print(all_emails)

# import pdb; pdb.set_trace()

# take the list and write file:
with open(output_path, 'w') as file:
    for email in all_emails:
        file.write(email)
        file.write(", \n")