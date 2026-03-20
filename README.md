# DM_python_datascience_2A
Rendu intermédiaire de python pour la datascience de 2A - groupe Mahaut Maurel, Gustave Billon, Gabriel Stremsdoerfer

# !!!! TOUJOURS PULL AVANT DE PUSH !!!!

# installer un nouvel environnement python à la racine du projet: 
        python -m venv venv 
# activer environnement:
        source venv/bin/activate 
# ! vérifier que le chemin de l'environnement est dans le .gitignore, le copier coller dedans sinon.

# installer les packages nécessaires :
        pip install -r requirements.txt

# le code de chaque question est dans un module dédié, on peut faire tourner le code directement 
# via rendu.ipynb

# Si jamais il y a un problème de cohérence de mémoire entre fichier jupyter et les modules (affiche erreur et c'est pas la bonne version du code qui est retournée dans le message d'erreur), lancer le code ci-dessous:
        from importlib import reload
        import code_exo.<remplir avec chemin>
        reload(code_exo.<remplir avec chemin>)
# de cette manière, c'est la dernière version sauvegardée du module qui tournera dans le jupyter