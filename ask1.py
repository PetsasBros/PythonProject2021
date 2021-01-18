import random
import math

x=int(input("Δώστε τη διάσταση του τετραγώνου.\n"))
y=list()
fpl=0 #fpl=μετραει το πληθος των τετραδων
pl=math.ceil((x**2)/2)
if x>3:
	for k in range(100):
		for i in range(x):
			y.append([])
			for j in range(x):
				y[i].append(0)
		metritis=0
		f=0 #f=μετραει τις τετραδες
		while True:
			i= random.randint(0,x-1)
			j= random.randint(0,x-1)
			if y[i][j]!=1:
				y[i][j]=1
				metritis +=1
			if metritis==pl:
				break
		for i in range(x):
			for j in range(x):
				if y[i][j]==1:
					f+=1	
				else:
					if f==4:
						fpl+=1
					f=0
		f=0
		for j in range(x):
			for i in range(x):
				if y[i][j]==1:
					f+=1
				else:
					if f==4:
						fpl+=1
					f=0
		f=0
		for i in range(x):
			for j in range(x):
				if i==j:
					if y[i][j]==1:
						f+=1
					else:
						if f==4:
							fpl+=1
						f=0
		f=0
		for i in range(x):
			for j in range(x):
				if i+j==x+1:
					if y[i][j]==1:
						f+=1
					else:
						if f==4:
							fpl+=1
						f=0
		f=0
	z=fpl/100
	print("Ο μέσος όρος των τετράδων είναι ", z)
else:
	print("Δεν μπορεί να εμφανιστεί ο μέσος όρος των τετράδων,\n καθώς ο πίνακας είναι πολύ μικρός.")
				
