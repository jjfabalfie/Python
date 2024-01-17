import os
import getpass
def main():
	loginDB = {
		"User1": "Password1",
		"User2": "Password2",
		"User3": "Password3",
		"User4": "Password4",}
	print("Welcome to JJFAB Security")
	print("##########################")
	user = str(input("Please enter your username: "))
	passwd = getpass.getpass(prompt="Password: ", stream=None) 
	if user in loginDB and passwd == loginDB[user]:
		print ("Login Succesful Welcome ",user, "!")
	else:
		print ("Login Failed, Locking Out")
main()
