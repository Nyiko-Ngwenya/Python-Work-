import re

def Add(stringz):
    if stringz:
        if stringz[:2] == '//':
            x = re.search(r"\n", stringz)
            nd_of_delim = x.span()[0]
            delim = stringz[2:nd_of_delim+1]
            # print(delim)
            if '[' in delim:
                pattern = r'\[.*?\]'
                collected_delimiters = re.findall(pattern, stringz)
                for i in collected_delimiters:
                    stringz = re.sub(i, ";", stringz)
                count = 0
                pattern = r'-?\d+'
                collectedNumbers = re.findall(pattern, stringz)
                print(collectedNumbers)
                for number in collectedNumbers:
                    if int(number) < 1000:
                        count += int(number)    
                return count
            else:
                x = re.search(r"\n", stringz)
                nd_of_delim = x.span()[0]
                delim = stringz[2:nd_of_delim]
                stringz = re.sub(delim, ";", stringz)
                count = 0
                pattern = r'-?\d+'
                collectedNumbers = re.findall(pattern, stringz)
                print(collectedNumbers)
                for number in collectedNumbers:
                    if int(number) < 1000:
                        count += int(number)    
                return count
                

        # pattern = r'-?\d+'
        # collectedNumbers = re.findall(pattern, stringz)
        # arrayNeg = [negative for negative in collectedNumbers if '-' in negative]
        # if arrayNeg:
        #     if len(arrayNeg) > 1:
        #         raise Exception(f'these are {arrayNeg} negative')
        #     else:
        #         raise Exception(f'this {arrayNeg[0]} is a negative ,negatives not allowed')
        # if collectedNumbers:
        #     for number in collectedNumbers:
        #         if int(number) < 1000:
        #             count += int(number)    
        #     return count
        else:
            count = 0
            pattern = r'-?\d+'
            collectedNumbers = re.findall(pattern, stringz)
            for number in collectedNumbers:
                if int(number) < 1000:
                    count += int(number)    
            return count

    else:
        return 0  

# print(add(""))
# #// should return 0

# print(add("1"))
# #// should return 1

# add("1,1")
# #// should return 2

# add("1,2,3,4")
# #// should return 10

# add("")
# #// should still return 0

# add("1")
# #// should still return 1

# add("1,1")
# #// should still return 2

# print(add("//;\n1;2"))
#// should return 3

#add("//4\n1424345")
#// should return 3

# add("//[:D][%]\n1:D2%3")
# #// should return 6

# add("//[***][%%%]\n1***2%%%3")
# #// should return 6

# add("//[(-_-')][%]\n1(-_-')2%3")
# #// should return 6

# add("//[abc][777][:(]\n1abc27773:(1")
# #// should return 7

# txt = "The rain in Spain"
# x = re.sub("rain", "9", txt)
# print(x)
# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)