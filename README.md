Transform Nao in Assitant with GTP-3 
## Nao-chatbot
Ce projet utilise les technologies suivantes :

# Prerequisites
- Nao robot with the Naoqi SDK installed
- OpenAI API key
- Python 2.7



SpeechRecognition pour la reconnaissance de la voix
OpenAI pour générer des réponses à partir d'un prompt
Naoqi pour faire parler le robot Nao
Dotenv pour stocker les informations sensibles (comme la clé API OpenAI) en dehors du code source
Le script principal main.py contient les fonctions suivantes :

configNao(Name) : crée un proxy pour communiquer avec le service de synthèse vocale de Nao
openai(text) : envoie une requête à l'API OpenAI pour générer une réponse à partir d'un prompt qui inclut le texte reçu (text)
recognize() : utilise la bibliothèque SpeechRecognition pour écouter et transcrire la voix de l'utilisateur
naoSay(proxy,text) : fait dire à Nao le texte reçu (text) en utilisant le proxy créé par configNao()
convertion() : appelle recognize() pour écouter l'utilisateur, puis openai() et naoSay() pour faire répondre Nao à l'utilisateur
main() : boucle infinie qui attend que l'utilisateur dise "Ok" ou "ok" ou "OK", puis appelle convertion() pour démarrer la conversation avec Nao

# Pour utiliser ce script, vous devez avoir :
une connexion à internet pour accéder à l'API OpenAI
un robot Nao avec une adresse IP valide et une connexion à cette IP
une clé API OpenAI valide et stockée dans un fichier .env (voir .env.example pour le format attendu)
une connexion audio pour enregistrer la voix de l'utilisateur
Pour lancer le script, vous devez installer les dépendances en exécutant pip install -r requirements.txt puis exécuter le script main.py en utilisant la commande python main.py.
il faut aussi télécharger le SDK de Naoqi a l'adresse suivante : 
https://www.aldebaran.com/fr/support/nao-6/downloads-softwares
documentation : http://doc.aldebaran.com/1-14/dev/python/install_guide.html

