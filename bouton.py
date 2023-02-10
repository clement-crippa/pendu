import pygame


class Bouton():
    def __init__(self, x, y, image, echelle):
        largeur = image.get_width()
        hauteur = image.get_height()
        # Permet de changer l'échelle de l'image 1 = par défaut
        self.image = pygame.transform.scale(image, (int(largeur * echelle), int(hauteur * echelle)))
        self.rect = self.image.get_rect()
        # Place l'image par rapport à son coin haut gauche
        self.rect.topleft = (x, y)
        # Bouton non appuyé
        self.clique = False

    def afficher_bouton(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # Si on appuie sur le bouton active l'action
            if pygame.mouse.get_pressed()[0] == 1:
                self.clique = True
            elif pygame.mouse.get_pressed()[1] == 0:
                self.clique = False
        # Affiche le bouton sur la fenêtre voulu
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

