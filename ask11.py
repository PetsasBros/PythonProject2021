def findk(dic,n,t):
	for i in dic:
		if i== ":" :
			for j in range(i-2,'"',-1):
				if j=='"':
					for k in range(j+1,'"'):
						
	


y=input()
x=open(y, "rt")
kname=list() #kname= το ονομα απο το κλειδι
ktimes=list() #ktimes= ποσες φορες εμφανιζεται το κλειδι
findk(x.read(),kname,ktimes)


"""
αποτυχημενοτερες προσπαθειες που η καρδια μου δεν με επαιρνε να σβησω
def kks(d):
	x=dict()
	for x in d:
		#print(x)
		kks(dict(x.get()))
kks(dict(dic))



from collections import Counter
cnt =Counter()
for word in dic:
	cnt[word]+=1
print(cnt)
#print(Counter(j for k in dic for j in k))
"""
