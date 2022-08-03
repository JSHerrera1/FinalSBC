import pandas as pd
from SPARQLWrapper import SPARQLWrapper, JSON


def __getResults(query):
    endpoint = "https://wikidata.demo.openlinksw.com/sparql"
    sparql = SPARQLWrapper(endpoint)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)

    results = sparql.query().convert()
    return results


def __extractDataFromResults(results):
    fields = results['head']['vars']
    fieldsValue = [field + '.value' for field in fields]

    df = pd.json_normalize(results['results']['bindings'])

    for row in range(len(df)):
        for field in fieldsValue:
            if field not in df.columns:
                df.loc[row, field] = None

    try:
        df = df[fieldsValue]
        df.columns = [fields]
    except Exception as e:
        print(e)

    dataObject = []

    for index, row in df.iterrows():
        data = {}

        for field in fields:
            data[field] = row[field]

        dataObject.append(data)

    if len(dataObject) != 0:
        return dataObject[0]
    return dataObject


def getDetailOf(id):
    query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        select ?type ?name ?description
        where {{
            wd:{id} rdf:type ?type ;
                 rdfs:label ?name ;
                 rdfs:comment ?description .
        }}
    """

    results = __getResults(query)
    data = __extractDataFromResults(results)

    return data


if __name__ == "__main__":
    data = getDetailOf('Q28865')

    print(data)
