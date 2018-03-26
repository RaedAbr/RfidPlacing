# RfidPlacing

Ce projet consiste en une aide au placement d'objets et meubles dans un espace, qui peut être une salle ou un bâtiment.
Un tag NFC est placé sur chaque objet concerné. L'objet pourra être scanné avec un téléphone Android par NFC. 
Lorsqu'un objet sera scanné, l'utilisateur recevra une information sur son téléphone sur l'endroit où il doit placer 
l'objet.

Techniquement, le projet est divisé en 2 parties au minimum : une application Android qui va lire le tag NFC et envoyer 
l'identifiant unique de l'objet scanné à un serveur REST distant (réalisé en Python avec Flask) qui va retourner l'information 
sur le placement de l'objet. Les informations de placement seront stockées dans une base de données SQLite.

Au minimum, les fonctionnalités suivantes seront proposées :
- Scan d'un tag avec l'application Android, soit pour enregistrer un nouvel objet, soit pour obtenir son emplacement
- Plan de la salle/espace inscrit "en dur" en base de données
- Information textuelle retournée par le serveur à l'application au sujet de l'emplacement de l'objet

Dans la mesure du temps disponible, les fonctionnalités suivantes seront proposées :
- L'utilisateur final pourra créer ses propres plans de placement d'objets via une interface desktop (web ou autre)
- Une information géographique sera retournée, au lieu d'une simple information textuelle
