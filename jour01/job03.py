class Operation :
    
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat
    
test = Operation(3,2)

print(f"le nombre1 est {test.nombre1}, le nombre2 est {test.nombre2}")
print(f"l'addition du nombre1 et du nombre2 est {test.addition()}")

