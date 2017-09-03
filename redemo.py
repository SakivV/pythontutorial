import re

line = "Cats are smarter than dogs"
matchObj = re.match(r'smarter',line)

if matchObj:
    print("Match Found")
else:
    print("Match Not Found")


matchObj2 = re.search(r'smarter',line)

if matchObj2:
    print("Match Found")
else:
    print("Match Not Found")

matchObj3 = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj3:
   print("matchObj3.group() : ", matchObj3.group())
   print("matchObj3.group(1) : ", matchObj3.group(1))
   print("matchObj3.group(2) : ", matchObj3.group(2))
else:
   print("No match!!")


