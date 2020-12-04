# japanese-mt-ie-pipeline
Contains project files for experiment using Japanese machine translated text for an IE pipeline

This file gives a simple breakdown of my research into how well machine translation works as part of an information extraction pipeline. This research was conducted for a dissertation presented in partial fulfillment for an MA in Computational Linguistics. The full paper has also been included. 

Information Extraction (IE) is the task of extracting machine-readable data from unstructured
text. More specifically it's focussed on mapping relations between entities or events and timelines. Extracted information is often stored in a structured way such as in a database. 

The reason one would utilise machine learning as part of this process is that information is often multilingual. This is especially true of text found on the internet. Such text is prone to trip up monolingual systems, hence the need for this research. 

I am also famililar with Japanese, so I have tested using text written in this language, translated to English using machine translation. 

After outlining the practical steps, and demonstrating some of the code that was used for this project, I will show some of the conclusions that were drawn.

## Step 1: Data

The first step in any NLP project is the collection of data to create a corpus. For this project, Wikipedia articles were chosen. Wikipedia articles are useful for IE as they are written in a consistently structured way that are useful for traning machine learning models. They have resources for many languages, and building a corpus using them is easy using wikidumps. 

A Wikidump provides a collection of Wikipedia articles listed on Wikipedia in a specific language and for a specified date. This can be performed with open-source Python modules and usually extracts articles, including image placement, infoboxes, reference links, and text body in an XML file.
