# HULK

A fast algorithm for unsupervised learning

alternatives:
- Homeostasis is necessary for the unsupervised learning of orientation-selective cells

## fr: Résumé

La formation des structures de connexions neurales est un processus largement non supervisé, c’est-à-dire que l’émergence de cette architecture est majoritairement auto-organisée.
Dans le cortex visuel primaire des mammifères par exemple, on observe ainsi au cours du développement l’émergence de cellules sélectives à l'orientation locale qui mènent à l'élaboration d'une représentation des contours à partir de l'image visuelle.
Une difficulté majeure pour la définition des algorithmes d’apprentissage non supervisé est qu'au cours de ce processus, d’un côté le codage est effectué connaissent une structure non mature et de l’autre côté de l’adaptation de cette structure est effectuée connaissant un code qui n'est pas encore optimal.
Nous proposons ici un algorithme rapide compatible avec une architecture neuro-mimétique qui résout ce problème et permet l’apprentissage de filtres localisés sensibles à l'orientation.
La clé de cet algorithme réside dans un mécanisme simple d’homéostasie qui permet de réconcilier ces processus antagonistes qui ont lieu à l’échelle de temps du codage et  de l’apprentissage.
Nous avons testé cet algorithme non supervisé avec cette règle optimale d'homéostasie pour différents algorithmes existants d’apprentissage non supervisé couplé avec des algorithmes différents de codage neural.
De plus, nous proposons une simplification de cette règle optimale d’homéostasie en implémentant une simple heuristique sur la probabilité d’activation des neurones.
Par rapport à la règle d’homéostasie optimale, nous montrons que cette heuristique permet d’implémenter un algorithme plus rapide d’apprentissage non supervisé tout en gardant une large part de son efficacité.
Enfin, nous montrons qu'un tel algorithme peut être étendu à des architectures de type convolutionnel et nous montrons les résultats obtenus sur différentes bases d’image naturelles. Ces résultats démontrent son application potentielle à des algorithmes rapides de classification des images, par exemple dans des architectures hiérarchiques et dynamiques.

## en: Abstract

The formation of structures in neural populations is mostly an unsupervised learning process, that is, that the emergence of this architecture is mostly self-organized.
In the primary visual cortex of mammals, for example, one may observe during development the emergence of cells selective to localized, oriented features and that lead to the development of a rough representation of contours of the retinal image in this area.
A major difficulty for the definition of unsupervised learning algorithms is that during this process, on the one hand the coding is performed knowing an immature structure and on the other hand, the adaptation of this structure is performed knowing a code that is not yet optimal.
We propose here a fast algorithm compatible with a neuromimetic architecture which solves this problem and allows for the fast emergence of localized filters sensitive to orientation.
The key to this algorithm lies in a simple yet optimal mechanism of homeostasis that reconciles the antagonistic processes that take place at the time scale of coding and learning.
We tested this unsupervised algorithm with this homeostasis rule for a range of existing unsupervised learning algorithms coupled with different neural coding algorithms.
In addition, we propose a simplification of this optimal rule of homeostasis by implementing a simple heuristic on the probability of activation of the neurons.
Compared to the optimal homeostasis rule, we show that this heuristic makes it possible to implement a faster unsupervised learning algorithm while keeping a large part of its efficiency.
Finally, we show that such an algorithm can be extended to convolutional architectures and we show the results obtained on different natural image databases. These results demonstrate the potential application of such a strategy to the fast classification of images, for example in hierarchical and dynamic architectures.

## fr: Introduction

