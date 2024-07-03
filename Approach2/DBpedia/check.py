from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setQuery("""
    SELECT (COUNT(?person) AS ?count) WHERE {
      ?person a dbo:Person .
    }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

count = int(results["results"]["bindings"][0]["count"]["value"])
print("Number of dbo:Person entities in DBpedia:", count)
