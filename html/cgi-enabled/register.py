#!/usr/bin/python

# Import modules for CGI handling 
import cgi, os
import cgitb; 

cgitb.enable()

form = cgi.FieldStorage()
		

# Get data from fields
firstname = form.getvalue('firname')
lastname  = form.getvalue('lstname')
fileitem = form['filename']


# Checkbox
hobbies=""
if form.getvalue('reading'):
   hobbies = "Reading "

if form.getvalue('cooking'):
   hobbies += "Cooking "

if form.getvalue('listening'):
   hobbies += "Listening "

#RadioButton
if form.getvalue('gender'):
   gender = form.getvalue('gender')
else:
   gender = "Not set"

#TextArea
if form.getvalue('textcontent'):
   text_content = form.getvalue('textcontent')
else:
   text_content = "Not entered"

#Dropdown box
if form.getvalue('dropdown'):
   edu = form.getvalue('dropdown')
else:
   edu = "Not entered"

if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('/tmp/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   path = '/tmp/' + fn
   image = Image.open('/tmp/' + fn)
   image.show()   
else:
   message = 'No file was uploaded'


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Register</title>"
print "</head>"
print "<body>"
print "<center>"
print "<br/><br/><br/><br/>"
print "<h2><u>Hello %s %s</u></h2>" % (firstname, lastname)
print "<br/>"
print "<b>First Name:</b>  %s" % firstname
print "<br/>"
print "<b>Last Name:</b>  %s" % lastname
print "<br/>"
print "<b>Hobiies:</b> %s" % hobbies
print "<br/>"
print "<b>Gender:</b> %s" % gender
print "<br/>"
print "<b>Comments . :</b> %s" % text_content
print "<br/>"
print "<b>Education :</b> %s" % edu
print "<h1><p>%s</p>"  % (message,)  
print "<img src ='%s' alt = '/tmp/%s'>"  % (path,fn,)
print "<button><a href='http://127.0.0.1/register.html'>Back</a></button>"         
print "</center>"
print "</body>"
print "</html>" 
         
