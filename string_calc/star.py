import re
stringz = "//***\n1***2***3"
x = re.search(r"\n", stringz)
nd_of_delim = x.span()[0]
delim = stringz[2:nd_of_delim]
print(delim)
# for i in delim:
#     stringz = re.sub(i, ";", stringz)
# print(stringz)
#stringz = re.sub(r'\***', ";", stringz)
print(stringz)

stringz = "//***\n1***2^^^3"
x = re.search(r"\n", stringz)
nd_of_delim = x.span()[0]
delim = stringz[2:nd_of_delim]
print(delim)
# stringz = re.sub(r'\***', ";", stringz)
# print(delim)
# for i in delim:
#     i = r"\\" +i
#     stringz = re.sub(i, ";", stringz)

# print(stringz)
print(r"\" +"j")