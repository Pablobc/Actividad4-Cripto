import random
from datetime import datetime

entrada="Hola mundo"

def cortadora(entrada):
	string=entrada
	salida=["","","","",""]
	if len(entrada)<25:
		while(len(string)<25):
			string="0"+string
		salida[0]=string[0:5]
		salida[1]=string[5:10]
		salida[2]=string[10:15]
		salida[3]=string[15:20]
		salida[4]=string[20:25]
	elif len(entrada)>25:
		string=entrada[0:25]
		salida[0]=string[0:5]
		salida[1]=string[5:10]
		salida[2]=string[10:15]
		salida[3]=string[15:20]
		salida[4]=string[20:25]
	else:
		salida[0]=string[0:5]
		salida[1]=string[5:10]
		salida[2]=string[10:15]
		salida[3]=string[15:20]
		salida[4]=string[20:25]
	print(salida)
	return(salida)

def procesar(entrada):
	salida=""
	random.seed(datetime.now())
	generador=random.randint(0,255)
	print(generador)
	
procesar("")