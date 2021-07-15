import random
class borracho():
    def __init__(self, nombre):
        self.nombre=nombre
    
class borracho_tradicional(borracho):
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
