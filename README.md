# App_Bonnes_Lectures (TP Framework Web)

Application web Django permettant de gérer une bibliothèque personnelle, d'ajouter des livres et de poster des avis.

## 🚀 Lancement Rapide

1.  Clonez le dépôt :
    ```bash
    git clone [https://github.com/mldxus/App_Bonnes_Lectures.git](https://github.com/mldxus/App_Bonnes_Lectures.git)
    cd App_Bonnes_Lectures
    ```

2.  Créez un fichier `.env` à la racine et ajoutez-y :
    ```env
    USERNAME=admin
    USERID=1000
    ```

3.  Lancez Docker (Assurez-vous que le port 8080 est libre) :
    ```bash
    docker-compose up -d --build
    ```

4.  **Créez les tables** de la base de données (trouvez le `<nom-du-conteneur>` dans Docker Desktop) :
    ```bash
    docker exec -it <nom-du-conteneur> python manage.py migrate
    ```

5.  Créez un compte admin :
    ```bash
    docker exec -it <nom-du-conteneur> python manage.py createsuperuser
    ```

6.  Accédez au site :
    * **Site :** `http://localhost:8080/`
    * **Admin :** `http://localhost:8080/admin/`