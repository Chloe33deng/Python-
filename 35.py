import re
def getText():
	txt=open("Hamlet.TXT","r").read()
	txt=txt.lower()
	for c in txt:
		if (c>='a' and c<='z'):
			continue
		else:
			txt=txt.replace(c,' ')
	txt=re.sub(' +',' ',txt) #正则表达式
	return txt
 
def dealtxt(txt):
	txtlist=txt.split(' ')
	for k in txtlist:
		txtdict[k]=txtdict.get(k,0)+1
	return txtlist
 
def sorttxt(txtlist):
	newtxtl=list(txtdict.items())
	newtxtl.sort(key=lambda x:x[1],reverse=True)
	return newtxtl
 
def showtxt(newtxtl,num):
	for i in range(num):
		print("{0:<15}{1:>10}".format(newtxtl[i][0],newtxtl[i][1]))
 
def main():
	txt=getText()
	txtlist=dealtxt(txt)
	newtxtl=sorttxt(txtlist)
	showtxt(newtxtl,10)
 
txtdict={}
main()



