import random
import math
x=int(input("Δώστε τις πλευρές του ορθογωνίου.\n"))
y=int(input())
z=list()
pl=0 #pl=πληθος των τριαδων
half=math.ceil((x**2)/2)
if x<3 and y<3:
	print("Δεν μπορεί να βρεθεί ο μέσος όρος των τριάδων,\n καθώς οι πλευρές είναι πολύ μικρές.")
else:
	for k in range(100):
		for i in range(x):
			z.append([])
			for j in range(y):
				z[i].append("S")
		metritis=0
		while True:
			i= random.randint(0,x-1)
			j= random.randint(0,y-1)
			if z[i][j]!="O":
				z[i][j]="O"
				metritis +=1
			if metritis==half:
				break
		for i in range(x):
			for j in range(1, y-1):
				if z[i][j]=="O":
					if z[i][j-1]=="S" and z[i][j+1]=="S":
						pl+=1
		for j in range(y):
			for i in range(1, x-1):
				if z[i][j]=="O":
					if z[i-1][j]=="S" and z[i+1][j]=="S":
						pl+=1
		for i in range(1,x-1):
			for j in range(1,y-1):
				if z[i][j]=="O":
					if (z[i-1][j-1]=="S" and z[i+1][j+1]=="S") or (z[i-1][j+1]=="S" and z[i+1][j-1]=="S"):
						pl+=1
	mo=pl/100 #mo=μεσος ορος
	print("Ο μέσος όρος των τριάδων SOS είναι: ",mo)
