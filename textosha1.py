import time
import hashlib
archivo=input("Ingrese nombre de archivo:" )
data=open(archivo,'r')
start=time.time()
for line in data:
	print(hashlib.sha1(line.encode()).hexdigest())
end= time.time()
print("Tiempo de ejecucion [segundos]:", end-start)