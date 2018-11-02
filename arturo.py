# you can translate arabic numbers to roman and vice versa
# but only up to 3999
# for translate arabic numbers use <ar_to_ro('number')> command
# for translate roman numbers use <ro_to_ar('number')> command
# but you must use capital letters for this
import re

romeCount={'M':1000, 'MM' : 2000, 'MMM':3000, 'C':100, 'CC':200,'CCC':300,
'XXX':30, 'XX':20, 'X':10, 'I':1, 'II':2, 'III':3,
'CM':900, 'DC':400, 'XC':90, 'XL':40, 'IV':4, 'IX':9,
'L':50, 'V':5, 'D':500}
romeCount.update((zip(('VI','VII','VIII','LX','LXX','LXXX','DC','DCC','DCCC'),
	(6,7,8,60,70,80,600,700,800))))


pattern =re.compile(r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})')

def ro_to_ar(x):
	b=list(pattern.search(x).groups())
	# print(b)
	# print(type(b))

	a=0
	for i in b:	
		print(i)
		if i in romeCount:
			a += romeCount[i]
		else:
			a+=0
	print( a)

digits=tuple(romeCount.values())
letters=tuple(romeCount.keys())
rDict=dict()
# print(rDict)
for i in range(len(digits)):
	
	rDict[digits[i]]=letters[i]
# print(rDict)
rDict.update(zip((6,7,8,60,70,80,600,700,800,'nope'),
	('VI','VII','VIII','LX','LXX','LXXX','DC','DCC','DCCC','')))
# print(rDict)

def ar_to_ro(a):


	a1=((a//1000)*1000) if a>999 else 'nope'
	a2=(((a//100)%10)*100) if a>99 else 'nope'
	a3=(((a//10)%10)*10) if a>9 else 'nope'
	a4=(a%10) if a>0 else 'nope'
	print((a))
	result=(a1 ,a2 ,a3, a4)
	# print(result)
	res=''
	for i in result:
		res+=(rDict[i])
	print(res)



