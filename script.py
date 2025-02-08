import requests
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.getenv("AUTH_TOKEN")  # Se citeste tokenul din .env

if not AUTH_TOKEN:
    raise ValueError("Token-ul de autentificare lipseste. Actualizeza fisierul '.env' corespunzator.")

headers = {
    'Authorization': f'Bearer {AUTH_TOKEN}',
}

#1 - Listat toate aplicațiile care exista în Apigee într-o organizatie data

print('============ TASK 1 ============')

org = os.getenv("ORG_NAME")

if not org:
    raise ValueError("Numele organizatiei lipseste. Actualizeza fisierul '.env' corespunzator.")

def listing_all_apps_from_org(org_name=org):
    try:
        response = requests.get(f'https://apigee.googleapis.com/v1/organizations/{org_name}/apps', headers=headers)
    except Exception as e:
        return f"Error: {e}"
        
    if response.status_code == 200:
        aplicatii = response.json()['app']
        aplicatii_id = []
        for app in aplicatii:
            aplicatii_id.append(app['appId'])

        apps_id_only = ', '.join(str(app) for app in aplicatii_id)
        
        return f"Aplicatiile din organizatia '{org_name}' au id-urile: {apps_id_only}"
    else:
        return (f"Eroare, mesajul: '{response.json()['error']['message']}'")



print(listing_all_apps_from_org())
print('\n')


#2 - Listat aplicațiile care aparțin unui anumit developer (primit ca parametru)

print('============ TASK 2 ============')

def listing_all_apps_for_a_developer(dev_mail, org_name='mateineagatesting'):
    try:
        response = requests.get(
        f'https://apigee.googleapis.com/v1/organizations/{org_name}/developers/{dev_mail}/apps',
        headers=headers
        )
    except Exception as e:
        return f"Error: {e}"

    if response.status_code == 200:
        aplicatii = response.json()['app']
        aplicatii_id = []
        for app in aplicatii:
            aplicatii_id.append(app['appId'])

        result = ', '.join(str(app) for app in aplicatii_id)
        
        return f"Aplicatiile din organizatia '{org_name}', pentru developerul cu adresa de email '{dev_mail}' au id-urile: {result}"
    else:
        return (f"Eroare, mesajul: '{response.json()['error']['message']}'")

developer_email = os.getenv("DEVELOPER_EMAIL")

if not developer_email:
    raise ValueError("Emailul developer-ului lipseste. Actualizeza fisierul '.env' corespunzator.")

listing_all_apps_for_a_developer_text = listing_all_apps_for_a_developer(developer_email)

print(listing_all_apps_for_a_developer_text)
print('\n')


#3 - Creat aplicatie noua cu un nume specific ( cu nume specific)

print('============ TASK 3 ============')
def creating_an_app(name, org_name='mateineagatesting', developer_email='user@example.com'):

    app_data = {
    "name": name,
    }

    try:
        response = requests.post(
            f'https://apigee.googleapis.com/v1/organizations/{org_name}/developers/{developer_email}/apps',
            headers=headers,
            json=app_data
        )
    except Exception as e:
        return f"Error: {e}"
    
    if response.status_code == 201:
        print(f"Aplicatia cu numele '{name}' a fost creata cu succes pentru developerul cu adresa de email '{developer_email}', in organizatia '{org_name}'.\n")
        verification=listing_all_apps_for_a_developer(developer_email)
        return (f"Verificare: {verification}")
    else:
        return (f"Eroare, mesajul: '{response.json()['error']['message']}'")

task_name = os.getenv("APP_NAME")

if not task_name:
    raise ValueError("Numele taskului care vrei sa fie adaugat lipseste. Actualizeza fisierul '.env' corespunzator.")

print(creating_an_app(task_name))