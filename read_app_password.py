import os

"""
This file exists to record the app password in at least a semi-secure way. The filename the password will be written to has been added to .gitignore and will have file permissions set such that only the owner can read or write to it.
"""


app_password = raw_input("What is your app password?\n")
assert(app_password != '')

text = '# This file contains the app password you created. For more info on the app password see README.md'

filename = 'appp.txt'

if os.path.isfile('./' + filename):
	print(filename + ' exists. Please delete and run this file again if you wish to re-record your password.')
else:
	with open(filename,'w') as f:
		f.write(text + '\n' + app_password)
		os.chmod(filename, 0o600)
