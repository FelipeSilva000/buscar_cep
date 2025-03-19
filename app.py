import requests 
import streamlit as st 

def buscar_cep(cep):
    endpoint = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(endpoint)
    localizacao = response.json() if response.status_code ==200 else ""
    return localizacao
  
    
st.title("Digite seu CEP:")

cep = st.text_input("Cep:", key="cep")
pesquisar = st.button("Pesquisar")

if pesquisar:
    localizacao = buscar_cep(cep)
    if localizacao: 
        st.success("Encontramos seu cep : ")
        st.write(f"**CEP:** {localizacao.get('cep', 'N/A')}")
        st.write(f"**Logradouro:** {localizacao.get('logradouro', 'N/A')}")
        st.write(f"**Bairro:** {localizacao.get('bairro', 'N/A')}")
        st.write(f"**Cidade:** {localizacao.get('localidade', 'N/A')}")
        st.write(f"**Estado:** {localizacao.get('uf', 'N/A')}")
        st.write(f"**DDD:** {localizacao.get('ddd', 'N/A')}")
    else:
        st.error("Nao foi possivel encontrar esse cep !")
