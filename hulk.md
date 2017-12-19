# HULK

A fast algorithm for unsupervised learning

## Résumé

La formation des structures de connexions neuronales est un processus largement non supervisé, c’est-à-dire que l’émergence de cette architecture est majoritairement auto-organisée.
Dans le cortex visuel primaire des mammifères par exemple, on observe ainsi au cours du développement l’émergence de cellules sélectives à l'orientation locale qui mènent à l'élaboration d'une représentation des contours à partir de l'image visuelle.
Une difficulté majeure pour la définition des algorithmes d’apprentissage non supervisé est qu'au cours de ce processus, d’un côté le codage est effectué connaissent une structure non mature et de l’autre côté de l’adaptation de cette structure est effectuée connaissant un code qui n'est pas encore optimal.
Nous proposons ici un algorithme rapide compatible avec une architecture neuro-mimétique qui résout ce problème et permet l’apprentissage de filtres localisés sensibles à l'orientation.
La clé de cet algorithme réside dans un mécanisme simple d’homéostasie qui permet de réconcilier ces processus antagonistes qui ont lieu à l’échelle de temps du codage et  de l’apprentissage.
Nous avons testé cet algorithme non supervisé avec cette règle optimale d'homéostasie pour différents algorithmes existants d’apprentissage non supervisé couplé avec des algorithmes différents de codage neural.
De plus, nous proposons une simplification de cette règle optimale d’homéostasie en implémentant une simple heuristique sur la probabilité d’activation des neurones.
Par rapport à la règle d’homéostasie optimale, nous montrons que cette heuristique permet d’implémenter un algorithme plus rapide d’apprentissage non supervisé tout en gardant une large part de son efficacité.
Enfin, nous montrons qu'un tel algorithme peut être étendu à des architectures de type convolutionnel et nous montrons les résultats obtenus sur différentes bases d’image naturelles. Ces résultats démontrent son application potentielle à des algorithmes rapides de classification des images, par exemple dans des architectures hiérarchiques et dynamiques.

## Introduction

L’architecture neuronale consiste en un système dynamique complexe qui opèrent à différentes échelles de temps.
Dans le cas du corps texte vite visuel primaire dans le cas du cortex visuel primaire par exemple des mammifères on peut observer un codage rapide de l’entrée rétinienne comme une un processus de transmission d’une image rétinienne en une une esquisse brute qui représente les contours de l’image. De l’image.
Cette opération est rapide de l’ordre de 50 000 secondes et la clé des résultats de Hubel et Wiesel qui ont montré que les cellules du cortex visuel primaire sont majeurs majoritairement sélective à désorientation sur des champs récepteurs localiser.
Une étape majeur dans la compréhension de ce mécanisme a été de montrer que quand elle a une émergence de ses filtres peut être expliqué comme le couplage d’un simple apprentissage de type est bien avec un codage optimal de l’image.
En effet les travaux de Bruno le savait scène ont montré quand on imposant un codage parcimonieux de l’âge on peut obtenir l’émergence de telles cellules dans un modèle de type neuronale.

C’est algorithme d’apprentissage non supervisez a été mis en relation avec de nombreux des algorithmes de représentation optimal utiliser aussi bien en traitement du signal quand intelligence artificielle.
En particulier, cette algorithme permet l’extraction des composantes indépendante du signal et ainsi de l’extraction Des composantes principales et indépendante du signal.
Un rapprochement récent entre ces algorithmes et des algorithmes probabiliste permettent de le mettre dans une nouvelle perspective. En effet l’algorithme mon supervisez revient à une optimisation d’un coup complète cinq Solaine de type informationnel. Celui-ci permet d’évaluer de façon de façon quantitative l’exploration de nouvelles composantes dans le signal par rapport à l’exploitation de ses composantes dans le codage. À ce titre c’est apprentissage non superviser consiste en deux mécanismes antagoniste un à long échelle de temps qui correspond à l’apprentissage est à l’exploration de nouvelles composantes et un à une échelle plus rapide qui correspond au codage.

