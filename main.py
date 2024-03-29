import random
from datetime import datetime
import time

#33-126 ascii

#Entrada: 2 enteros
#Salida: bits del numero n desplazados circularmente b veces
def shift(n, b):
    return ((n << b) | (n >> (7 - b))) 

#entrada: string de largo x
#salida: lista de 7 strings de 4 letras cada una confeccionada a partir de los primeros 28 caracteres del string entrada.
#En caso de haber menos de 28 caracteres, la string de entrada se rellena con 0 a la izquierda
def cortadora(entrada):
	string=entrada
	salida=["","","","","","",""]
	if len(entrada)<28:
		if(len(entrada)<2):
			while(len(string)<28):
				string="0"+string
		else:
			while(len(string)<28):
				aux=ord(string[0])+ord(string[1])
				aux=aux & 126
				if aux<33:
					aux+=33
				string=chr(aux)+string
		salida[0]=string[0:4]
		salida[1]=string[4:8]
		salida[2]=string[8:12]
		salida[3]=string[12:16]
		salida[4]=string[16:20]
		salida[5]=string[20:24]
		salida[6]=string[24:28]
	elif len(entrada)>28:
		while(len(string)>28):
			aux=""
			for i in range(len(string)-1):
				aux2=ord(string[i])^ord(string[len(string)-(i+1)])
				aux2=aux2 & 126
				if aux2<33:
					aux2+=33
				aux+=chr(aux2)
			string=aux
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

#entrada: string de 4 caracteres
#salida: string de 4 caracteres, producida a partir de la string de entrada donde a cada caracter se le hizo una permutacion distinta con un numero generado aleatoriamente
#y otras operaciones

def procesar(entrada):
	generador=random.randint(1,7)
	generador2=random.randint(33,126)
	h=[0]*4
	h[0]=h[0]+shift(ord(entrada[0])^ord(entrada[1]),generador)+h[1]+h[2]
	h[1]=h[1]+shift(ord(entrada[1])|ord(entrada[2]),generador)^h[0]
	h[2]=h[2]+(shift(ord(entrada[3])^ord(entrada[0]),generador)^ord(entrada[2])|h[1]^h[0])
	h[3]=h[3]+(shift((ord(entrada[2])|h[0])^ord(entrada[3])^h[2],generador)^h[1])
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

#entrada: lista de 7 strings de 4 caracteres
#salida: string producida a partir de la union de 7 strings de 4 caracteres a las cuales se le aplico la función procesar()

def shiaa_28(entrada):
	random.seed(datetime.now().replace(second=0, microsecond=0))
	chunks=cortadora(entrada)
	out=[0]*7
	i=0	
	while(i<7):
		out[i]=procesar(chunks[i])
		i+=1
	return "".join(j for j in out)

if __name__ == '__main__':
	import os
	import math
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
				start = time.time()
				data=open(text,'r')
				for line in data:
					print("Texto: "+line.strip()+" ----- Hash: "+shiaa_28(line.strip()))
				end = time.time()
				print("Tiempo de ejecucion [segundos]:", end-start)
			else:
				start = time.time()
				print("Texto: "+text.strip()+" ----- Hash: "+shiaa_28(text))
				end = time.time()
				print("Tiempo de ejecucion [segundos]:", end-start)
			continue
		elif(opt=="2"):
			text=input("Ingrese un texto para calcular su entropía: ")
			print(text +"\nEntropía -----"+str(len(text)*math.log(94,2)))
			continue
		elif(opt=="3"):
			opt=10
			continue
