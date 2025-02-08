# db-task-mateineaga

Dupa cum este cerut, programul "script.py" returneaza toate aplicatiile dintr-o anumita organizatie, toate aplicatiile unui developer dintr-o anumita organizatie, si de asemenea, creeaza o aplicatie, desigur in cadrul unei organizatii pentru un anumit developer.

Asadar, pentru a rula cu succes scriptul, trebuie modificat fisierul ".env", care constituie variabilele de environment, fiind necesara o structura de forma:

ORG_NAME=x
DEVELOPER_EMAIL=y
APP_NAME=z
AUTH_TOKEN=k

Pentru a obtine tokenul de autentificare, se va rula comanda "gcloud auth print-access-token". Tokenul expira dupa 1h.

Codul trateaza si cazurile in care organizatiile, developerii sau taskul nu pot fi accesate/create cu mesaje sugestive.
