import sys
import os
try:
	x = sys.argv[1]
except Exception:
	print('error: no first parameter')
	quit()
y = os.path.isfile(x)
if y:
	pass # check if dir exists
else:
	print('not valied directory')
	quit()
w=open(x, 'r')
a=w.read()
b=list(a)
c=''
j = 0
for i in b:
	if i == '\n':
		b[j] = ' '
	elif i == ';':
		b[j] = ' '
	elif i == '\'':
		b[j] = ' \' '
	elif i == ':':
		try:
			if b[j-1] == 't':
				b[j] = ': '
			elif b[j-1] == 'd':
				b[j] = ': '
			elif b[j+1] == 'b':
				b[j] = ' :'
		except Exception:
			pass#
	j+=1
for i in b:
	c=c+str(i)
b=str(c).split()
j=''
m=0
n=0
ind=2
style=''
for i in b:
	k=''
	indent='\t'*ind
	if i == 'class':
		try:
			j=j+str(indent)+'<div class=\''+str(b[m+1])+'\'>\n'
			ind+=1
		except Exception as err:
			print('syntax error: no class name')
			quit()
	elif i == 'class-end':
		ind-=1
		if ind < 2:
			ind = 2
		indent='\t'*ind
		j=j+str(indent)+'</div>\n'
	elif i == 'p:':
		j=j+str(indent)+'<p>'
		n+=2
		try:
			while b[n] != '\'':
				k=k+str(b[n])+' '
				n+=1
		except Exception:
				print('syntax error: no end of string')
		j=j+k+'</p>\n'
	elif i == 'script:{':
		try:
			j=j+str(indent)+'<script src=\''+b[n+1]+'\'>'+'</script>\n'
		except Exception:
			print('syntax error: no file atached to the script:{ tag')
	elif i == 'style:{':
		try:
			style=style+'\t\t<link rel="stylesheet" href="'+b[n+1]+'">\n'
		except Exception:
			print('syntax error: no file atached to the style:{ tag')
	elif i == 'input:':
		try:
			if b[m+1] == 'button=>{':
				j=j+str(indent)+'<button class=\''+b[m+2]+'\'>'
				try:
					n=n+4
					while b[n] != '\'':
						k=k+str(b[n])+' '
						n+=1
				except Exception:
					print('syntax error: no end of string')
				j=j+k+'</button>\n'
			elif b[m+1] == 'textbox=>{':
				j=j+str(indent)+'<input type=\'text\' id=\''+b[m+2]+'\' name=\''+b[m+3]+'\'>'
				n+=3
				j=j+k+'\n'
		except Exception:
			print('syntax error')
	elif i == ':br>':
		j=j+str(indent)+'<br>\n'
	if ind < 2:
		ind = 2
	m+=1
	n=m
x = os.path.splitext(x)[0]
w=open(x+'.html', 'w')
w.write(
	'<!DOCTYPE html>\n'
	'<html>\n'
	'\t<head>\n'
	'\t\t<meta charset="utf-8">\n'
	+style+'\n'
	'\t</head>\n'
	'\t<body>\n'
	+j+'\n'+
	'\t</body>\n'
	'</html>'
)
w.close()