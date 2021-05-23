#regexprex22.py
#program  for searching only 'a'
import re
matinfo=re.finditer("a", "abaabaaab")
print("-----------------------------------------------------------------")
for mat in matinfo:
	print("start index={}\t value={}".format(mat.start(),mat.group()))
print("-----------------------------------------------------------------")
