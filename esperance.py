from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

# ouvrir le fichier HTML
with open("krl.html", encoding='utf-8') as f:
    html = f.read()

# créer un objet Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# trouver tous les éléments de tableau dans le HTML
table_rows = soup.find_all("tr")

# boucler sur les lignes de tableau et extraire les informations souhaitées
drop = []
for row in table_rows:
    cols = row.find_all("td")
    if cols:
        try:
            price = cols[1].find("span", {"class": "base-price__value"}).text
            odds = cols[2].text
            drop.append([odds, float(price)])
        except:
            continue

# afficher les résultats
print(drop)

total_percentage = sum([float(d[0].replace("%", "")) for d in drop])
if total_percentage == 100:
    print("La somme des pourcentages est égale à 100%")
else:
    print(f"Attention, la somme des pourcentages est de {total_percentage}%")

def calculer_esperance(liste_gains):
    somme_pond = 0
    somme_gains = 0
    for pourcentage, gain in liste_gains:
        # Convertit le pourcentage en décimal
        pourcentage_decimal = float(pourcentage[:-1]) / 100
        somme_pond += pourcentage_decimal
        somme_gains += pourcentage_decimal * gain
    esperance = somme_gains / somme_pond
    return esperance

esperance = calculer_esperance(drop)
print("L'espérance est de :", esperance)

def plot_histogram(drop, step_size):
    min_gain = min(d[1] for d in drop)
    max_gain = max(d[1] for d in drop)
    bins = list(range(int(min_gain), int(max_gain) + step_size, step_size))
    counts, bins, _ = plt.hist([d[1] for d in drop], bins=bins)
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(len(counts)):
        plt.bar(bins[i], counts[i], width=step_size, color=colors[i % len(colors)])
    plt.xticks(bins)
    plt.show()

#plot_histogram(drop, 17)






