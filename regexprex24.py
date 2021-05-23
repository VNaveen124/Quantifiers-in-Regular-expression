#regexprex24.py
#program  for searching zero or one 'a' or more 'a' s
import re
matinfo=re.finditer("a*", "abaabaaab")
print("-----------------------------------------------------------------")
for mat in matinfo:
	print("start index={}\t value={}".format(mat.start(),mat.group()))
print("-----------------------------------------------------------------")

#output
#start Index       end index   values
#   0                   1       a
#   1		        2	-----	
#   2                   4       aa
#   4			5       -----
#   5                   8       aaa
#   8                   9       -----
#   9							
