import os
nombre = os.getenv("NAME")
edad = int(os.getenv("EDAD"))
if edad >= 18:
    print (f"{nombre} esta ya esta grande")
else:
    print (f"{nombre} uste es un niño deje el celular de mi onichan")