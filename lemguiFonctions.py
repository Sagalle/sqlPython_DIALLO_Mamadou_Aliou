import mysql.connector as ms

#****************************** Dictionnaire du Menu ***********************************
requeteDict ={
    "1": "1) Lister les tous les agences",
    "2": "2) Lister tous les caissiers par ordre croissant de leur nom",
    "3": "3) Lister tous chef d’agence ainsi que le nom de l’agence",
    "4": "4) Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
    "5": "5) Lister la somme des montants déposés par un caissier dans un compte de transactionde l’agence dont le chef est moussa dop par ordre croissant du montant",
    "6": "6) Lister les utilisateurs de l’agence Plateau",
    "7": "7) Lister le nombre de compte par agence",
    "8": "8) Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
    "9": "9) Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
    "10": "10) Lister le montant des transactions effectué par utilisateur et par date dans l’agencedont le numéro est 001",
    "11": "11) Lister le nombre d’affectation par utilisateur et numéro de compte durant le premiertrimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agencedont le numéro est 001",
    "12": "12) Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussadiop par ordre croissant du montant",
    "13": "13) Lister les montants de transactions et les frais associés effectués par l’utilisateurAssane Faye dans l’agence dont le chef est moussa diop .",
    "14": "14) Lister la somme des parts de l’agence, de l'état et de l’état des transactions par datedans l’agence dont le numéro est 001.",
    "15": "15) Lister la somme des parts de l’agence et de l'état par agence durant deuxième del’année 2021",
    "16": "16) Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
    "17": "17) Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
    "18": "18) Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
    "19": "19) Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
    "20": "20) Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
    "21": "21) Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 2021",
    "22": "22) Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
    "23": "23) Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
    "e": "E) Historique",
    "q": "Q) Quitter"
}


#********************* Menu et Historique **********************************
def Menu():
    print("=============== MENU PRINCIPAL=====================")
    for key in requeteDict.keys():
        print(requeteDict[key])
        
historiqueDict ={}  
def historiqueMenu():
    print("==============HISTORIQUE DES CHOIX==================")
    
    for hkey in historiqueDict.keys():
        print(historiqueDict[hkey])
    

            


#**********************Parametre des requetes SQL *****************************
params ={
    "host": "localhost",
    "user": "aliousagalle",
    "password": "aliousagalle",
    "database": "DB_LemGUI"
}

def fetchFonction(x):
    with ms.connect(**params) as db:
        with db.cursor() as c:
            c.execute(x)
            result = c.fetchall()
            for elm in range(len(result)):
                print(result[elm])


    
#***************** Fonction contenant les requetes SQL *******************************
def requeteFonction(x):
    requeteDicts ={
        "1": fetchFonction("select adresse_AGENCE from AGENCE"),
        "2": fetchFonction("select nom_USER from USERS join PROFIL on (id_PROFIL_PROFIL = id_PROFIL) where libelle_PROFIL = 'caissier' order by nom_USER"),
        "3": fetchFonction("select nom_USER,libelle_PROFIL,adresse_AGENCE  from USERS,PROFIL,AGENCE where id_USER_USER = id_USER and id_PROFIL = id_PROFIL_PROFIL and libelle_PROFIL ='chef agence'"),
        "4": fetchFonction("select numero,solde_COMPTE_TRANSACTION,adresse_AGENCE from COMPTE_TRANSACTION,AGENCE,USERS where id_USER = numero_AGENCE and adresse_AGENCE = '5 Nova Road'order by solde_COMPTE_TRANSACTION"),
    }
    requeteDicts[x]
    
    
#**************** Choix du Menu et de l'historique  *******************
def historiquechoices():
    h = input("Revenir sur un choix déjas fait:")
    for hkey in range(1,len(requeteDict) + 1):
        hk = str(hkey)
        if hk == h:
            requeteFonction(h)
            Menu()
            choices() 
  
def choices():
    c = input("Faites un choix: ")
    if c == "e":
        historiqueMenu()
        historiquechoices()
    elif c == "q":
        print("AU REVOIR !!!!!!!!!!!!!!!")
    else:
        for key in range(1,len(requeteDict) + 1):
                k = str(key)
                if k == c:
                    historiqueDict[c] = requeteDict[c]
                    del requeteDict[c]
                    requeteFonction(c)
                    Menu()
                    choices()
                else:
                    print("Votre choix est incorrect Veuillez en faire un autre........")
                    choices()