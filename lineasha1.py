import time
import sys
import os
import hashlib
linea=input("Ingrese una palabra:" )
start=time.time()
print(hashlib.sha1(linea.encode()).hexdigest())
end= time.time()
print("Tiempo de ejecucion [segundos]:", end-start)