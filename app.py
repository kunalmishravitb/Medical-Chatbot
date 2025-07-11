from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings # Embeddings is used to convert data into vector
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers # CTransformers is used for loading data
from langchain.chains import RetrievalQA
from dotenv import load_dotenv # Loading .env
from src.prompt import *
import os

app = Flask(__name__) # FLask is a Package. Here we are passing the current module

load_dotenv() # Here all variables are loaded

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

embeddings = download_hugging_face_embeddings()

# Initializing the Pinecone
pinecone.init(api_key=PINECONE_API_KEY,
              environment=PINECONE_API_ENV)

index_name="medicalchatbot"

# Loading the index
docsearch=Pinecone.from_existing_index(index_name, embeddings)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="D:/Projects/Medical-Chatbot/model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                   model_type="llama",
                   config={'max_new_tokens':512,
                            'temperature':0.8})

qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}), # 2 similar answers we are fetching from the database
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__=='__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

