def mostrar_fila(x):
    if x!=[]:
        print(str(x[0]))
        mostrar_fila(x[1:])

def crear_fila(x,z,c,f):
    if(f>=0):
       
        z.append(x[f][c])
        return crear_fila(x,z,c,f-1)
    else:
        return z[::-1]

def rotar(x,y,c):
    if c>=0:
        y.append(crear_fila(x,[],c,len(x)-1))
        return rotar(x,y,c-1)
    else:
        return y

                     
    
def mostrar(x):
    if x!=[]:
        mostrar_fila(x[0])
        mostrar(rotar(x[1:],[],len(x[0])-1))




mostrar([x.split() for x in open('matriz.txt').readlines()])

