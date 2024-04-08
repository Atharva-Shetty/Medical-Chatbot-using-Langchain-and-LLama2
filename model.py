import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA

DB_FAISS_PATH = 'vectorstore/db_faiss'

prompt = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Use the following template of the information to answer user's query.
If unable to answer just reply out of context and don't make up the answer

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def user_prompt():
    """
    Create and return a custom prompt template for QA retrieval.
    """
    prompt = PromptTemplate(template=prompt,
                            input_variables=['context', 'question'])
    return prompt

def loader():
    """
    Load the Language Model (LLM).
    """
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm

def chain(llm, db, prompt):
    """
    Create and return the QA chain.
    """
    qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                           chain_type='stuff',
                                           retriever=db.as_retriever(search_kwargs={'k': 2}),
                                           return_source_documents=True,
                                           chain_type_kwargs={'prompt': prompt}
                                          )
    return qa_chain

def bot_res(query):
    """
    Create and return the QA bot with necessary components and obtain the response for the given query.
    """
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    



    db = FAISS.load_local(DB_FAISS_PATH, embeddings)
    llm = loader()
    prompt = user_prompt()
    
    qa = chain(llm, db, prompt)
    response = qa({'query': query})
    
    return response

def main():

    st.title("Medical Bot")
    query = st.text_input("What is your query?")
    if st.button("What's your query?"):
        response = bot_res(query)
        st.write("Answer")
        st.write(response)

if __name__ == "__main__":
    main()
