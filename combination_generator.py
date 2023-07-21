letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
indexes = []
password_length = int(input("How many letters is each word: "))
answer = input("Would you like to use the default character list consisting of lower case letters?\n"
               "Type (y)es or (n)o: ")
if answer == 'n':
    characters = input("Enter all the characters you want to use. Do not separate them by any character or space.\n")
    letters = list(characters)
idx = 0
while idx < password_length:
    indexes.append(0)
    idx += 1
idx = 0

def index_fixer(list_of_indexes):
    idx = 0
    try:
        while list_of_indexes[idx] != len(letters):
            idx += 1
        list_of_indexes[idx] = 0
    except IndexError:
        return False
    try:
        list_of_indexes[idx + 1] += 1
    except IndexError:
        return False
    return list_of_indexes

with open('passwords.txt', 'w') as file:
    while indexes:
        string = ''
        for index in indexes:
            string += letters[index]
        indexes[0] += 1
        try:
            while len(letters) in indexes:
                indexes = index_fixer(indexes)
        except:
            pass
        file.write(string + "\n")
