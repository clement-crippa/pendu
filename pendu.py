# Import sys optionnel il évite des erreurs console
import sys
import pygame
import random
from bouton import Bouton

pygame.init()

# Taille de la fenêtre
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jeu du pendu')
Icone = pygame.image.load('img/icone.png')
pygame.display.set_icon(Icone)

# Charge le fichier des mots
with open('mots.txt', 'r') as f:
    mots = f.readlines()
# Images des boutons
jouer_image = pygame.image.load("img/bouton/Jouer.png")
ajouter_image = pygame.image.load("img/bouton/Ajouter.png")
# Emplacement des boutons
jouer_bouton = Bouton(280, 160, jouer_image, 1)
ajouter_bouton = Bouton(280, 320, ajouter_image, 1)


# Menu principal
def menu():
    while True:
        fenetre.fill((255, 255, 255))
        jouer_bouton.afficher_bouton(fenetre)
        ajouter_bouton.afficher_bouton(fenetre)
        for clique in pygame.event.get():
            # Permet de fermer le programme
            if clique.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Permet de lancer une partie
            elif jouer_bouton.clique:
                jouer()
            # Permet d'ajouter un mot
            elif ajouter_bouton.clique:
                ajouter_mot()

        # Affiche le menu principal
        pygame.display.update()


def ajouter_mot():
    # Permet à l'utilisateur d'ajouter un mot
    texte_police = pygame.font.Font(None, 36)
    texte = texte_police.render("Écrivez un mot pour l'ajouter puis validé avec la touche enter:", True, (0, 0, 0))
    fenetre.blit(texte, (50, 420))
    pygame.display.update()

    # Ajoute le mot dans le fichier txt
    mot = ''
    while True:
        for touche_appuie in pygame.event.get():
            if touche_appuie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif touche_appuie.type == pygame.KEYDOWN:
                if touche_appuie.unicode.isalpha() or touche_appuie.unicode == ' ':
                    mot += touche_appuie.unicode
                elif touche_appuie.key == pygame.K_RETURN:
                    with open('mots.txt', 'a') as z:
                        z.write(mot + '\n')
                    menu()
        texte_police = pygame.font.Font(None, 36)
        texte = texte_police.render(mot, True, (0, 0, 0))
        fenetre.blit(texte, (350, 450))
        pygame.display.update()


# Partie de pendue
def jouer():
    # Met a jour les mots si des nouveaux on était ajouté
    with open('mots.txt', 'r') as f:
        mots = f.readlines()

    # Choix d'un mot aleatoire
    mot = random.choice(mots).strip()

    lettres_devinees = ['_' for l in mot]
    nombre_de_fautes = 1

    # Affichage du pendu
    images = [pygame.image.load(f"img/pendu_{i}.png") for i in range(8)]
    # Partie en cours
    while True:
        for touche_appuie in pygame.event.get():
            if touche_appuie.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Lettre jouée par l'utilisateur en appuyant sur le clavier
            elif touche_appuie.type == pygame.KEYDOWN:
                if touche_appuie.unicode.isalpha():
                    lettre = touche_appuie.unicode
                    if lettre in mot:
                        for i, l in enumerate(mot):
                            if l == lettre:
                                lettres_devinees[i] = lettre
                    # +1 faute si la lettre n'est pas dans le mot
                    else:
                        nombre_de_fautes += 1

        # Affichage de la partie
        fenetre.fill((255, 255, 255))
        texte_police = pygame.font.Font(None, 36)
        texte = texte_police.render(' '.join(lettres_devinees), True, (0, 0, 0))
        fenetre.blit(texte, (200, 100))
        if nombre_de_fautes > 0:
            fenetre.blit(images[nombre_de_fautes - 1], (470, 295))
        # Fin de partie
        if nombre_de_fautes == 8:
            texte_police = pygame.font.Font(None, 72)
            texte_police_mot = pygame.font.Font(None, 40)
            texte = texte_police.render("Perdu!", True, (255, 0, 0))
            fenetre.blit(texte, (300, 500))
            texte = texte_police_mot.render("Le mot était : " + mot, True, (0, 0, 0))
            fenetre.blit(texte, (200, 50))
        pygame.display.update()
        # Partie gagne
        if '_' not in lettres_devinees:
            image_victoire = pygame.image.load("img/pendu_victoire.png")
            fenetre.blit(image_victoire, (450, 200))
            texte_police = pygame.font.Font(None, 72)
            texte = texte_police.render("Gagné!", True, (0, 255, 0))
            fenetre.blit(texte, (300, 500))
            pygame.display.update()
            pygame.time.wait(5000)
            break
        # Partie perdue
        elif nombre_de_fautes == 8:
            pygame.display.update()
            pygame.time.wait(5000)
            break


# Affiche le menu principal au lancement du programme
menu()
