import requests

url = "https://naas.isalman.dev/no"     #URL ophalen van de API
response = requests.get(url)            #GET verzoek sturen naar de API
if response.status_code != 200:         #Controleren of het verzoek succesvol was
    raise Exception("API request failed with status code {}".format(response.status_code))
else:
    data = response.json()              #JSON antwoord omzetten naar een Python dictionary
    print(data["reason"])               #De "reason" waarde uit de dictionary afdrukken