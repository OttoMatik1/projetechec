#fonction qui détermine si une pièce est capturable lors d'un mouvement: 



def est_capturable(echiquier, depart, arrivee):
    piece_depart = echiquier[depart[0]][depart[1]]
    piece_arrivee = echiquier[arrivee[0]][arrivee[1]]
    if piece_arrivee is None:
        return False
    elif piece_depart.couleur != piece_arrivee.couleur:
        return True
    else:
        return False
        
def capture_piece(self, position):
    piece = self.obtenir_piece(position)
    if piece is None:
        return "Aucune pièce à cette position"
    else:
        self.echiquier[position[0]][position[1]] = None
        return "La pièce a été capturée avec succès"


#pour mettre à jour le jeu:

def mettre_a_jour_jeu(self, position_depart, position_arrivee):
    piece_depart = self.obtenir_piece(position_depart)
    piece_arrivee = self.obtenir_piece(position_arrivee)
    
    # Vérifier si la case d'arrivée est vide ou si la pièce sur la case d'arrivée est de couleur différente
    if piece_arrivee is None or piece_arrivee.couleur != piece_depart.couleur:
        # Vérifier si le déplacement est autorisé pour la pièce
        if position_arrivee in self.piecemouvementpossible(position_depart):
            # Déplacer la pièce
            self.echiquier[position_depart[0]][position_depart[1]] = None
            self.echiquier[position_arrivee[0]][position_arrivee[1]] = piece_depart
            
            # Capturer la pièce si nécessaire
            if piece_arrivee is not None:
                # Ajouter la pièce capturée à la liste des pièces capturées du joueur adverse
                if piece_arrivee.couleur == 'blanc':
                    self.piece_capturee_noir.append(piece_arrivee)
                else:
                    self.piece_capturee_blanc.append(piece_arrivee)
            
            # Changer le tour du joueur
            if self.tour == 'blanc':
                self.tour = 'noir'
            else:
                self.tour = 'blanc'
                
            print("Déplacement effectué avec succès !")
        else:
            print("Déplacement non autorisé pour cette pièce !")
    else:
        print("Impossible de capturer une pièce de même couleur !")









#ENREGISTER L'ÉTAT DE L'ÉCHIQUIER

def sauvegarder_etat_echiquier(echiquier):
    etat_echiquier = []

    for ligne in echiquier:
        ligne_echiquier = []
        for piece in ligne:
            if piece:
                ligne_echiquier.append((piece.couleur, piece.symbole))
            else:
                ligne_echiquier.append(None)
        etat_echiquier.append(ligne_echiquier)

    return etat_echiquier


#EXEMPLE:

def sauvegarder_etat_echiquier(echiquier):
    etat_echiquier = []

    for ligne in echiquier:
        ligne_echiquier = []
        for piece in ligne:
            if piece:
                ligne_echiquier.append((piece.couleur, piece.symbole))
            else:
                ligne_echiquier.append(None)
        etat_echiquier.append(ligne_echiquier)

    return etat_echiquier
