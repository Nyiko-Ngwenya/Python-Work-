import re
#stringz = '//[abc][777][:(]\n1abc27773:(1'
stringz = "//***\n1***2***3"
pattern = r'\[.*?\]'
collected_delimiters = re.findall(pattern, stringz)
for i in collected_delimiters:
    stringz = re.sub(i, ";", stringz)

#print(collectedNumbers)
print(stringz)
count = 0
pattern = r'-?\d+'
collectedNumbers = re.findall(pattern, stringz)
print(collectedNumbers)
for number in collectedNumbers:
    if int(number) < 1000:
        count += int(number)    
print(count) 
# x = re.sub("abc", ";", stringz)
# print(x)