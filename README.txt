Guide de résolution pour la génération des clés 256 bits:

Ensuite, accédez au répertoire OpenSSL :
On a cloné le dépôt OpenSSL
git clone --branch OpenSSL_1_1_1-stable https://github.com/openssl/openssl.git

Ensuite, on accede au répertoire OpenSSL :
cd openssl

On ouvre le fichier crypto/rsa/rsa_local.h dans un éditeur de texte. 
nano crypto/rsa/rsa_local.h

On cherche la ligne qui définit la taille minimale des clés RSA. On remplace 512 par 256.
#define RSA_SMALL_MODULUS_BITS 512 
Devient donc :
#define RSA_SMALL_MODULUS_BITS 256 
 

Configurez OpenSSL avec la nouvelle modification et compilez-le :
./config
make
sudo make install








Guide d'utilisation 

Installation d’open ssl : Assurez-vous d'avoir installé les bibliothèques nécessaires en exécutant la commande suivante dans votre terminal :
Sudo apt-get install openssl
Exécution du Script :
o    Ouvrez votre terminal dans le répertoire où se trouve le script.
o    Exécutez la commande suivante pour lancer la génération des clés :
python3 ABITBOL_BARKA_256keys.py

et

python3 ABITBOL_BARKA_512keys.py