import sys
import crypt

def main():
	str = ""
	for line in open(sys.argv[2], "r").readlines():
		if sys.argv[1] in line: #checks for the username in the line
	 		str = line
	if str == "":
	 	print "Username does not exist",
	 	sys.exit(0)

	sections = str.split(":") #line in the shadow
	parts = sections[1].split("$") #parts of the encryted pw
	salt = "$" + parts[1] + "$" + parts[2] + "$"


	pw = ""
	with open("/usr/share/dict/american-english", "r") as f:
		for line in f:
			for word in line.split():
				if crypt.crypt(word, salt) == sections[1]:
					pw = word
					print "Success! The password is: " + pw
					sys.exit(0)
	if pw == "":
		print "Password is not in the directory"

if __name__=="__main__":
	main()