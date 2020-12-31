# Multilingual Information Extraction With Machine Translation: A Pipeline Experiment Using Japanese Wikipedia

This file gives a breakdown of research into how well machine translation works as part of an information extraction pipeline. This research was conducted for a dissertation presented in partial fulfillment for an MA in Computational Linguistics. The full paper has also been included in the repository. 

Information Extraction (IE) is the task of extracting machine-readable data from unstructured
text. More specifically it's focussed on mapping relations between entities or events and timelines. Extracted information is often stored in a structured way such as in a database. 

This process often includes multilingual information. This is especially true of text found on the internet. Monolingual systems have trouble with this increasingly used text, hence the need for this research. 

As I am famililar with Japanese, I have tested using text written in this language, translated to English using machine translation. 

Steps are outlined here and code mentioned is included in the repository. Conclusions also summarised.

## Data

For data collection, Wikipedia articles were chosen. These are useful for IE as they are written in a consistently structured way useful for traning machine learning models. They have resources for many languages, and building a corpus using them is easy using wikidumps. 

A wikidump provides a collection of Wikipedia articles listed on Wikipedia in a specific language and for a specified date. This can be performed with open-source Python modules and usually extracts articles, including image placement, infoboxes, reference links, and text body in an XML file. A wikidump of Japanese articles can be found at http://shinra-project.info/?lang=en categorised by Sekine's Extended Named Entity Heirarchy (see https://www.semanticscholar.org/paper/Extended-Named-Entity-Hierarchy-Sekine-Sudo/f664c4a6aee50411f1db79999fd5e7c88a35b926) and is used in this project. 

## Data Cleaning/Processing
As there were a lot of obscure Japanese figures without much text, only articles with English equivalents were kept (en_link_check.py). 

Landing pages where article names were ambiguous included in the wikidump were removed (remove_incorrect_articles.py)

Example set of articles collected (getting_test_data.py)

Titles of articles were then mapped to Q numbers used to query Wikidata for labels used to train the classifiers (mapping_titles.py). (See https://pypi.org/project/wikimapper/)

Meta information was removed from articles so only text remained in articles before translation step (translation_preprocess.py).

## Translation
Articles were ran through Microsoft Azure to save time at this experimental stage (mstranslate.py, translate_dataset.py). 

Future implementations should use Huggingface transformers trained on the the Helsinki OPUS ja-en available: https://huggingface.co/Helsinki-NLP/opus-mt-ja-en?

## Wikidata labels 

