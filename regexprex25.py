#regexprex25.py
import re

result=re.search("python","python is an oop lang. python is an pop lang")
if result!=None:
	print("Search is successful")
else:
	print("Search not successful:")

#findall()-----finding all matches and returns in the form of list object
#finditer()----finding all matches and returns in the form of <Callable_Iterator> object

#serarch()--->finding first match only and it never search futher matches if we have.
                #---->If not matching it return None
