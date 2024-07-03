# create folder which will contains the used data
mkdir toLoad
cd toLoad

# create the query
echo "PREFIX dataid: <http://dataid.dbpedia.org/ns/core#>
PREFIX dataid-cv: <http://dataid.dbpedia.org/ns/cv#>
PREFIX dataid-mt: <http://dataid.dbpedia.org/ns/mt#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcat:  <http://www.w3.org/ns/dcat#>

# Get latest ontology NTriples file 
SELECT DISTINCT ?file WHERE {
 	?dataset dataid:artifact <https://databus.dbpedia.org/denis/ontology/dbo-snapshots> .
	?dataset dcat:distribution ?distribution .
        ?distribution dcat:mediaType dataid-mt:ApplicationNTriples . 
	?distribution dct:hasVersion ?latestVersion .  
	?distribution dcat:downloadURL ?file .

	{
	SELECT (?version as ?latestVersion) WHERE { 
		?dataset dataid:artifact <https://databus.dbpedia.org/denis/ontology/dbo-snapshots> . 
		?dataset dct:hasVersion ?version . 
	} ORDER BY DESC (?version) LIMIT 1 
	} 
	
} " > query

# use dockerized databus-client to downlaod files
docker run --name databus-client \
    -v $(pwd)/query:/opt/databus-client/query \
    -v $(pwd):/var/repo \
    -e FORMAT="ttl" \
    -e COMPRESSION="gz" \
    dbpedia/databus-client

# move file in the right place
mv -t ./ $(find . -name "*.gz")

# remove
docker rm databus-client

docker run --name my-virtuoso \
    -p 8895:8890 -p 1111:1111 \
    -e DBA_PASSWORD=dba \
    -e SPARQL_UPDATE=true \
    -e DEFAULT_GRAPH=http://dbpedia.org/ontology \
    -v $(pwd):/data \
    -d openlink/virtuoso-opensource-7