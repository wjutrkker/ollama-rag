from langchain_community.graphs import Neo4jGraph
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_experimental.graph_transformers import LLMGraphTransformer



os.environ["NEO4J_URI"] = "bolt://192.168.86.35:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "your_password"

graph = Neo4jGraph()


llm = Ollama(base_url='http://192.168.86.35:11434', model="llama3.1:8b")
llm_transformer = LLMGraphTransformer(llm=llm)


from langchain_neo4j import Neo4jGraph

graph = Neo4jGraph()
"""
CREATE CONSTRAINT DeviceUniqueName UNIQUE (device(systemName));

CLASS CybersecurityDocument
LABEL document;
 
PROPERTY systemName;
PROPEReT systemOwner;
PROPERTY vulnerabilityType;
PROPERTY severityLevel;
PROPERTY documentDate;
"""