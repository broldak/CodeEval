import string
import sys

def emailValid(email):
		if (string.count(email, "@")==0 or string.count(email, "@")>1):
			print "false"
			return False
		else:
			email = string.split(email, "@")
			newEmail = email[0]+email[1]
			print newEmail
			if (string.count(newEmail,".")==0 or string.count(newEmail,".")>1):
				print "false"
				return False
			else:
				for x in email:
					if x in string.punctuation:
						print "1false"
						return False
		print "true"
		return True

emailValid("@h.com")