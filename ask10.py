def depth(dic):
	Max=0
	size =-1
	for i in dic:
		if i== "{": #μετραει καθε καινουρια αγκυλη, καθως αυτο σημαινει ενα καινουριο εμφωλευμενο λεξικο
			size+=1
		if i== "}":
			if Max<size:
				Max=size
			size-=1 #διασφαλιζει πως βρισκομαστε στον σωστο αριθμο των αγκυλων
	return(Max)

y=input("Δώστε το αρχείο.\n") 
x= open(y, "rt") #x= ανοιγει το αρχειο
print(depth(x.read()))
