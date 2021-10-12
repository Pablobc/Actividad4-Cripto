import random
from datetime import datetime

#33-126 ascii


def shift(n, b):
    return ((n << b) | (n >> (7 - b))) 

def cortadora(entrada):
	string=entrada
	salida=["","","","","","",""]
	if len(entrada)<28:
		while(len(string)<28):
			string="0"+string
		salida[0]=string[0:4]
		salida[1]=string[4:8]
		salida[2]=string[8:12]
		salida[3]=string[12:16]
		salida[4]=string[16:20]
		salida[5]=string[20:24]
		salida[6]=string[24:28]
	elif len(entrada)>28:
		string=entrada[0:28]
		salida[0]=string[0:4]
		salida[1]=string[4:8]
		salida[2]=string[8:12]
		salida[3]=string[12:16]
		salida[4]=string[16:20]
		salida[5]=string[20:24]
		salida[6]=string[24:28]
	else:
		salida[0]=string[0:4]
		salida[1]=string[4:8]
		salida[2]=string[8:12]
		salida[3]=string[12:16]
		salida[4]=string[16:20]
		salida[5]=string[20:24]
		salida[6]=string[24:28]
	return(salida)

def procesar(entrada):
	random.seed(datetime.now())
	generador=random.randint(1,7)
	generador2=random.randint(33,126)
	h=[0]*4
	h[0]=shift(ord(entrada[0])^ord(entrada[1]),generador)
	h[1]=shift(ord(entrada[1])|ord(entrada[2]),generador)^h[0]
	h[2]=shift(ord(entrada[3])^ord(entrada[0]),generador)^ord(entrada[2])|h[1]^h[0]
	h[3]=shift((ord(entrada[2])|h[0])^ord(entrada[3])^h[2],generador)^h[1]
	i=0
	while(i<4):
		h[i]=h[i]&126
		if h[i]<33:
			h[i]+=generador2
			h[i]=h[i]&126
		if h[i]<33:
			h[i]+=33
		i+=1
	return "".join(chr(j) for j in h)	


def shiaa_28(entrada):
	chunks=cortadora(entrada)
	out=[0]*7
	i=0	
	while(i<7):
		out[i]=procesar(chunks[i])
		i+=1
	return "".join(j for j in out)

if __name__ == '__main__':
	import os
	opt=0
	while(opt!=10):
		print("1-Ingresar un mensaje para hash")
		print("2-Calcular entropia de un texto")
		print("3-Salir")
		opt=input("Ingrese una opcion: ")
		print(opt)
		if(opt=="1"):
			text=input("Ingrese un mensaje o una direccion de archivo: ")
			if(os.path.isfile(text)):
				data=open(text,'r')
				for line in data:
					print(shiaa_28(line.strip()))
			else:
				print(shiaa_28(text))
			continue
		elif(opt=="2"):
			text=input("Ingrese un texto para calcular su entropía: ")
			continue
		elif(opt=="3"):
			opt=10
			continue
