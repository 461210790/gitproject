import sys
import unicodedata
print("decimal    hex    chr    {0:^40}".format("name"))
print("------    ---    ---    {0:-^40}".format(""))
for i in  range(32,122):
    c=chr(i)
    name=unicodedata.name(c, "***unknown***")
    print("{0:7}    {0:5X}    {0:^3c}    {1:^40}".format(i,name.title()))
