Dans les archives de Claude Shannon, Richard Hamming a retrouvé une lettre, dont chaque caractère
appartient à la table ASCII et est encodée sur 8 bits. Ne parvenant pas à la déchiffrer, il souhaite
l'envoyer à son ami David Albert Huffman. Sachant que des erreurs pourraient s'insérer dans la lettre
lors de sa transmission, il enrichit le codage binaire (il devient 1,75 fois plus long) pour que le
destinataire puisse éventuellement corriger ces erreurs lors de sa réception. Le contenu modifié de la
lettre se trouve dans le fichier lettre.txt
Une fois la lettre reçue, Huffman détecte deux erreurs (une au début et une à la fin), les corrige, puis
supprime les bits de contrôle et l'encode sous forme de caractères alphanumériques. Obtenant une
suite de caractères incohérents, il se rend compte, après analyse, qu'elle a été chiffrée par une méthode
de chiffrement polyalphabétique du XVIème siècle. Grand amateur de serpents, il parvient à la décrypter
et découvre alors le destinataire de cette lettre.
Decidé à lui faire parvenir, il rechiffre la lettre par une variante du chiffrement précédant, considéré
comme "le seul algorithme cryptographique à confidentialité parfaite" par Claude Shannon. De plus,
jugeant le poids du fichier trop important, il parvient à rendre le codage binaire optimal et à réduire ce
poids de plus d'un quart.
Il envoie alors la lettre chiffrée et compressée à son destinataire, qui parvient finalement à la lire
(grâce aux données supplémentaires que lui a fourni Huffman) ...
Il est demandé de produire un programme dans le langage de votre choix permettant d'effectuer les
manipulations d'Huffman et du destinataire sur la lettre. Le code doit être commenté. Ce programme
comportera des jeux d'essais afin de tester automatiquement toutes les fonctionnalités demandées lors
de son lancement (chaque étape sera bien identifiée)
