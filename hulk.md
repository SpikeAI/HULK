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
Dans le cas du cortex visuel primaire des mammifères, on peut par exemple observer un codage rapide de l’entrée rétinienne comme un processus de transmission d’une image rétinienne en une esquisse brute qui représente les contours de l’image.
Cette opération rapide, de l'ordre de 50 milli-secondes chez les humains, est la clé des résultats de Hubel et Wiesel qui ont montré que les cellules du cortex visuel primaire des mammifères sont majoritairement sélectifs à des orientations sur des champs récepteurs relativement localisés.
Une étape majeure dans la compréhension de cette observation a été de montrer que l'émergence de ces filtres peut être expliquée comme le couplage d’un simple apprentissage de type Hebbien avec un codage optimal de l’image.
En effet les travaux de Bruno Olshausen ont montré qu'en imposant un codage parcimonieux de l’image, on peut obtenir l’émergence de telles cellules dans un modèle de type neural.
Ce type d'algorithme d’apprentissage non supervisé a été mis en relation avec de nombreux autres types d'algorithmes de représentation optimale aussi bien utilisés en traitement du signal qu'en intelligence artificielle.
En particulier, cet algorithme permet l’extraction des composantes indépendantes du signal, par exemple les orientations dans l'image.
Cette représentation permet d'observer l'émergence de représentations invariantes à des transformées géométriques comme ici les rotations et le translations.
Un rapprochement récent entre ces algorithmes et des algorithmes de type apprentissage machine permettent de les placer dans une nouvelle perspective. En effet, ces algorithmes non supervisés sont équivalents à l'optimisation par descente de gradient d’un coût de codage de type informationnel. Ce coût permet d’évaluer de façon de façon quantitative l’exploration de nouvelles composantes dans le signal pour l'apprentissage par rapport à l’exploitation de ces composantes dans le codage. À ce titre, cette remarque montre que l'apprentissage non-supervisé consiste en deux mécanismes antagonistes, un à longue échelle de temps qui correspond à l’apprentissage et à l’exploration de nouvelles composantes et une échelle plus rapide qui correspond au codage.

Une composante souvent ignorée dans ce type d’apprentissage est l'ensemble des mécanismes d’homéostasie. En effet, ceux-ci sont implémenté dans les algorithmes originaux (Olshausen, Rehn, ...) comme une heuristique qui permet simplement d’éviter que l’algorithme ne diverge. Elle consiste dans des algorithmes récents à ne constituer qu'une égalisation de l'énergie de chaque composante (Mairal).
Toutefois, les mécanismes neuronaux d'homéostasie sont à l’œuvre dans de nombreuses composantes du code neural et sont essentiels au fonctionnement global du code neural.
Par exemple, les réseaux de neurones inhibiteurs de type GABA permettent de réguler l’activité globale de population de neurones.
Ce mécanisme permet alors de balancer la contribution de l’activité excitatrice par rapport à l’activité inhibitrice.
Par ce mécanisme, ce type de réseau balancé permettent d’expliquer de nombreuses fonctionnalités inhérentes au cortex visuel primaire (Hansel).
Ces mécanismes qui prennent souvent la forme de règles de normalisation (Schwartz) dans le réseau servent souvent de théorie normative pour expliquer les mécanismes présents dans le cortex visuel primaire (voir Heeger).
Toutefois, ces travaux ont souvent pour objectif de montrer que les cellules qui émergent de cet algorithme ont les mêmes caractéristiques que celle observée en neurophysiologie (Rehn, Loxley).
D’autres algorithmes utilisent des non-linéarités qui implémentent de façon implicite des règles homéostatiques dans des algorithmes neuro-mimétiques (Gerstner et Brito). Ces non-linéarités sont majoritairement utilisées dans la sortie des couches successives des réseaux d’apprentissage profond qui sont massivement utilisés de nos jours pour la classification d’images ou l’intelligence artificielle.
Toutefois la plupart de ces règles de normalisation non-linéaire sont basées sur des heuristiques imitant les mécanismes neuronaux mais ne sont pas justifiées comme partie intégrante de l’algorithme non supervisé à partir de la descente de gradient sur le coût de représentation.

Il est important de noter à ce point que les algorithmes d’apprentissage utilisés en intelligence artificielle peuvent nous apporter un nouvel éclairage sur le fonctionnement de ces processus neuraux et notamment sur l'apprentissage non supervisé.
Dans le domaine de l’apprentissage machine, l’apprentissage non supervisé correspond en effet à l’apprentissage de dictionnaires de représentation quand les données de catégorisation sont inconnues. Cet apprentissage est donc effectué de façon autonome et il est notamment utilisé en compression d’image et du signal, en détection d'objets, en séparation de sources mais aussi pour la diminution du bruit dans des signaux bruts.
À ce titre, cette classe d’algorithmes est extrêmement utile dans les premières couches des algorithmes d’intelligence artificielle comme les algorithmes profonds.
Il existe de nombreuses variantes de tels algorithmes qui prennent la forme soit d’une optimisation du transfert d'information (Bell), soit sous la forme de règles d’apprentissages dans l’apprentissage profond ou encore sous la forme d’algorithmes récursifs en statistiques et probabilités avec par exemple la poursuite de projection.
Une classe importante de ces algorithmes considère que l’ensemble des solutions qui vont être considérées sont celles qui correspondent à un codage optimal. Ces solutions prennent la forme d’un codage parcimonieux c’est-à-dire pour lequel pour lequel un petit nombre de composantes seront sélectionnés par rapport à la taille du dictionnaire.
Ce principe est assez général pour être appliqué à de nombreuses classes de signaux et permettre une analyse mathématique de ce problème (Donoho).
En particulier nous avons montré précédemment qu’un algorithme rapide de codage de type parcimonieux peut être implémenté dans une architecture de type normal neural (Perrinet, 2010).
Aussi, il a été montré qu’un tel codage permet d’améliorer des algorithmes de classification en particulier en limitant le nombre de couches nécessaires dans un algorithme d’apprentissage profond permettant la classification de d'images contenant ou ne contenant pas des animaux (Perrinet et Bednar, 2015).
Toutefois, des études récentes semblent remettre en cause ce principe de codage parcimonieux (Eichhorn 2009, Zoran et Weiss 2012) et suggère qu’une analyse plus simple appliquée dans une métrique complexe est suffisante pour expliquer émergence de filtres sélectifs à l’orientation similaires à ceux observés dans le cortex visuel primaire.