Une composante souvent ignoré dans ce type d’apprentissage sont les mécanismes d’homéostasie. En effet ceux-ci sont implémenté dans les algorithmes originaux des hommes savent scène commune heuristique qui permet simplement d’éviter l’algorithme d’atteindre un minimum local dans la fonction de coup.
Les mécanismes
Les mécanismes neuronaux sont à l’œuvre dans de nombreuses composantes du code Nordal neuronale.
Par exemple les réseaux de neurones il dit bien tard de type Gaba permettent de réguler l’activité globale de population de neurones aussi.Pas en balançant l’activité excitatrices par rapport à l’activité inhibitrices.
Aussi ce type de réseau dit de type balancer permettent d’expliquer de nombreuses fonctionnalités inhérentes au cortex visuel primaire.
C’est mécanismes qui prône souvent la forme de règles de normalisation dans le réseau servent souvent de théorie normative pour expliquer les mécanismes présent dans le cortex visuel primaire voir Rahway Balard ou Vince égal.
Toutefois la plupart de ces algorithmes sont basées sur des heuristique imitant les mécanismes neuronaux mais ne sont pas justifiées comme partie intégrante de l’algorithme non supervisez.
Par exemple ceci ont pas ont pour objectif de montrer que les cellules qui émerge de cette algorithme ont les mêmes caractéristiques que celle observée en neurophysiologie.
D’autres algorithme fixe des noms linéarité appeler dans des règles homéostatique aussi bien dans des algorithmes normal mimétique de type Gartner et Barrideau et sont majoritairement utilisé dans la sortie des différentes couches des réseaux d’apprentissage profond qui sont majoritairement utilisé maintenant pour la classification la classification de l’âge ou l’intelligence artificielle. Alu

Il est important de noter à ce point de la discussion que les que les algorithmes d’apprentissage d’intelligence artificielle peuvent porter un nouvel éclairage sur le fonctionnement de ses computation processus neuronaux.
Dans le domaine de l’apprentissage machine l’apprentissage non supervisez correspond à l’apprentissage de dictionnaire de représentation qui est notamment utilisé en compression d’image et du signal en détection en séparation de source est et aussi pour la diminuassions diminution du bruit dans des signaux brute.
À ce titre c’est cette classe d’algorithme est extrêmement utile dans les premières couches des des algorithmes d’intelligence artificielle.
Il existe de nombreuses variantesOui de la dentelle de tes algorithmes des algorithmes dans supervisez qui prennent la forme soit d’une optimisation de la fin du transfert de la formation soit sous la forme de règles d’apprentissage dans l’apprentissage profond ou encore ou encore sous la forme d’algorithme récursifs en statistiques et probabilités avec la poursuite de projection.
Une classe importante de ses algorithmes considère que l’ensemble des solutions qu’ils vont être considéré sont celles qui correspondent à un codage optimal sous la forme d’un codage parcimonieux c’est-à-dire pour lequel pour lequel un petit nombre de composantes seront sélectionnés.
Ce principe est assez générale pour être appliquée à de nombreuses classes de signaux et permettre une analyse mathématique de ce principe.
Il a été montré qu’un tel codages permet d’améliorer des algorithmes de classification en particulier en limitant le nombre
D’apprentissage profond en limitant le nombre de couches nécessaires dans un Dell Gorette made apprentissage profond algorithme d’apprentissage profond permettant la classification de Dîmages contenant on ne contenant pas des animaux
En particulier nous avons montré précédemment qu’un algorithme rapide de codage de type par ce manuel peut être implémenté dans une implémenté dans une architecture de type normal neuronale.
Toutefois des études récentes mettre en cause ce principe de codage parcimonieux et suggère qu’un simple analyse de type analyse en composantes principales fenêtre suffisante pour expliquer émergence de filtre des filtres sélectif à Lorient sélectif à l’orientation dans le cortex visuel primaire.

Afin d’ offrir une perspective plus large sur ce problème nous allons essayer de l’exprimer sous la forme d’un problème probabiliste.
Cette approche est déjà largement exploité dans les travaux anciens de parano est sorti ni Vassalent et on conduit à traduire ce travail et ont conduit à traduire ce principe d’apprentissage non super Asie sous le terme de codage efficace par exemple en implémentant des règles d’inhibition dans le champ récepteurs de la rétine.
D’autres études montrent que ces systèmes reviennent à imposer la critique alité du système et à balancer entre codage et apprentissage
Plus généralement nous placerons notre modèle sous la théorie de laine en utilisant la théorie de l’énergie libre formulée par Karl Friston et qui permet de poser explicitement le problème du codage imparfait durant la prends tissage l’apprentissage durant l’apprentissage.

