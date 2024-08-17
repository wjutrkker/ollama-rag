README

Working on the RAG pieces. 

install ollama locally like before. 

curl https://ollama.ai/install.sh | sh
ollama serve


git clone git@github.com:wjutrkker/ollama-rag.git
cd ollama-rag
DATA_PATH=$PWD

docker build -t ollama-rag:latest .  
docker run -it --network host -v $PWD:/code -v $DATA_PATH:/data ollama-rag:latest bash

cd /code
python3 databasechromadb.py