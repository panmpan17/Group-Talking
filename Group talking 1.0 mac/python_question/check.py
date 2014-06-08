def check(gn, gp, un, up):
	import urllib2
	data = urllib2.urlopen('http://orangeapple-student-data.appspot.com')
	User = open('user.py','w')
	User.write(data.read() +'\ng = \''+ gn+'\'\n'+"un = '" + un + "'")
	User.close()
	from user import user
	if (gn in user) and (user[gn][0] == gp):
		if (un in user[gn][1]) and (user[gn][1][un] == up):
			return True
	return False