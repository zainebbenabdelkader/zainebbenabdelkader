import json

contacts = {}

def show_Contact(dict, name):
    names = [key.lower() for key in dict.keys()]
    name = name.lower()
    if name in names:
        print(f"Les numéros associés à {name} sont {dict[name]}")
    else:
        print("Ce contact n'existe pas.")

def add_Contact(dict, name, number):
    name = name.lower()
    if name in dict:
        print("Ce contact existe déjà.")
    else:
        dict[name] = [number]
        print(f"Le contact {name} avec le numéro {number} a été ajouté avec succès.")

def delete_contact(filename, name):
    confirm = input(f"Êtes-vous sûr de vouloir supprimer le contact '{name}' ? (Oui/Non) ")
    name = name.lower()
    if confirm.lower() in ("oui", "o"):
        with open(filename, 'r') as file:
            contacts = json.load(file)

        if name in contacts:
            del contacts[name] 
            with open(filename, 'w') as file:
                json.dump(contacts, file, indent=4)  

            print(f"Le contact '{name}' a été supprimé avec succès.")
        else:
            print(f"Le contact '{name}' n'existe pas.")
    else:
        print("Suppression annulée.") 

def saveRep(contact, filename):
    with open(filename, "w") as repfile:
        json.dump(contact, repfile)
    print("Sauvegarde effectuée avec succès.")

etat = True
while etat:
    print("choisir:")
    print("1- Afficher toute la répertoire")
    print("2- Ajouter un nouveau contact")
    print("3- Afficher le numéro d'un contact")
    print("4- Supprimer un numéro")
    print("5- Sauvegarder la répertoire")
    print("6- Quitter")
    
    choix = input("Entrez votre choix: ")
    filename = "contact.json"
    match choix:
        case "1":
            print("La liste de tous les contacts est :")
            print(contacts)
           
        case "2":
            name = input("Entrez le nom du nouveau contact : ")
            number = input("Entrez le numéro du nouveau contact : ")
            add_Contact(contacts, name, number)
        case "3":
            name = input("entrez le nom du contact que vous voulez : ")
            show_Contact(contacts, name)
        case "4":
          
            name = input("Entrez le nom du contact que vous voulez supprimer : ")
            delete_contact(filename, name)
        case "5":
            
            saveRep(contacts, filename)
        case "6":
            etat = False
            print("bye bye")
        case _:
            print("Choix invalide, veuillez réessayer.")
