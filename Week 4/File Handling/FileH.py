# File = open('text1.txt', 'r')
# F = File.readlines()

# for line in F:
#     print(line)
# File.close()

# String = 'Starting Line\nMiddle Line\nLast Line'

# with open('text2.txt', 'r') as File2:
#     LINES = File2.readline(5)
#     print(LINES)
#     for line in LINES:
#         print(line)

Name = input('Enter your name: ')
Password = input('Enter your Password: ')
# Age  = input('Enter your age: ')

# # with open('data.txt', 'a') as D:
# #     # D.write(Name+Age+Password)
# #     D.write(Name+',')
# #     D.write(Age+',')
# #     D.write(Password+'\n')

with open('data.txt', 'r') as d: 
    Lines = d.readlines()
    for line in Lines:
        L = line.split(',')
        # print(L)
        if Name == L[0] and Password == L[2].strip():
            print(line)
            break