import time
import sys
import os
import hashlib
linea=input("Ingrese una palabra:" )
start=time.time()
print(hashlib.md5(linea.encode()).hexdigest())
end= time.time()
print("Tiempo de ejecucion [segundos]:", end-start)