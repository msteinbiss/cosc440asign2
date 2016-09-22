import sys
import crypt

def main():
	str = ""
	for line in open(sys.argv[2], "r").readlines(): #open file and iterate through it
		if sys.argv[1] in line: #checks for the username in the line
	 		str = line
	if str == "": #if the username is not found
	 	print "Username does not exist",
	 	sys.exit(0)

	sections = str.split(":") #line in the shadow split apart
	parts = sections[1].split("$") #parts of the encryted pw split apart
	salt = "$" + parts[1] + "$" + parts[2] + "$" #type of encryption & actual salt

	pw = ""
	with open("/usr/share/dict/american-english", "r") as f: #iterate through dictionary
		for line in f:
			for word in line.split():
				if crypt.crypt(word, salt) == sections[1]: #encrypt every word & test it
					pw = word
					print "Success! The password is: " + pw
					sys.exit(0)
	if pw == "": 
		print "Password is not in the directory"

if __name__=="__main__":
	main()