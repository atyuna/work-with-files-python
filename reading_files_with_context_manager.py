
import pdb
# sample 1
# sample_file = '/Users/anna/Desktop/txt/Favola.txt'
# with open(sample_file, 'r') as f:
#     content = f.read()
#
# print(content)
# pdb.set_trace()


# sample 2
countries_file = '/Users/anna/Desktop/countries.rtf'
with open(countries_file, 'r') as f:
    countries = f.readlines()

#print(countries)
# pdb.set_trace()

list_of_c = [i.strip() for i in countries]

pdb.set_trace()