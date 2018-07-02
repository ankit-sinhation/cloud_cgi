#!/usr/bin/python
import cgi,os,cgitb
cgitb.enable()
print "content-type:text/html"
print ""
data=cgi.FieldStorage()
b=data.getvalue('n')
print "plz wait."
print b
#print "<meta HTTP-EQUIV='refresh' content='3;url=http://192.168.5.4/firefox.tar' target='_self'/>"
