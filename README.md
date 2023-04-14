#  Analyse des probabilités de drop sur un site de jeux d'argent en ligne
Ce projet consiste en une analyse des probabilités de drop pour les skins dans les caisses disponibles sur un site de jeux d'argent en ligne. L'objectif de l'analyse était de déterminer si certaines caisses étaient plus ou moins avantageuses que d'autres, et de calculer l'espérance de gain pour chaque caisse.

## Fonctionnement du projet
Le projet est divisé en deux fichiers principaux :

`drop.py` : ce fichier contient le code Python utilisé pour récupérer les probabilités de drop pour chaque skin dans chaque caisse. Il utilise des requêtes HTTP pour récupérer les données à partir du site de jeux d'argent en ligne, puis calcule l'espérance de gain pour chaque caisse.
Ce programme retourne la liste `drop` qui est de la forme : [[probabilités(en %), montant_du_gain], ... ].
Il retourne également l'espérance et la vérification que la somme des probabilités soit bien à 100%.

`ratio.xlsx` : ce fichier Excel contient les données brutes récupérées à partir de `drop.py`. Donc pour chaque caisse il contient l'espérance, le prix de la caisse, la différence entre le prix et l'espérance, le ratio de 'perte' et donc par déduction le TRJ fixé par le site pour la caisse en question

![alt text][excel]

## Résultats de l'analyse
L'analyse a révélé que le ratio de perte était le même pour toutes les caisses, soit environ 14%. Cela signifie que l'espérance de gain pour chaque caisse est proportionnelle à son prix. La seule exception est la caisse qui coûte 400$, qui présente un ratio de perte de 8% et un TRJ (taux de reversement aux joueurs) de 92%.

L'histogramme des probabilités de drop pour chaque caisse a révélé que la répartition des probabilités suit une loi exponentielle avec un lambda qui semble être supérieur ou égal à 1.5.

![alt text][histKRL]

## Conclusion
En conclusion, cette analyse montre que peu importe le prix payé pour une caisse, l'espérance de gain est toujours proportionnelle au prix et est calculée de manière à ce que le site de jeux d'argent en ligne ait un ratio de gain d'environ 14%. Il n'y a donc pas de caisse plus ou moins avantageuse que d'autres.

## Références
Les probabilités de drop ont été récupérées à partir du site de jeux d'argent en ligne (https://hellcase.com/).


[excel]: https://github.com/Axellrn13/projet-esperance/blob/main/excel.png "Aperçu de l'excel"
[histKRL]: https://github.com/Axellrn13/projet-esperance/blob/main/histKRL.png "Histogramme de la caisse KRL"