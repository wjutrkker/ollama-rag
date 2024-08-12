# this requires ollama webui to be running in the background. 

from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import Ollama

from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


import os
import getpass
from fileTypes import load_all_docs
# test your ollama integration
llm = Ollama(base_url='http://localhost:11434', model="llama3.1:8b")


# Load the document, split it into chunks, embed each chunk and load it into the vector store.

# raw_documents = DirectoryLoader("/data", glob="*/*", show_progress=True, use_multithreading=True, silent_errors=False).load()
raw_documents = load_all_docs("/data")

# split the documents into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts= []
for document in raw_documents:
    texts.append(text_splitter.split_documents(document))
# texts = 

# select which embeddings we want to use
embeddings = OllamaEmbeddings(base_url='http://localhost:11434',model="llama3.1:8b")
# create the vectorestore to use as the index
breakpoint()
if os.path.isdir("/data/chroma_db"):
    db = Chroma(embedding_function=embeddings, persist_directory="/data/chroma_db")
else:
    db = Chroma.from_documents(texts[7], embeddings, persist_directory="/data/chroma_db")

# expose this index in a retriever interface
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})
# create a chain to answer questions 
qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)


query = "Can you summarize this the Readme.md file"
result = qa({"query": query})
print(result)