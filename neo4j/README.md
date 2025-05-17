## Trying out NEO4j graph database. 
docker pull neo4j
docker run \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --restart always \
    --volume=$HOME/neo4j/data:/data \
    --env NEO4J_AUTH=neo4j/your_password \
    --name neo4j-apoc \
    -d \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS='["apoc", "apoc-extended"]' \
     neo4j

http://neo4j.com/docs/operations-manual/current/deployment/single-instance/docker/

Locally running the python pieces. 

uv venv
uv pip install langchain_neo4j langchain_ollama langchain langchain_community neo4j langchain_experimental  json-repair
uv run --with jupyter jupyter lab

Then use that URL to run the jupyter Notebook. 
Login into the browser on the hostIP Address at localhost:7474
use your credentials to log into the Browser. 