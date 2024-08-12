FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel
USER root
RUN apt-get update && apt-get install -y git

RUN pip install langchain 
RUN pip install llama_index
RUN pip install unstructured unstructured[md]
RUN pip install sentence-transformers
RUN pip install vecs
RUN pip install chromadb
RUN pip install "unstructured[all-docs]"
RUN pip3 install langchain_community


ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
RUN apt-get install -y tzdata
RUN apt-get install -y libgl1-mesa-dev ffmpeg
RUN pip3 install llama-parse
RUN pip3 install git+https://github.com/openai/whisper.git
RUN pip3 install llama-index-core
RUN pip3 install llama-index-embeddings-openai
RUN pip3 install llama-index-postprocessor-flag-embedding-reranker
RUN pip3 install git+https://github.com/FlagOpen/FlagEmbedding.git
RUN pip3 install docx2txt
RUN pip3 install llama-index-llms-langchain
RUN pip3 install llama-index --upgrade --no-cache-dir --force-reinstall
RUN pip install llama-index qdrant_client torch transformers 
RUN pip install llama-index-llms-ollama




# ENTRYPOINT [ "python3", "/code/databasechromadb.py" ]