Afin d’offrir une perspective plus large sur ce problème, nous allons essayer de l’exprimer sous la forme générique d’un problème probabiliste.
Cette approche est déjà largement exploitée dans les travaux anciens de Barlow sous le terme de principe de réduction de redondance (voir aussi Atick).
Ils ont conduit à traduire ce problème d’apprentissage en terme de codage efficace par exemple en implémentant des règles d’inhibition dans le champ récepteur de la rétine chez le tigre à dents de sabre (Srinivasan, 1981).
D’autres études montrent que ces règles reviennent à imposer au système d'être proche d'une limite de criticalité et à optimiser la balance entre optimisation du codage et de l'apprentissage (Beggo, 2008 in Sandin)
Plus généralement, nous nous placerons dans le cadre de la théorie de minimisation de l’énergie libre formulée par Karl Friston. Ce principe permet de poser explicitement le problème du codage et de l'apprentissage non supervisé, aussi durant l’apprentissage.
Dans cette théorie, l'apprentissage n'est plus un but en lui-même mais participe à la minimisation de l'énergie libre à différentes échelles de temps, depuis le codage à l'apprentissage mais aussi au temps intermédiaire de l'homéostasie.
Selon ce principe, le but global de de système neural est de pouvoir au mieux prévoir n'importe quelle entrée sensorielle. Ce principe se traduit par des modifications de la structure de la population (connections synaptiques)).
Le but de l'apprentissage et simplement de ne pas être surpris par l'entrée sensorielle.
À ce titre, le but de l'apprentissage et d'obtenir un codage qui soit le moins variables a priori, c'est-à-dire avant d'avoir reçu l'information sensorielle.
D'une part, cette théorie étend celle d'Olshausen et montre alors que l'homéostasie a aussi une part prédictive qui va permettre de surcroit de formuler une théorie normative du code neural à l'échelle de temps de l'homéostasie en l'associant à des mécanismes d'adaptation (Rao Balard).
Ainsi, l'ensemble des processus aux différentes échelles de temps sont ainsi considéré dans une et même théorie normative.

``>>> LUP IS HERE <<<<``
Ce papier est organisé suivant le plan suivant.
Tout d’abord nous montrerons l’importance de l’homéostasie dans les algorithmes d’apprentissage non supervisé. Nous dériverons une règle optimal pour l’adaptation homéostatique basée sur une égalisation de l’histogramme.
Nous montrerons ensuite des résultats quantitatifs de cet algorithme optimal en l’appliquant à différents couples dalgorithmes de codage et d’apprentissage.En utilisant différentes bases d’apprentissage nous pourrons donner une analyse quantitative qui permettra de comparer ces différentes solutions.
Nous délivrerons ensuite un algorithme neuro-mimétique d’homéostasie dérivé à partir de la règle optimale grâce à une simple heuristique.
Nous comparerons alors les résultats de ce nouvel algorithme avec l’algorithme optimal ainsi qu’avec d'autres algorithmes existant d’apprentissage non supervisé.
De par sa nature, cet algorithme peut facilement être étendu à des réseaux de type convolutionnels du type de ceux utilisés en apprentissage profond.
Cette extension est possible en étendant le dictionnaire de filtre par l’hypothèse d’une invariances à la translation des représentations.
Nos résultats sur différentes bases d’apprentissage montre l’émergence stable et rapide de filtres caractéristiques à ces différentes bases. Ce résultat montre un e perspective probable d'extension de cette représentation  et pour lesquelles nous espérons obtenir des résultats de classification supérieurs aux algorithmes existant dans l'état-de-l'art.
Enfin nous conclurons en montrant l’importance de l’homéostasie dans les algorithmes d'apprentissage non supervisés.
En développant cet algorithme rapide d’apprentissage nous espérons son application rapide dans des algorithmes d’intelligence artificielle.
Ce type d’architecture est à la fois économique, efficace et rapide. Il  permet de renouveler l’ensemble des algorithmes de type algorithme profonds dont le défaut majeur est d'être très gourmands en ressources de calcul.
Notamment, nous envisageons des perspectives pour les réseaux dynamiques et nous espérons appliquer ce type d’algorithme sur des systèmes embarqués du types de robots aériens.
En parallèle, nous espérons ainsi que ce nouveau type d’algorithme rapide d’apprentissage non supervisé puisse fournir une théorie normative pour le codage de l’information dans le traitement sensoriel de bas niveau, qu’il soit par exemple visuel ou auditif.

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
