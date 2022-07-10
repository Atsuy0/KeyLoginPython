import os
import time
import random

os.system('cls' if os.name == 'nt' else 'clear')
 
msg = {False: "Non autorisé", True: "Autorisé"}
 
#N° du Badge (n° qui sera normalement récupéré grâce au NFC)
key = "6Ufd7iubMzA69fG5W55K"
 
with open("key.txt", "r") as f_badges:
    for ligne in f_badges:
        if key == ligne.strip():
            autorisation = True
            break
    else:
        autorisation = False
 
print(msg[autorisation])