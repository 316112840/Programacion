class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def longitud(self): #Para calcular la longitud del vector
        return (self.x*self.x + self.y*self.y + self.z*self.z )**0.5
    def SumaVectores(a,b):
        return Vector3D(a.x + b.x, a.y + b.y, a.z + b.z )
    def RestaVectores(a,b):
        return Vector3D(a.x - b.x, a.y - b.y, a.z - b.z )
    def imprime(self):
        print("x:",self.x, "\ny:", self.y, "\nz:", self.z )
