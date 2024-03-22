class livre :
    def __init__(self, titre = "programmation en javascript", auteur = "karlMartson", prix = 123):
        self.T = titre
        self.A = auteur
        self.P = prix
    def initialiser(self):
        self.T = input("entrer le titre de livre : ")
        self.A = input("entrer l'auteur de livre : ")
        self.P = float(input("entrez le prix du livre : "))

    def getTitre(self):
        return self.T
    def getAuteur(self):
        return self.A
    def getPrix(self):
        return self.P
    
    def setTitre(self,new_titre):
        self.T = new_titre

    def setAuteur(self, new_Auteur):
        self.A = new_Auteur
    
    def setPrix(self, new_Prix):
        self.P = new_Prix

    def afficher(self):
        print("Titre :", self.T , "\nAuteur :", self.A, "\nPrix :", + str(self.P))
    
l1 = livre()
print(l1)
print("\n---------------------------------")
l2 = livre("learn python")
print(l2)
print("\n---------------------------------")
l3 =  livre("learn java", "younes")
print(l3)

l1.initialiser()
print(l1)