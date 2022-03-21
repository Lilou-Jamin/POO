import random # Utilisé pour les nombres aléatoires

# Classe de Pokemon utilisé pour le Player mais aussi pour l'ordinateur
class Pokemon :
    def __init__(self) :
        # On instancie les attributs de la classe à des valeurs initiales
        self.nomdupokemon = ""
        self.pointsdevie = 0
        self.typespokemon = "Aucun"
        self.attaque = 0
        self.bonusattaque = 1
    # Méthode Choix du pokémon du Player
    # Mise à jour des attributs en fonction du choix de Pokémon
    def ChoixPlayerpokemon(self, nom):
        if nom == "Pyroli" :
            self.nomdupokemon = "Pyroli"
            self.pointsdevie = 65
            self.typespokemon = "Feu"
            self.attaque = 60
        elif nom == "Carapuce" :
            self.nomdupokemon = "Carapuce"
            self.pointsdevie = 44
            self.typespokemon = "Eau"
            self.attaque = 48
        elif nom == "Pikachu" :
            self.nomdupokemon = "Pikachu"
            self.pointsdevie = 35
            self.typespokemon = "Electrick"
            self.attaque = 55
    # Méthode pour choisir aléatoirement un Pokémon adverse
    # et attribution des attributs de ce pokémon
    def ChoixRandomPlayerOrdi(self):
        # On définit une liste de pokémons adversaires
        pokemonadversaire = ['Ponyta','Krabby','Voltorbe']
        # On choisit au hasard un pokémon
        choixadversaire = random.choice(pokemonadversaire)
        if choixadversaire == "Ponyta" :
            self.nomdupokemon = "Ponyta"
            self.pointsdevie = 40
            self.typespokemon = "Feu"
            self.attaque = 55
        elif choixadversaire == "Krabby" :
            self.nomdupokemon= "Krabby"
            self.pointsdevie = 48
            self.typespokemon = "Eau"
            self.attaque = 41
        elif choixadversaire == "Voltorbe" :
            self.nomdupokemon = "Voltorbe"
            self.pointsdevie = 40
            self.typespokemon = "Electrick"
            self.attaque = 52
    # Méthode pour calculer les avantages et faiblesses entre deux pokémons
    def AvantageFaiblesse(self,typeAtt,typeDef) :
        # Attaquant Eau
        if typeAtt == "Eau" :
            if typeDef == "Feu" :
                self.bonusattaque = 2
            elif typeDef == "Electrik" :
                self.bonusattaque = 1
            elif typeDef == "Eau" :
                self.bonusattaque = 0.5
        # Attaquant Feu
        if typeAtt == "Feu" :
            if typeDef == "Feu" :
                self.bonusattaque = 0.5
            elif typeDef == "Electrik" :
                self.bonusattaque = 1
            elif typeDef == "Eau" :
                self.bonusattaque = 0.5
        # Attaquant Electrik
        if typeAtt == "Electrik" :
            if typeDef == "Feu" :
                self.bonusattaque = 1
            elif typeDef == "Electrik" :
                self.bonusattaque = 0.5
            elif typeDef == "Eau" :
                self.bonusattaque = 2

# Classe du Jeu
class Game :
    def __init__(self) :
        # On instancie les attributs de la classe à des valeurs initiales
        self.round = 0
        self.PlayerActif = 0 # 0 = Joueur, 1 = Ordinateur
        self.QuiAtt = 0 # Qui attaque
        self.QuiDef = 1 # Qui défend
    # Méthode qui définit aléatoirement un joueur qui commence
    def PlayerStart(self):
        NombreJoueur = [0,1] # 0 = Joueur, 1 = Ordinateur
        self.PlayerActif = random.choice(NombreJoueur)
    # Méthode qui switch d'un joueur à l'autre l'attribut PlayerActif
    def ChangePlayerActif(self) :
        if self.PlayerActif == 0 :
            self.PlayerActif = 1
        elif self.PlayerActif == 1 :
            self.PlayerActif = 0
        return self.PlayerActif
    # Méthode d'attaque, return les dégats générés
    def Attaque(self,PointAttaquant,BonusAttaquant):
        return (random.randint(1,PointAttaquant)) * BonusAttaquant

print("Bienvenue sur le jeu Pokémon créé par Lilou ! Bon jeu !")
pokemon = int(input("Choisissez votre pokémon : tapez 0 pour Pyroli (Feu), 1 pour Carapuce (Eau), 2 pour Pikachu (Electrick) : "))
# On crée une instance de Pokémon qui sera le Joueur
Pok = Pokemon()
# On affecte le pokémon choisi
if pokemon == 0 :
    Pok.ChoixPlayerpokemon("Pyroli")
elif pokemon == 1 :
    Pok.ChoixPlayerpokemon("Carapuce")
elif pokemon == 2 :
    Pok.ChoixPlayerpokemon("Pikachu")
else :
    input("Invalide, saississez un pokémon entre 0 et 2")
    exit()
# On crée une instance de pokémon adverse (l'ordinateur)
PokOrdi = Pokemon()
# On choisit aléatoirement un Pokémon adverse
PokOrdi.ChoixRandomPlayerOrdi()

print("Votre pokémon est :",Pok.nomdupokemon,"avec",Pok.pointsdevie,"points de vie.")
print("Et votre adversaire est :",PokOrdi.nomdupokemon,"avec",PokOrdi.pointsdevie,"points de vie.")

# On calcule et met à jour les attributs des bonus de chaque joueur
Pok.AvantageFaiblesse(Pok.typespokemon,PokOrdi.typespokemon)
PokOrdi.AvantageFaiblesse(PokOrdi.typespokemon,Pok.typespokemon)

Jeux = Game()
# On choisit un joueur au hasard pour commencer
Jeux.PlayerStart()
# On affiche le joueur qui commence
if Jeux.PlayerActif == 0 :
    print(Pok.nomdupokemon ,"commence...")
else :
    print(PokOrdi.nomdupokemon , "commence...")

# Boucle du jeu
while (Pok.pointsdevie > 0 or PokOrdi.pointsdevie > 0):
    # On lance une attaque
    if Jeux.PlayerActif == 0 :
        print(Pok.nomdupokemon,"attaque...")
    else:
        print(PokOrdi.nomdupokemon,"attaque...")

    # Si le player joue
    if Jeux.PlayerActif == 0 :
        degat = Jeux.Attaque(Pok.attaque,Pok.bonusattaque)
        PokOrdi.pointsdevie -= degat
        print (PokOrdi.nomdupokemon,"a pris",degat, "il lui reste", PokOrdi.pointsdevie,"points de vie")
    # Si l'ordinateur joue
    elif Jeux.PlayerActif == 1 :
        degat = Jeux.Attaque(PokOrdi.attaque,PokOrdi.bonusattaque)
        Pok.pointsdevie -= degat
        print (Pok.nomdupokemon,"a pris",degat, "il vous reste", Pok.pointsdevie,"points de vie")
    if (Pok.pointsdevie <= 0 or PokOrdi.pointsdevie <= 0 ) :
        break
    Jeux.ChangePlayerActif()
    entree = input("Appuyez sur une touche pour continuer")
# Il y a un gagnant
if Pok.pointsdevie <= 0 :
    print(Pok.nomdupokemon, "est mort. Vous avez perdu !")
else :
    print(PokOrdi.nomdupokemon, "est mort. Bravo vous avez gagné !")