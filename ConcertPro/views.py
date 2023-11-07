import random
from flask import redirect, render_template, request, url_for
from .app import app, db
import datetime
from . import models as mo

IMAGES = ["banniere.jpeg", "logo-black.png", "logo-white.png", "test.png", "logo-no-background.png", "logo-color.png"]
ARTISTES = [{"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}, {"telephone": "0795351865", "mail": "nom@prenom.gmail.com", "nom_artiste": "a", "prenom_artiste": "b", "date_de_naissance": "10/10/2000", "lieu_de_naissance": "Orly", "adresse": "everglen", "securite_sociale": "non", "cni": "jsp", "date_delivrance_cni": "jamais", "date_expiration_cni": "toujours", "carte_reduction": "oui", "id_style_musique": 1}]
CONCERTS = [{"artiste": "Lucie", "date_debut": datetime.datetime.strptime("2023-10-26", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("10:00", "%H:%M").time(), "salle": "Bercy", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "yaaa", "heure_duree":2, "minute_duree":25, "jour":4}, {"artiste": "Mira", "date_debut": datetime.datetime.strptime("2023-10-24", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("8:30", "%H:%M").time(), "salle": "Bercy", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "test", "heure_duree":3, "minute_duree":00, "jour":1}, {"artiste": "Muse", "date_debut": datetime.datetime.strptime("2023-10-29", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("10:00", "%H:%M").time(), "salle": "Bercy", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 1", "heure_duree":1, "minute_duree":35, "jour":6}, {"artiste": "Daft Punk", "date_debut": datetime.datetime.strptime("2023-10-23", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("14:20", "%H:%M").time(), "salle": "Stade de France", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 2", "heure_duree":4, "minute_duree":00, "jour":1}, {"artiste": "Beyoncé", "date_debut": datetime.datetime.strptime("2023-10-24", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("11:00", "%H:%M").time(), "salle": "Madison Square Garden", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 3", "heure_duree":1, "minute_duree":30, "jour":4}, {"artiste": "The Beatles", "date_debut": datetime.datetime.strptime("2019-04-10", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("12:30", "%H:%M").time(), "salle": "Royal Albert Hall", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 4", "heure_duree":00, "minute_duree":45, "jour":1}, {"artiste": "Ed Sheeran", "date_debut": datetime.datetime.strptime("2019-05-05", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("9:00", "%H:%M").time(), "salle": "Wembley Stadium", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 5", "heure_duree":3, "minute_duree":30, "jour":3}, {"artiste": "Adele", "date_debut": datetime.datetime.strptime("2019-06-12", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("22:00", "%H:%M").time(), "salle": "The O2 Arena", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 6", "heure_duree":1, "minute_duree":25, "jour":7}, {"artiste": "Michael Jackson", "date_debut": datetime.datetime.strptime("2023-10-18", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("8:45", "%H:%M").time(), "salle": "Tokyo Dome", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 7", "heure_duree":2, "minute_duree":00, "jour":1}, {"artiste": "Taylor Swift", "date_debut": datetime.datetime.strptime("2019-08-25", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("15:30", "%H:%M").time(), "salle": "Arrowhead Stadium", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 8", "heure_duree":2, "minute_duree":25, "jour":3}, {"artiste": "Coldplay", "date_debut": datetime.datetime.strptime("2019-09-14", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("11:11", "%H:%M").time(), "salle": "Estadio Wanda Metropolitano", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 9", "heure_duree":5, "minute_duree":00, "jour":5}, {"artiste": "Kanye West", "date_debut": datetime.datetime.strptime("2023-10-23", "%Y-%m-%d"), "heure_debut": datetime.datetime.strptime("13:30", "%H:%M").time(), "salle": "American Airlines Center", "url": IMAGES[random.randint(0,len(IMAGES)-1)], "nom": "concert 10", "heure_duree":1, "minute_duree":30, "jour":2}]
SALLES = [{"nom": "Bercy", "nbPlaces": 130, "photo":"test.png"}, {"nom": "Stade de France", "nbPlaces": 80000, "photo":"test.png"}, {"nom": "Madison Square Garden", "nbPlaces": 20000, "photo":"test.png"}, {"nom": "Royal Albert Hall", "nbPlaces": 5000, "photo":"test.png"}, {"nom": "Wembley Stadium", "nbPlaces": 90000, "photo":"test.png"}, {"nom": "The O2 Arena", "nbPlaces": 20000, "photo":"test.png"}, {"nom": "Tokyo Dome", "nbPlaces": 55000, "photo":"test.png"}, {"nom": "Arrowhead Stadium", "nbPlaces": 80000, "photo":"test.png"}, {"nom": "Estadio Wanda Metropolitano", "nbPlaces": 68000, "photo":"test.png"}, {"nom": "American Airlines Center", "nbPlaces": 21000, "photo":"test.png"}]
LOGEMENTS = [{"nom_etablissement":"yaaaa", "adresse_ville_codepostal":"rue du yaaa", "nb_etoile": 3}]

HEURES1 = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
PAS1 = 1
HEURES2 = [8, 10, 12, 14, 16, 18, 20, 22]
PAS2 = 2
JOUR_VOULU = datetime.datetime.now() # -datetime.timedelta(days=7) ou +datetime.timedelta(days=7) --> pour changer de semaine (- ou + 1 semaine)

# accueil
@app.route('/')
def accueil():
    """page d'accueil"""
    heures = HEURES2
    pas = PAS2
    jour = JOUR_VOULU
    agenda = concerts_agenda(heures, pas)
    lundi = (jour + datetime.timedelta(days=-(jour.weekday()+1)) + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    dimanche = (jour + datetime.timedelta(days=7-(jour.weekday()+1))).replace(hour=23, minute=59, second=59, microsecond=0)
    return render_template(
        "accueil.html",
        concerts=mo.prochains_concerts(),
        agenda=agenda,
        heures=heures,
        date_lundi=lundi.strftime("%d-%m-%Y"),
        date_dimanche=dimanche.strftime("%d-%m-%Y")
    )
    
@app.template_filter('str')
def string_filter(value):
    return str(value)

# concert
@app.route('/creer_concert')
def creer_concert():
    """page de création de concert"""
    return render_template(
        "creer_concert.html",
        artistes=mo.artistes(),
        salles=mo.salles()
    )

@app.route('/voir_prochains_concerts')
def voir_prochains_concerts():
    """page qui affiche les concerts à venir"""
    return render_template(
        "voir_prochains_concerts.html",
        concerts=mo.prochains_concerts()
    )
    

@app.route('/historique_concert')
def historique_concerts():
    """page qui affiche les concerts passés"""
    return render_template(
        "historique_concerts.html",
        concerts = mo.historique_concerts()
    )

@app.route('/save_concert1', methods=("POST",))
def save_concert1():
    """sauvegarde d'un concert"""
    concert = {}
    concert["artiste"] = request.form['artiste']
    concert["date_debut"] = datetime.datetime.strptime(request.form['date_debut'], "%Y-%m-%d")
    concert["salle"] = request.form['salle']
    concert["nom"] = request.form['titre']
    concert["heure_debut"] = datetime.datetime.strptime(request.form['heure_debut'], "%H:%M").time()
    concert["heure_duree"] = datetime.datetime.strptime(request.form['duree'], "%H:%M").time().hour
    concert["minute_duree"] = datetime.datetime.strptime(request.form['duree'], "%H:%M").time().minute
    concert["jour"] = 7
    concert["url"] = "test.png"
    CONCERTS.append(concert)
    return redirect(url_for('concert', nom=concert["nom"]))

@app.route('/save_concert', methods=("POST",))
def save_concert():
    """sauvegarde d'un concert"""
    nom_concert = request.form['titre']
    date_debut = datetime.datetime.strptime(request.form['date_debut'], "%Y-%m-%d")
    heure_debut = datetime.datetime.strptime(request.form['heure_debut'], "%H:%M").time()
    date_heure_concert = datetime.datetime.combine(date_debut, heure_debut)
    heure_duree = datetime.datetime.strptime(request.form['duree'], "%H:%M").time().hour
    minute_duree = datetime.datetime.strptime(request.form['duree'], "%H:%M").time().minute
    duree_concert = heure_duree*60 + minute_duree
    id_artiste = mo.get_artiste(request.form['artiste'])[0]
    id_salle = mo.get_salle(request.form['salle'])[0]
    description_concert = request.form['description']
    photo = "test.png"
    try:
        cursor = mo.get_cursor()
        req = "INSERT INTO Concert (id_concert, nom_concert, date_heure_concert, duree_concert, id_artiste, id_salle, description_concert, photo) VALUES("+str(get_id_concert_max()+1)+", '" + str(nom_concert) + "', '" + str(date_heure_concert) + "', " + str(duree_concert) + ", " + str(id_artiste) + ", " + str(id_salle) + ", '" + str(description_concert) + "', '" + str(photo) + "')"
        cursor.execute(req)
        mo.db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)
    return redirect(url_for('concert', nom=nom_concert))

@app.route('/concert/<nom>')
def concert(nom):
    """page pour le concert <nom>"""
    concert = mo.get_concert(nom)
    return render_template(
        "concert.html",
        concert=concert
    )

@app.route('/concert/<nom>/supprimer')
def supprimer_concert(nom):
    """supprime le concert <nom>"""
    remove_concert(nom)
    return redirect(url_for('accueil'))

# salle
@app.route('/ajout_nouvelle_salle')
def ajout_nouvelle_salle():
    """page de création de salle"""
    return render_template(
        "ajout_nouvelle_salle.html"
    )

@app.route('/voir_salles')
def voir_salles():
    """page qui affiche les salles"""
    try:
        cursor = mo.get_cursor()
        request = "SELECT * FROM Salle"
        cursor.execute(request)
        info = cursor.fetchall()
        mo.close_cursor(cursor)
        return render_template(
            "voir_salles.html",
            salles=info
        )
    except Exception as e:
        print(e.args)
        return render_template(
            "error.html",
            error_message="An error occurred while retrieving data from the database."
        )

@app.route('/salle/<nom>')
def salle(nom):
    """page pour la salle <nom>"""
    salle = mo.get_salle(nom)
    return render_template(
        "salle.html",
        salle=salle
    )

@app.route('/save_salle', methods=("POST",))
def save_salle():
    """sauvegarde d'une salle"""
    nom_salle = request.form['titre']
    nb_places = request.form['place']
    profondeur_scene = request.form['profondeur']
    longueur_scene = request.form['longueur']
    description_salle = request.form['description']
    adresse_salle = request.form['adresse']
    telephone_salle = request.form['telephone']
    adresse_salle = request.form['adresse']
    code_postal_salle = request.form['code_postal']
    photo = "test.png"
    adresse_salle = adresse_salle + ", " + code_postal_salle
    if request.form['loge']:
        loge = "oui"
    else:
        loge = "non"
    try:
        cursor = mo.get_cursor()
        req = "INSERT INTO Salle (id_salle, id_type_salle, loge, nom_salle, nb_places, prfondeur_scene, longueur_scene, description_salle,adresse_salle,telephone_salle,photo_salle) VALUES("+str(get_id_salle_max()+1) + ", '" + str(loge) + ", '" + str(nom_salle) + "', '" + str(nb_places) + "', " + str(profondeur_scene) + ", " + str(longueur_scene) + ", " + str(description_salle) + ", '" + str(adresse_salle) + "', '" + str(telephone_salle) + "', '" +  str(photo) + "')"
        cursor.execute(req)
        mo.db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)
    return redirect(url_for('concert', nom=nom_salle))
@app.route('/salle/<nom>/supprimer')
def supprimer_salle(nom):
    """supprime la salle <nom>"""
    remove_salle(nom)
    return redirect(url_for('accueil'))

# artiste
@app.route('/ajout_artiste')
def ajout_artiste():
    """page d'ajout d'un artiste"""
    return render_template(
        "ajout_artiste.html"
    )

@app.route('/voir_artistes')
def voir_artistes():
    try:
        cursor = mo.get_cursor()
        request = "SELECT * FROM Artiste"
        cursor.execute(request)
        info = cursor.fetchall()
        mo.close_cursor(cursor)
        return render_template(
            "voir_artistes.html",
            artistes=info
        )
    except Exception as e:
        print(e.args)
        return render_template(
            "error.html",
            error_message="An error occurred while retrieving data from the database."
        )


@app.route('/artiste/<nom_artiste>')
def artiste(nom_artiste):
    """page de l'artiste <nom_artiste>"""
    artiste = mo.get_artiste(nom_artiste)
    return render_template(
        "artiste.html",
        artiste=artiste
    )

@app.route('/save_artiste1', methods=("POST",))
def save_artiste1():
    """sauvegarde d'un artiste"""
    artiste = {}
    artiste["nom_artiste"] = request.form['nom']
    artiste["prenom_artiste"] = request.form['prenom']
    artiste["mail"] = request.form['mail']
    artiste["telephone"] = request.form['telephone']
    artiste["date_de_naissance"] = request.form['date_naissance']
    artiste["lieu_de_naissance"] = request.form['lieu_naissance']
    artiste["adresse"] = request.form['adresse']
    artiste["securite_sociale"] = request.form['num_secu_sociale']
    artiste["cni"] = request.form['cni']
    artiste["date_delivrance_cni"] = request.form['date_delivrance']
    artiste["date_expiration_cni"] = request.form['date_expiration']
    artiste["carte_reduction"] = request.form['carte_train']
    ARTISTES.append(artiste)
    return redirect(url_for('artiste', nom=artiste["nom_artiste"]))

@app.route('/save_artiste', methods=("POST",))
def save_artiste():
    """sauvegarde d'un artiste"""
    nom_artiste = request.form['nom']
    prenom_artiste = request.form['prenom']
    mail = request.form['mail']
    telephone = request.form['telephone']
    date_de_naissance = datetime.datetime.strptime(request.form['date_naissance'], "%Y-%m-%d")
    lieu_de_naissance = request.form['lieu_naissance']
    adresse = request.form['adresse']
    securite_sociale = request.form['num_secu_sociale']
    cni = request.form['cni']
    date_delivrance_cni = datetime.datetime.strptime(request.form['date_delivrance'], "%Y-%m-%d")
    date_expiration_cni = datetime.datetime.strptime(request.form['date_expiration'], "%Y-%m-%d")
    carte_reduction = request.form['carte_train']
    try:
        req = "INSERT INTO Artiste (id_artiste, nom_artiste, prenom_artiste, mail, telephone, date_de_naissance, lieu_naissance, adresse, securite_social, cni, date_delivrance_cni, date_expiration_cni, carte_reduction) VALUES("+str(get_id_artiste_max()+1)+", '" + str(nom_artiste) + "', '" + str(prenom_artiste) + "', '" + str(mail) + "', '" + str(telephone) + "', '" + str(date_de_naissance) + "', '" + str(lieu_de_naissance) + "', '" + str(adresse) + "', '" + str(securite_sociale) + "', '" + str(cni) + "', '" + str(date_delivrance_cni) + "', '" + str(date_expiration_cni) + "', '" + str(carte_reduction) + "')"
        cursor.execute(req)
        db.commit()
    except Exception as e:
        print(e.args)
    return redirect(url_for('artiste', nom_artiste=nom_artiste))

@app.route('/artiste/<nom_artiste>/supprimer')
def supprimer_artiste(nom_artiste):
    """supprime l'artiste <nom_artiste>"""
    remove_artiste(nom_artiste)
    return redirect(url_for('accueil'))

# logement
@app.route('/logement/<nom_etablissement>')
def logement(nom_etablissement):
    """page du logement <nom_etablissement>"""
    logement = mo.get_logement(nom_etablissement)
    return render_template(
        "logement.html",
        logement=logement
    )

@app.route('/ajout_logement')
def ajout_logement():
    """page d'ajout de logement"""
    return render_template(
        "ajout_logement.html"
    )

@app.route('/voir_logements')
def voir_logements():
    try:
        cursor = mo.get_cursor()
        request = "SELECT * FROM Logement"
        cursor.execute(request)
        info = cursor.fetchall()
        mo.close_cursor(cursor)
        return render_template(
            "voir_logements.html",
            logements=info
        )
    except Exception as e:
        print(e.args)
        return render_template(
            "error.html",
            error_message="An error occurred while retrieving data from the database."
    )

@app.route('/save_logement', methods=("POST",))
def save_logement():
    """sauvegarde d'un logement"""
    logement = {}
    logement["nom_etablissement"] = request.form['Entrer_nometablissement']
    logement["adresse_ville_codepostal"] = request.form['Entrer_adresse']
    logement["nb_etoile"] = request.form['Entrer_nbetoiles']
    LOGEMENTS.append(logement)
    return redirect(url_for('logement', nom_etablissement=logement["nom_etablissement"]))

@app.route('/logement/<nom_etablissement>/supprimer')
def supprimer_logement(nom_etablissement):
    """supprime le logement >nom_etablissement>"""
    remove_logement(nom_etablissement)
    return redirect(url_for('accueil'))

# calendrier
@app.route('/calendrier/<jour>')
def calendrier(jour=JOUR_VOULU):
    """page du calendrier au jour <jour>"""
    heures = HEURES1
    pas = PAS1
    if type(jour) == str:
        jour = datetime.datetime.strptime(jour, "%d-%m-%Y")
    agenda = concerts_agenda(heures, pas, jour)
    lundi = (jour + datetime.timedelta(days=-(jour.weekday()+1)) + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    dimanche = (jour + datetime.timedelta(days=7-(jour.weekday()+1))).replace(hour=23, minute=59, second=59, microsecond=0)
    return render_template(
        "calendrier.html",
        concerts=mo.prochains_concerts(),
        agenda=agenda,
        heures=heures,
        date_lundi=lundi.strftime("%d-%m-%Y"),
        date_dimanche=dimanche.strftime("%d-%m-%Y")
    )

@app.route('/calendrier/redirection', methods=("POST",))
def calendrier_redirection():
    """redirige vers le calendrier du jour"""
    jour = datetime.datetime.strptime(request.form['date'], "%Y-%m-%d")
    return redirect(url_for('calendrier', jour=jour.strftime("%d-%m-%Y")))

@app.route('/calendrier/semaine_precedente/<jour_actuel>')
def calendrier_semaine_precedente(jour_actuel=JOUR_VOULU):
    """page du calendrier de la semaine précédent <jour_actuel>"""
    if type(jour_actuel) == str:
        jour_actuel = datetime.datetime.strptime(jour_actuel, "%d-%m-%Y")
    jour = jour_actuel + datetime.timedelta(days=-7)
    return redirect(url_for('calendrier', jour=jour.strftime("%d-%m-%Y")))

@app.route('/calendrier/semaine_suivante/<jour_actuel>')
def calendrier_semaine_suivante(jour_actuel=JOUR_VOULU):
    """page du calendrier de la semaine suivant <jour_actuel>"""
    if type(jour_actuel) == str:
        jour_actuel = datetime.datetime.strptime(jour_actuel, "%d-%m-%Y")
    jour = jour_actuel + datetime.timedelta(days=7)
    return redirect(url_for('calendrier', jour=jour.strftime("%d-%m-%Y")))

def remove_concert(nom):
    concert = mo.get_concert(nom)
    try:
        cursor = mo.get_cursor()
        req = "DELETE FROM Concert where id_concert="+str(concert[0])
        cursor.execute(req)
        db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)

def remove_salle(nom):
    salle = mo.get_salle(nom)
    try:
        cursor = mo.get_cursor()
        req = "DELETE FROM Salle where id_salle="+str(salle[0])
        cursor.execute(req)
        db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)

def remove_logement(nom_etablissement):
    logement = mo.get_logement(nom_etablissement)
    try:
        cursor = mo.get_cursor()
        req = "DELETE FROM Logement where id_logement="+str(logement[0])
        cursor.execute(req)
        db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)

def remove_artiste(nom):
    artiste = mo.get_artiste(nom)
    try:
        cursor = mo.get_cursor()
        req = "DELETE FROM Artiste where id_artiste="+str(artiste[0])
        cursor.execute(req)
        db.commit()
        mo.close_cursor(cursor)
    except Exception as e:
        print(e.args)

def concerts_agenda(heures=HEURES1,pas=PAS1,jour_voulu=JOUR_VOULU):
    """renvoie un agenda des concerts de la semaine du jour voulu"""
    #initialisation de l'agenda
    agenda = {}
    for i in range(1,8):
        agenda[i] = {}
        for heure in heures:
            agenda[i][heure] = []
    #remplissage de l'agenda
    jour = jour_voulu
    if type(jour) == str:
        jour = datetime.datetime.strptime(jour, "%d-%m-%Y")
    for concert in mo.concerts():
        # if datetime.timedelta(days=-(jour.weekday()+1))<concert["date_debut"]-jour<datetime.timedelta(days=7-(jour.weekday()+1)+1):
        #     for h in heures:
        #         fin_horaire = h+pas
        #         # format 24h obligatoire
        #         if fin_horaire > 23:
        #             fin_horaire = datetime.time(hour=h+pas-1, minute=59)
        #         else:
        #             fin_horaire = datetime.time(hour=h+pas)
        #         debut_horaire = datetime.time(hour=h)
        #         minutesC = (concert["heure_debut"].minute+concert["minute_duree"])%60
        #         heuresC = concert["heure_debut"].hour+concert["heure_duree"]+(concert["heure_debut"].minute+concert["minute_duree"])//60
        #         fin_concert = datetime.time(hour=heuresC, minute=minutesC)
        #         debut_concert = concert["heure_debut"]
        #         # ajouter le concert si il est dans l'intervalle horaire
        #         if not(debut_concert >= fin_horaire or fin_concert <= debut_horaire):
        #             agenda[concert["date_debut"].weekday()+1][h].append(concert["nom"])
        pass
    return agenda
