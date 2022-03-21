def main():
	year=getYear()
	flag=isRun(year)
	printRun(flag)
 
def getYear():
	while True:
		try:
			year=eval(input("请输入一个年份\n"))
			return year
		except:
			print("请输入一个整数\n")
 
def isRun(year):
	if year%4==0 and year%100!=0:
		return True
	elif year%400==0:
		return True
	else:
		return False
 
def printRun(flag):
	if flag:
		print("闰年")
	else:
		print("不是闰年")
 
main()

