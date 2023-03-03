my_string = 'Once upon a time there was a girl....'

# ex 1

# with open('/Users/anna/Desktop/txt/sample_output2.txt', 'w') as f:
#     f.write(my_string)

# ex 2 (appending)
my_list = ['user1', 'user2', 'user3']
with open('/Users/anna/Desktop/txt/sample_output2.txt', 'a') as f:
    for i in my_list:
        f.write(i + '\n')
        f.write(i + '\t')
        f.write('\n')
        f.write("this is a new line")


# ex 3

my_langs = ['Java','Python','Ruby','PHP']
with open('/Users/anna/Desktop/txt/my_lang.csv','w') as l:
    l.writelines(my_langs)

# ex

my_langs = ['Java','Python','Ruby','PHP']
with open('/Users/anna/Desktop/txt/my_lang_join.csv','w') as g:
    my_str_lang = '\n'.join(my_langs)
    g.write(my_str_lang)