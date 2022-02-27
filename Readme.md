### Midterm Project For Univerisity

## Edible or Not?: Exploring the relation between features basedon the Agaricus and Lepiota Mushrooms Families

#### Introduction

Mushrooms are the spore (fungi reproductive cell) bearing fruiting body of a fungus. With more than 14,000
species of mushrooms classified and over 50,000 other species, most are edible, few are actually consumed,
some are hallucinogenic, and some are poisonous.
With cap colours displaying the entire visible spectrum, different habitats, range of odors, stalks, veils, rings,
spores, and gills the classification of mushrooms has lots of different variables. If we want to eat a mushroom
taken from the wild it would be helpful to know if there exist some patterns, relations, and characteristics that
can allow us to make and educated guess on the edibility of the mushroom, without risking our own health.
This project was inspired by my own curiosity that lead me to go for walks into the forests, research into fungi
and ultimately, the forage and collection of wild mushrooms.

#### Data source, usefulness and ethics

With image classification via machine learning growing day by day there are many mushrooms datasets that
cointain thousands of images of mushroom species. The problem with these is that the dataset do not contain
the attributes of each image (mushroom) this leads to machine learning models to generalize the attributes by
finding patters based on what the image portray, leading to inaccurate results.

The dataset chosen is the mushroom-classification dataset originally contributed to the UCI Machine Learning
repository in the 27 April 1987, in this time period mushroom hunting was gaining popularity and thus, 23
attributes per species of gilled mushrooms in the Agaricus and Lepiota Family Mushroom were drawn from
The Audubon Society Field Guide to North American Mushrooms (1981.)

This is especially useful when trying to find hard correlations between features and mushroom edibility. Each
species is identified as definitely edible, definitely poisonous, or of unknown edibility and not recommended.
This latter class was combined with the poisonous one.

This dataset is open to the public by the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication License and
accesible via the link: https://www.kaggle.com/uciml/mushroom-classification therefore no anonymisation of
data is required. Other mushroom datasets like https://www.kaggle.com/huhao05133/mushrooms?
select=Mushrooms.csv are just subsets of this one and https://www.kaggle.com/maysee/mushrooms-
classification-common-genuss-images contain only images.

Any person or entity with the desire of using this data is free to do so as the dataset is open to the public, and
this paper is released under the MIT License. All the analysis and conclusions are my own. Please be aware
that the analysis made are purely informational and educational and the dataset does not cover all the
species of mushrooms found in the wild. The results are only applicable to this and only this dataset and
should not be used as a certain guide to mushroom classification

#### Aims & Objectives

Explore the dataset to find out which attributes have the most number of variations. Example:
Are there more gill or cap colors?
Make hypotesis based on mushroom characteristics and compare them to results obtained from the
data. 
Examples:
- Are bright color mushroom poisonous?
- Are good smelling mushroom edible?
- Use the mushroom attributes (headers) in the dataset to find any type of correlation between them and
- the edibility of any given mushroom Examples:
- What is the realtion between the cap and gill colors in the mushrooms
- What mushroom shape trends to be more poisonous
- Create a foraging summary that diplays the traits that make the mushroom always and most of the times
- edible ot poisonous Example:
- All x mushrooms are edible
- Find and describe flaws in the dataset and my own analysis methods

This paper will not cover the complex inter-relations of non-generalized attribute

#### Results:

Mushroom Foraging Summary:

*Edible Attributes*
- All green, and purple color cap
- 70% white, and cinnamon color cap
- All Sunken shape cap are edible
- 89.5% bell shape cap
- All "Nice" smelling (almond, anise)
- Most none smelling (~97%)
- All orange, and red gill color
- 88.4% black, brown, purple, and 77.5% white, yellow gill color
- All buff, orange, purple and yellow spore-prints
- 88% black and brown spore prints
- All gray, orange, red stalk color
- 61.7% white stalk color
- ~73% fibrous, scaly, and smooth stalks shapes
- 91.4% crowded gill-spaced are edible

*Poisonous Attributes*
- All conical shape cap
- 72.3% knobbed shape cap
- 71.7% buff, 60.5% pink, yellow and red color cap
- All "Foul" smelling (fishy,foul,musty,...)
- All buff, green gill colors
- 69.8% chocolate and gray gill color
- All chocolate and green spore-prints
- 75.8% white spore prints
- All brown, buff, cinnamon, yellow stalks color
- 69.5% pink stalk color
- All silky stalk shape
- 88.4% narrow gill-size are poisonous

*Flaws*

The poisonous chance plot function uses rates, if the data is not balanced or vastly one-sided it will not portray the best representative values


Resources Used:
https://en.wikipedia.org/wiki/Mushroom#classification
http://www.ikonet.com/en/visualdictionary/static/us/edible_mushrooms#:~:text=There%20are%20over%2050%2C000%20species,used%20for%20their%20medicinal%20properties.
https://www.kaggle.com/uciml/mushroom-classification
https://seaborn.pydata.org/generated/seaborn.countplot.html#seaborn.countplot
https://seaborn.pydata.org/tutorial/categorical.html#showing-multiple-relationships-with-facets
https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_and_donut_labels.html#sphx-glr-gallery-pie-and-polar-charts-pie-and-donut-labels-py