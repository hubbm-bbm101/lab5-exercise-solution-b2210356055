mail=input("E-mail : ")
mail_check = ('@' in mail) and ('.' in mail)
if mail_check:
	print("Welcome")
else:
	print("invalid mail address")