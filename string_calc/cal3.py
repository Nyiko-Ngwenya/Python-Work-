import re
stringz = "//***\n1***2***3"
#stringz = "//4\n1424345"
x = re.search(r"\n", stringz)
nd_of_delim = x.span()[0]
delim = stringz[2:nd_of_delim]
print(type(delim))
print(len(delim))
for i in delim:
    print(f'{i} is the char')
if delim == '***':
    print('we are same')
else:
    print('we not')
print(delim)
#stringz = re.sub(delim, ";", stringz)
stringz = re.sub("1", ";", stringz)
print(stringz)


# #stringz = '//4\n1424345'
# #stringz = re.sub('4', ";", stringz)
# print(stringz)
# count = 0
# pattern = r'-?\d+'
# collectedNumbers = re.findall(pattern, stringz)
# print(collectedNumbers)
#stringz = '//[***][777][:(]\n1abc27773:(1'
bull = r"*/*/*"
print(bull)
stringz = re.sub(bull, ";", stringz)
# print(stringz)
print(type('***'))
