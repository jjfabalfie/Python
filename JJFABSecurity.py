import os
import getpass
def main():
	loginDB = {
		"Alfie": "Password1",
		"Jake": "Password2",
		"Jasmine": "Password3",
		"Bonnie": "Password4",}
	print("Welcome to JJFAB Security")
	print("##########################")
	user = str(input("Please enter your username: "))
	passwd = getpass.getpass(prompt="Password: ", stream=None) 
	if user in loginDB and passwd == loginDB[user]:
		print ("Login Succesful Welcome ",user, "!")
	else:
		print ("Login Failed, Locking Out")
main()
