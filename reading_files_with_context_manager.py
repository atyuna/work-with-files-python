
import pdb
# sample 1
# sample_file = '/Users/txt/Favola.txt'. #path changed
# with open(sample_file, 'r') as f:
#     content = f.read()
#
# print(content)
# pdb.set_trace()


# sample 2
countries_file = '/Users/countries.rtf' #path changed
with open(countries_file, 'r') as f:
    countries = f.readlines()

#print(countries)
# pdb.set_trace()

list_of_c = [i.strip() for i in countries]

pdb.set_trace()
