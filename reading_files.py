coun_file = open ('countries.txt', 'r')
for lines in coun_file.readlines():
    print(lines)


coun_file.close()