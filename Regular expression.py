"""
import re
pattern = r"colour"
text = r"My favourite colour is Red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

"""


#Search And Replace

"""
import re
pattern = r"colour"
text = r"My favourite colour is Red. I love blue colour as well"
text1 = re.sub(pattern,"color",text,count=1)
print(text1)
"""
#Metacharecter

import re
pattern = r"[A-Z] [a-z] [0-9]"

if re.match(pattern,"Ag0"):
    print("Matched")