L’architecture neurale consiste en un système dynamique complexe qui opère à différentes échelles de temps. En particulier, une de ses propriétés est de réussir le tour de force de pouvoir à la fois représenter une information rapidement mais aussi de pouvoir s'y adapter sur le long terme de façon autonome (auto-organisée) pour optimiser ce codage.
Dans le cas du cortex visuel primaire des mammifères, on peut par exemple observer un codage rapide de l’entrée rétinienne comme un processus de transmission d’une image rétinienne en une une esquisse brute qui représente les contours de l’image.
Cette opération rapide, de l'ordre de 50 milli-secondes chez les humains, est la clé des résultats de Hubel et Wiesel qui ont montré que les cellules du cortex visuel primaire des mammifères sont majoritairement sélectifs à des orientations sur des champs récepteurs relativement localisés.
Une étape majeure dans la compréhension de ce mécanisme a été de montrer que l'émergence de ces filtres peut être expliquée comme le couplage d’un simple apprentissage de type Hebbien avec un codage optimal de l’image.
En effet les travaux de Bruno Olshausen ont montré qu'en imposant un codage parcimonieux de l’image, on peut obtenir l’émergence de telles cellules dans un modèle de type neural.
Ce type d'algorithme d’apprentissage non supervisé a été mis en relation avec de nombreux autres types d'algorithmes de représentation optimale aussi bien utilisés en traitement du signal qu'en intelligence artificielle.
En particulier, cet algorithme permet l’extraction des composantes indépendantes du signal, par exemple les orientations dans l'image. Cette représentation permet d'observer l'émergence de représentations invariantes à des transformées géométriques comme les rotations.
Un rapprochement récent entre ces algorithmes et des algorithmes de type probabiliste permettent de les placer dans une nouvelle perspective. En effet, ces algorithmes non supervisés sont équivalents à l'optimisation par descente de gradient d’un coût de codage de type informationnel. Celui-ci permet d’évaluer de façon de façon quantitative l’exploration de nouvelles composantes dans le signal pour l'apprentissage par rapport à l’exploitation de ces composantes dans le codage. À ce titre, cet apprentissage consiste en deux mécanismes antagonistes, un à longue échelle de temps qui correspond à l’apprentissage et à l’exploration de nouvelles composantes et une échelle plus rapide qui correspond au codage.

Une composante souvent ignorée dans ce type d’apprentissage est l'ensemble des mécanismes d’homéostasie. En effet, ceux-ci sont implémenté dans les algorithmes originaux (Olshausen, Rehn, ...) comme une heuristique qui permet simplement d’éviter que l’algorithme ne diverge. Elle consiste dans des algorithmes récents à ne constituer qu'une égalisation de l'énergie de chaque composante (Mairal).
Toutefois, les mécanismes neuronaux d'homéostasie sont à l’œuvre dans de nombreuses composantes du code neural.
Par exemple, les réseaux de neurones inhibiteurs de type GABA permettent de réguler l’activité globale de population de neurones.
Ce mécanisme permet alors de balancer la contribution de l’activité excitatrice par rapport à l’activité inhibitrice.
Par ce mécanisme, ce type de réseau balancé permettent d’expliquer de nombreuses fonctionnalités inhérentes au cortex visuel primaire (Hansel).
Ces mécanismes qui prennent souvent la forme de règles de normalisation (Schwartz) dans le réseau servent souvent de théorie normative pour expliquer les mécanismes présents dans le cortex visuel primaire (voir Heeger).
Plutôt, ces travaux ont pour objectif de montrer que les cellules qui émergent de cet algorithme ont les mêmes caractéristiques que celle observée en neurophysiologie (Rehn, Loxley).
D’autres algorithmes utilisent des non-linéarité qui implémentent de façon implicite des règles homéostatiques dans des algorithmes neuro-mimétiques (Gartner et Brito). Ces non-linéarités sont majoritairement utilisées dans la sortie des couches successives des réseaux d’apprentissage profond qui sont utilisé maintenant pour la classification d’images ou l’intelligence artificielle.
Toutefois la plupart de ces règles de normalisation non-linéaire sont basées sur des heuristiques imitant les mécanismes neuronaux mais ne sont pas justifiées comme partie intégrante de l’algorithme non supervisé à partir de la descente de gradient sur le coût de représentation.

Il est important de noter à ce point que les que les algorithmes d’apprentissage utilisés en intelligence artificielle peuvent nous apporter un nouvel éclairage sur le fonctionnement de ces processus neuraux et notamment sur l'apprentissage non supervisé.
Dans le domaine de l’apprentissage machine, l’apprentissage non supervisé correspond à l’apprentissage de dictionnaires de représentation quand des données de catégorisation sont inconnus. Cet apprentissage est donc effectué de façon autonome et il est notamment utilisé en compression d’image et du signal, en détection d'objets, en séparation de source mais aussi pour la diminution du bruit dans des signaux bruts.
À ce titre, cette classe d’algorithmes est extrêmement utile dans les premières couches des algorithmes d’intelligence artificielle comme les algorithmes profonds.
Il existe de nombreuses variantes de tels algorithmes qui prennent la forme soit d’une optimisation du transfert d'information (Bell), soit sous la forme de règles d’apprentissages dans l’apprentissage profond ou encore sous la forme d’algorithmes récursifs en statistiques et probabilités avec par exemple la poursuite de projection.
Une classe importante de ces algorithmes considère que l’ensemble des solutions qu’ils vont être considéré sont celles qui correspondent à un codage optimal sous la forme d’un codage parcimonieux c’est-à-dire pour lequel pour lequel un petit nombre de composantes seront sélectionnés.
Ce principe est assez général pour être appliqué à de nombreuses classes de signaux et permettre une analyse mathématique de ce principe.
Ainsi, il a été montré qu’un tel codage permet d’améliorer des algorithmes de classification en particulier en limitant le nombre de couches nécessaires dans un algorithme d’apprentissage profond permettant la classification de d'mages contenant ou ne contenant pas des animaux (Perrinet et Bednar, 2015).
En particulier nous avons montré précédemment qu’un algorithme rapide de codage de type par ce manuel peut être implémenté dans une implémenté dans une architecture de type normal neuronale (Perrinet, 2010).
Toutefois des études récentes mettre en cause ce principe de codage parcimonieux (Eichhorn 2009, Zoran et Weiss 2012) et suggère qu’un simple analyse de type analyse en composantes principales appliqués dans une métrique complexe est suffisante pour expliquer émergence de filtres sélectifs à l’orientation similaires à ceux observés dans le cortex visuel primaire.

