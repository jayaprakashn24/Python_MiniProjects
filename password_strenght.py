
import re 

# re stands for Regular Expression. It is a built-in Python module used to search, match, and validate text based on a pattern.


password = input("Enter password: ")

Strong = (len(password) >=8 and 
          re.search(r'[A-Z]', password)and 
          re.search(r'[a-z]', password)and 
          re.search(r'[0-9]', password)and 
          re.search(r'[!@#$%^&*]', password) )
print("Strong ✅" if Strong else "weak ❌")
