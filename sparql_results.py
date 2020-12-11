# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import pandas as pd
from qnumbers import values

endpoint_url = "https://query.wikidata.org/sparql"

query = """SELECT ?item ?itemLabel ?dobLabel ?occupationLabel ?placeofbirthLabel ?dateofdeath ?sexLabel ?positionLabel ?educationLabel
WHERE
{
  VALUES ?item { %s }
  OPTIONAL { ?item wdt:P569 ?dob . }
  OPTIONAL { ?item wdt:P106 ?occupation . }
  OPTIONAL { ?item wdt:P19 ?placeofbirth . }
  OPTIONAL { ?item wdt:P570 ?dateofdeath . }
  OPTIONAL { ?item wdt:P21 ?sex . }
  OPTIONAL { ?item wdt:P39 ?position . }
  OPTIONAL { ?item wdt:P69 ?education . }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ja". }
}
ORDER BY ?item ?itemLabel ?dobLabel ?occupationLabel ?placeofbirthLabel ?dateofdeath ?sexLabel ?positionLabel ?educationLabel
""" % (values)


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

keys = ['item', 'dateofdeath', 'itemLabel', 'dobLabel', 'occupationLabel', 'placeofbirthLabel', 'sexLabel', 'positionLabel', 'educationLabel']

final_results =[]

for result in results['results']['bindings']:
    
    holder_list = []
    for key in keys:
        try:
            holder_list.append(result[key]['value'])
        except:
            holder_list.append('none')
    
    final_results.append(holder_list)
        
results_df = pd.DataFrame(final_results, columns=keys)
results_df.to_csv('df15_ja.csv')