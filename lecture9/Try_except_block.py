filename = input('ENter a filename : ')
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except I0Error:
    print('An error occured trying to raed')
    print('The file', filename)
print("End of program")