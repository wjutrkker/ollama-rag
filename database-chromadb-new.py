# this requires ollama webui to be running in the background. 

from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.llms import Ollama
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from langchain.chains import RetrievalQA
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
# breakpoint()
if os.path.isdir("/data/chroma_db"):
    db = Chroma(embedding_function=embeddings, persist_directory="/data/chroma_db")
else:
    db = Chroma.from_documents(texts[7], embeddings, persist_directory="/data/chroma_db")

# expose this index in a retriever interface
retriever = db.as_retriever(search_type="similarity", search_kwargs={"k":2})

prompt = ChatPromptTemplate.from_messages(
    [
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
        (
            "user",
            "Given the above conversation, generate a search query to look up to get information relevant to the conversation",
        ),
    ]
)

retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Answer the user's questions based on the below context:\n\n{context}",
        ),
        ("placeholder", "{chat_history}"),
        ("user", "{input}"),
    ]
)
document_chain = create_stuff_documents_chain(llm, prompt)

qa = create_retrieval_chain(retriever_chain, document_chain)

question = "Can you tell me about anything Ollama?"
result = qa.invoke({"input": question})
print(result["answer"])