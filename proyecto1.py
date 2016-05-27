def prob_1 (num):
	return (num%2==0)	
	
def prob_2 (grad):
	cel=(grad-32)/1.8
	return (cel)	

def prob_3 (base, potencia):
	p=base
	for i in range (1, potencia):
		base=base*p
	return (base)	

def prob_4 (caracter,palabra):
	
	casi=(caracter-len(palabra))
	return ("*"*lon, caracter , "*"*lon)

def prob_5	(l1,l2,x,y,z,X,Y,Z):
	l1=[x,y,z]
	l2=[X,Y,Z]
	l3=[]
	wx=(l1[1]*l2[2]) - (l1[2]*l2[1])
	wy=(l1[2]*l2[0]) - (l1[0]*l2[2])
	wz=(l1[0]*l2[1]) - (l1[1]*l2[0])
	l3=[wx,wy,wz]