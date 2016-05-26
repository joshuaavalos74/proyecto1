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

def prob_4 (Caracter,lon):
	h = len caracter
	lon=lon-h
	lon=lon/2
	return ("*"*lon, caracter , "*"*lon)

def prob_5	