#Souhail Daoudi
#Anis Rahmouni El idrissi

def effaceTableau (tab):
   
   ''' (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   tableau2=[['-','-','-'],['-','-','-'],['-','-','-']]
   i=0
   while i<len(tab):
       j=0
       while j<len(tab[i]):
           tab[i][j]=tableau2[i][j]
           j=j+1
       i=i+1
       
def verifieGagner(tab):
   
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''
    
    varr='non' #on initialise la variable: varr='non' (dans ce cas pas de gagnant)
    
    a=testLignes(tab)
    # 'a' est le return de la fonction testLignes(tab)
    if a=='X':
      print("le joueur 'x'a gagner")
      varr='oui'
      return True
    elif a =='O':
       print("le joueur 'o'a gagner")
       varr='oui'
       return True
      
    b=testCols(tab)
    # 'b' est le return de la fonction testCols(tab)
    if b=='X':
      print("le joueur 'x'a gagner")
      varr='oui'
      return True
    elif b =='O':
       print("le joueur 'o'a gagner")
       varr='oui'
       return True
      
    c=testDiags(tab)
    #'c' est le return de la fonction testDiags(tab)
    if c=='X':
       print("le joueur 'x'a gagner")
       varr='oui'
       return True
    elif c=='O':
     print("le joueur 'o'a gagner")
     varr='oui'
     return True
    #d est le return de la fonction testMatchNul(tab)
   
    d=testMatchNul(tab)
    if d==True :
     varr='oui'
     print("le match est nul")
     return True
   
    if varr=='non':#var=='non' -> pas de gagnant et pas de match nul donc le jeu n'est pas fini
     return False
   
def testLignes(tab):
   
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''
   
   i=0
   j=0
   varr='non'#on initialise la variable varr='non'(dans ce cas pas de gagnant)
   while True:
      
         if tab[i][j]==tab[i][j+1] and tab[i][j+1]==tab[i][j+2]and tab[i][j]=="X":#ligne de 'x'
           varr='oui'
           return 'X'
         
         elif tab[i][j]==tab[i][j+1] and tab[i][j+1]==tab[i][j+2]and tab[i][j]=="O" :#ligne de 'o'
            varr='oui'
            return 'O'
         i=i+1
         
         if i==3:  #si  i==len(matrrice)=3 on stop la fonction while
          break
   if varr=='non': #pas de ligne de 'x' ou de 'o'
      return '-'
   
def testCols(tab):
   
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   i=0
   j=0
   varr='non' #on initialise la variable varr='non'(dans ce cas pas de gagnant)
   while True:
      
      if tab[j][i]==tab[j+1][i] and tab [j+1][i]==tab[j+2][i] and tab[j][i]=="X":   #colonne de 'x'
        varr='oui'
        return 'X'
      
      elif tab[j][i]==tab[j+1][i] and tab [j+1][i]==tab[j+2][i] and tab[j][i]=="O": #colonne de 'o'
        varr='oui'
        return 'O'
      i=i+1
      
      if i==3:#si  i==len(matrrice)=3 on stop la fonction while
         break
   if varr=='non':# pas de colonnes de 'x' ou de 'o'
    return '-'
   
def testDiags(tab):
   
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   i=0
   j=0
   k=2
   varr='non' #on initialise la variable varr='non'(dans ce cas pas de gagnant)
   while True:
         if tab[i][j]==tab[i+1][j+1] and tab[i+1][j+1]==tab[i+2][j+2] and tab[i][j]=="X":#diagonale gauche de 'x'
              varr='oui'
              return 'X'
            
         elif tab[i][j]==tab[i+1][j+1] and tab[i+1][j+1]==tab[i+2][j+2]and tab[i][j]=="O":#diagonale gauche de 'o'
            varr='oui'
            return 'O'
         
         elif tab[i][k]==tab[i+1][j+1] and tab[i][k]==tab[k][i] and tab[i][k]=="X":#diagonale droite de 'x'
            varr='oui'
            return 'X'
         elif tab[i][k]==tab[i+1][j+1] and tab[i][k]==tab[k][i] and tab[i][k]=="O":#diagonale droite de 'o'
            varr='oui' 
            return 'O'
         
         if varr=='non':#pas de diagonales de 'x' ou 'o'
           return '-'
       
def testMatchNul(tab):
   
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   
   i=0
   while i<len(tab):
      j=0
      while j<len(tab[i]):
         if tab[i][j]=="-": #si le jeu n'est pas fini retourne False
            return False
         j=j+1   
      i=i+1
   return True
         
