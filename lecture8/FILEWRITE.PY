def main():
    outfile = open('philosopher.txt','w')
    outfile.write('John lock')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    outfile.close()

main()