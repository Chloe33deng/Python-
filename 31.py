def cInTxt(filename,char):
	count=0
	fo=open(filename,'r')
	txt=fo.read()
	txt=txt.lower()
	for word in txt:
		if char==word:
			count+=1
	fo.close()
	return count
 
print(cInTxt('Hamlet.TXT','t'))