Ce papier est organisé suivant le plan suivant.
Tout d’abord nous montrerons l’impôtL’importance l’importance de l’homéostasie dans de l’eau mais Austasie dans des algorithmes d’apprentissage ah non superviser et dériveront une règle optimal pour l’apprentissage basé sur une et quoi Lisa Sion de l’histogramme et quoi Lisa Sion de l’histogramme.
Basé sur une égalisation de lest histogramme de l’histogramme.
Nous montrerons ensuite des résultats quantitatifs de cet algorithme optimal de me saisi en l’appliquant à différents des algorithmes aussi bien de codage que d’apprentissage.
En utilisant différentes bases d’apprentissage nous pourrons donner une analyse quantitative qui permettra de comparer ses différentes solutions.
Nous délivrons ensuite un algorithme Neuro mimétique d’homéostasie dérivés à partir de la règle optimal par rapport à une Aurice tique heuristique heuristique.
Nous comparons les résultats de ce nouvel algorithme avec l’algorithme optimal ainsi qu’avec les les algorithmes existe existant d’apprentissage dans supervisant non supervisez non supervisez.
De par sa nature Jules cet algorithme de par sa nature de par sa nature, cette algorithme peut facilement être étendu à des réseaux convolution L. Deux types de ceux utilisés en apprentissage profond.
C’est dépenses extension est possible en n’étant dans le dictionnaire de filtre par l’hypothèse d’un variances à la translation des représentations.
Nos résultats sur différentes bases d’apprentissage montre l’émergence stable et rapide de filtre caractéristiques à ses différentes bases et pour lesquelles nous espérons obtenir des résultats de classification supérieur aux algorithmes existant.
Enfin nous conclurons en montrant L’importance en montrant l’importance de l’homéostasie dans les algorithmes non supervisé.
En développant cet algorithme rapide d’apprentissage nous espérons son application rapide dans des algorithmes d’intelligence artificielle et notamment avec des perspectives pour les réseaux dynamiques en particulier nous espérons appliquer ce type d’algorithme sur j’ai embarqué deux types de grandes robot aérien.
Ce type d’architecture de type économique efficace et rapide permet de renouveler l’ensemble des algorithmes de type algorithme profond qui sont très gourmand en ressources à 20 %.
Nous espérons ainsi que ce nouveau type d’algorithme rapport rapide d’apprentissage non cyber mon supervisez puisse fournir une théorie normative pour le codage de l’information dans Lézères corticale primaire et dans le traitement sensoriel va niveau qu’il soit visuelle ou auditive.



## Algorithme


Le principe de l’algorithme consiste à rajouter des variables l’attente qui vont permettre de prédire les déviations dans le codage ou l’apprentissage pendant l’apprentissage

## Méthode

## Résultat : apprentissage de filtre localiser

## Résultat : apprentissage de noyau de convolution

## Discussion et conclusions

## références

In addition to learning filters we have a place is better today on the coverage of colors compilation Calmels
Caramels Karen else Karen else cuddles kill themselves care of that isNine
Leppo to sessional cigars it thi
L’apprentissage non supervisez de filtre peut être étendu à l’apprentissage de noyau de convolution.
En incluant une hypothèse d’un variances à la translation dans le modèle génératif des imagess
On peut augmenter le dictionnaire de représentation en incluant les filtres à toutes les positions de l’image et en mettant des zéro autre part
Et le produit scalaire si obtenue revient à un opérateur de convolution sur les filtres symétrique
Cette manipulation permet D’augmenter la dimension de représentation dans les images tout en gardant l’algorithme totalement préserver tout
Cette manipulation permet tout en préservant l’intégralité du principe de l’algorithme d’augmenter la dimension de la représentation du dictionnaire


Peter
Title
A male status as necessary falls and supervised learning of Canada Calmels Charles capitals caramels
How many with Palos help with pages homeostasis who meals tases line

Homeostasis is necessary for the unsupervised learning of call of the conversation Calmels

Nous avons appliquer cette méthode à l’apprentissage des noyaux de convolution pour différentes classes d’image. Une première classe d’image constitué d’images naturel montre un Libergère localiser sélectif a des tailles et orientations différentes.
En utilisant uneConduisant une base de données d’image représentant des visages nous obtenons un autre ensemble de dictionnaire de noyau de composition ceci représente des caractéristiques spécifiques au visage comme la bouche les yeux le visage et qui correspondent aux différentes parties qui constituent l’intégralité d’un visage.
