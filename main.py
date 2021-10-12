import random
from datetime import datetime
import struct

entrada="Hola MundoHola MundoHola MundoHola MundoHola Mundo"
def cortadora(entrada):
	string=entrada
	salida=["","","","","","",""]
	if len(entrada)<28:
		while(len(string)<28):
			string="0"+string
		salida[0]=bytes(string[0:4],encoding='utf-8')
		salida[1]=bytes(string[4:8],encoding='utf-8')
		salida[2]=bytes(string[8:12],encoding='utf-8')
		salida[3]=bytes(string[12:16],encoding='utf-8')
		salida[4]=bytes(string[16:20],encoding='utf-8')
		salida[5]=bytes(string[20:24],encoding='utf-8')
		salida[6]=bytes(string[24:28],encoding='utf-8')
	elif len(entrada)>28:
		string=entrada[0:28]
		salida[0]=bytes(string[0:4],encoding='utf-8')
		salida[1]=bytes(string[4:8],encoding='utf-8')
		salida[2]=bytes(string[8:12],encoding='utf-8')
		salida[3]=bytes(string[12:16],encoding='utf-8')
		salida[4]=bytes(string[16:20],encoding='utf-8')
		salida[5]=bytes(string[20:24],encoding='utf-8')
		salida[6]=bytes(string[24:28],encoding='utf-8')
	else:
		salida[0]=bytes(string[0:4],encoding='utf-8')
		salida[1]=bytes(string[4:8],encoding='utf-8')
		salida[2]=bytes(string[8:12],encoding='utf-8')
		salida[3]=bytes(string[12:16],encoding='utf-8')
		salida[4]=bytes(string[16:20],encoding='utf-8')
		salida[5]=bytes(string[20:24],encoding='utf-8')
		salida[6]=bytes(string[24:28],encoding='utf-8')
	print(salida)
	return(salida)

def procesar(entrada):
	w=[0]*7
	random.seed(datetime.now())
	generador=random.randint(0,31)
	i=0
	while(i<7):
		w[i]=struct.unpack(b'>I', entrada[i])[0]
		i+=1
	print(w)
	w[0]=(w[0]<<generador) & 0xffffffff
	w[1]=(w[1]^generador) & 0xffffffff
	w[2]=(w[2]>>generador) & 0xffffffff
	w[3]=(w[3] & generador) & 0xffffffff
	w[4]=(w[4] | generador) & 0xffffffff
	w[5]=(w[5] ^ w[4] ^ generador) & 0xffffffff
	w[6]=((w[6]^w[5]) << generador) & 0xffffffff
	print(w)
	return b''.join(struct.pack(b'>I', h) for h in w)
	

print(procesar(cortadora(entrada)))
