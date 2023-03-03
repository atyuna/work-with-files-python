my_string = 'I love to learn new thing'
a_string = 'Ha ha ha it is only the beginning!'

# exemple 1

my_f = open('/Users/txt/sample_output1.txt', 'w')
my_f.write(my_string)
my_f.close()

# exemple 2

my_f = open('/Users/txt/sample_output1.txt', 'a')   #path changed
my_f.write(a_string + '\n')
my_f.write(a_string + '\n')
my_f.write(my_string + "\n")
my_f.write(a_string + '\n')
my_f.close()
