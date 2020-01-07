# Example Projects

A collection of data analysis-oriented projects by Paige McKenzie. 

Table of Contents
======
[Allrecipes.com text analysis](#allrecipes-text)

[Allrecipes.com Hall of Fame analysis](#allrecipes-hof)

[Bachelor Finale twitter analysis](#bachelor-finale)

[Edmunds reviews analysis](#Edmunds)

[Jane Austen text analysis](#Jane)

[Wake County Restaurants analysis](#wake-county)

<a name="allrecipes-text"/>

## Allrecipes.com text analysis

A multi-part project involving getting data from [Allrecipes.com](http://www.allrecipes.com)'s
various categories.

See my 1st [blog post](https://p-mckenzie.github.io/2018/08/06/Allrecipes-categories-scraper/) of the project (covering the scraping).

See my 2nd [blog post](https://p-mckenzie.github.io/2018/10/01/ingredient-analysis/) of the project (covering the analysis).

Files:
```
+-- Allrecipes text analysis
    --scraper.py
    --analysis.ipynb
    --requirements.txt
```

Software:
The data scraping used Chromedriver 2.41 for Windows. Make sure to update the file to include the path to your chromedriver.
Package requirements can be found in `requirements.txt`.

<a name="allrecipes-hof"/>

## Allrecipes.com Hall of Fame

A project leveraging both R and Python to acquire data from [Allrecipes.com](http://www.allrecipes.com)'s
yearly Hall of Fame collections.

See my [blog post](https://p-mckenzie.github.io/2018/02/23/allrecipes-hall-of-fame/) concerning this project.

Required files:
```
+-- Allrecipes Hall of Fame
    --allrecipes_scraper.py
    --allrecipes_analysis.Rmd
```

Software:
The data scraping was with Python 3.5.1, Selenium 3.6.0, using Chromedriver 2.35 for Windows. Make sure to update the file to include the path to your chromedriver.

Analysis was completed in RStudio using R 3.4.1, requiring on dplyr, ggplot2, corrplot, ggthemes, wordcloud, and tm.

<a name="bachelor-finale"/>

## Bachelor Finale twitter analysis

A project leveraging Python and the twitter API to acquire tweets about the bachelor season 22 finale and After the Final Rose.

See my [blog post](https://p-mckenzie.github.io/2018/03/12/Bachelor-finale/) concerning this project.

Required files:
```
+-- twitter - Bachelor finale
    --Scraper.ipynb
    --Analysis.ipynb
```

Software:
All analysis was completed using Python 2.7, relying primarily on the pandas, re, and nltk libraries. 
The data was extracted from twitter using python-twitter, a python-based wrapper for the twitter API.
Visualizations made with matplotlib.

<a name="Edmunds"/>

## Edmunds reviews analysis

A text-analytics microproject using a dataset from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/opinrank+review+dataset).

See my [blog post](https://p-mckenzie.github.io/content/2017/11/16/edmunds-reviews/) concerning this project.

Required files:
```
+-- Edmunds analysis.ipynb
+-- cars
    --2007
       --data files
    --2008
       --data files
    --2009
       --data files
```
Data files available from the [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/opinrank+review+dataset).

Software:
Python 2.7, relying on Pandas, Bokeh 0.12.13

<a name="Jane"/>

## Jane Austen text analysis

A text-analytics microproject using a three novels written by Jane Austen: Emma, Pride and Prejudice, and Sense and Sensibility.

See my [blog post](https://p-mckenzie.github.io/content/2018/01/11/Jane-Austen/) concerning this project.

Required files:
```
+-- Jane Austen analysis.ipynb
+-- Emma.txt
+-- Sense and Sensibility.txt
+-- Pride and Prejudice.txt
```
Data files available from [Project Gutenberg](https://www.gutenberg.org/).

Software:
Python 2.7, relying on pandas, re, nltk, and Bokeh 0.12.13

## Wake County Restaurants analysis

Simulating a marketing campaign to target restaurants "at-risk" of failing their next inspection using North Carolina public restaurant inspection data.

See my [blog post](https://p-mckenzie.github.io/2019/07/22/Wake-county-restaurants/) concerning this project.

Required files:
```
+-- Wake_county_restaurants.ipynb
```
Data courtesy of Wake County Open Data (pulled 7/3/19):
* [Restaurants](https://data-wake.opendata.arcgis.com/datasets/restaurants-in-wake-county)
* [Inspections](https://data-wake.opendata.arcgis.com/datasets/food-inspections)
* [Violations](https://data-wake.opendata.arcgis.com/datasets/food-inspection-violations)

Software:
Python 3.7, relying on pandas, sklearn.
