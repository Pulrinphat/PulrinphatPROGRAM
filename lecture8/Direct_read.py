def example_w_plus_mode():
    with open('example_w+.txt','w') as file:
        file.write("this is the first line in the file.\n")
        file.write("this is the second line in the file.\n")

        file.seek(0)

        content = file.read()
        print("Content of the file:")
        print(content)

example_w_plus_mode()