``>>> LUP IS HERE <<<<``
Afin d’offrir une perspective plus large sur ce problème, nous allons essayer de l’exprimer sous la forme d’un problème probabiliste.
Cette approche est déjà largement exploité dans les travaux anciens de Barlow sous le terme de principe de réduction de redondance.
Ils ont conduit à traduire ce problème d’apprentissage en terme de codage efficace par exemple en implémentant des règles d’inhibition dans le champ récepteurs de la rétine (Srinivasan, 1981).
D’autres études montrent que ces règles reviennent à imposer au système d'être proche d'un limite de criticalité et à optimiser la balance entre optimisation du codage et de l'apprentissage (Beggo, 2008 in Sandin)
Plus généralement, nous placerons notre modèle sous la théorie de laine en utilisant la théorie de l’énergie libre formulée par Karl Friston et qui permet de poser explicitement le problème du codage imparfait durant la prends tissage l’apprentissage durant l’apprentissage.
L'apprentissage L'apprentissage n'est plus un but par lui-même.
l'hoimeosatsie a une part  predicitve (Rao Balard)
Le but de global de la formation des connexionsEt d'obtenir une structure telle queL'entrée sur ce rielEst-on mieux prédit l'entrée sensorielle est au mieux prédit l'entrée sensorielle et au mieux prédite par la structure de la population dans.
L'ensemble des processusAux différentes échelles de tempsDu codageAllô mais au stage est à l'apprentissage sont ainsi considérésDans une même théorieNormative.Le but de l'apprentissage et simplementDe ne pas être surpris par l'entrée sensorielle.
À ce titre le but de l'apprentissage et d'obtenir un codage qu'il se soit le moins variablesA priori c'est-à-dire avant d'avoirReçu à l'information sensorielle.


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

## en: Introduction

## fr: Algorithme


Le principe de l’algorithme consiste à rajouter des variables latentes qui vont permettre de prédire les déviations dans le codage ou l’apprentissage pendant l’apprentissage.

## en: Algorithm


## Méthode

## Résultat : apprentissage de filtre localiser

## Résultat : apprentissage de noyau de convolution

## Discussion et conclusions

In addition to learning filters we have a place is better today on the coverage of colors compilation Calmels
Caramels Karen else Karen else cuddles kill themselves care of that isNine
Leppo to sessional cigars it thi
L’apprentissage non supervisez de filtre peut être étendu à l’apprentissage de noyau de convolution.
En incluant une hypothèse d’un variances à la translation dans le modèle génératif des imagess
On peut augmenter le dictionnaire de représentation en incluant les filtres à toutes les positions de l’image et en mettant des zéro autre part
Et le produit scalaire si obtenue revient à un opérateur de convolution sur les filtres symétrique
Cette manipulation permet D’augmenter la dimension de représentation dans les images tout en gardant l’algorithme totalement préserver tout
Cette manipulation permet tout en préservant l’intégralité du principe de l’algorithme d’augmenter la dimension de la représentation du dictionnaire



Nous avons appliquer cette méthode à l’apprentissage des noyaux de convolution pour différentes classes d’image. Une première classe d’image constitué d’images naturel montre un Libergère localiser sélectif a des tailles et orientations différentes.
En utilisant uneConduisant une base de données d’image représentant des visages nous obtenons un autre ensemble de dictionnaire de noyau de composition ceci représente des caractéristiques spécifiques au visage comme la bouche les yeux le visage et qui correspondent aux différentes parties qui constituent l’intégralité d’un visage.

## références