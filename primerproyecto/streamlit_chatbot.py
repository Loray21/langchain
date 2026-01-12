from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage , HumanMessage, SystemMessage
import streamlit as st
from langchain.prompts import PromptTemplate

# Configurar la pagina de la app
st.set_page_config(page_title= "Chatbot Basico", page_icon="")
st.title("Chatbot Basico Langchain")
st.markdown("Este es un *chatbot de ejemplo* contruido con LangChain + StreamLit.Escribe tu mensaje abajo para comenzar!")

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature=0.7, api_key="AIzaSyDM4NZMOyQXRnRDudCZMJbnwBn28ECt764")

with st.sidebar:
    st.header("Configuracion")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.5, 0.1)
    model_name = st.selectbox(
    "Modelo",
    [
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro"
    ]
)
    llm = ChatGoogleGenerativeAI(model = model_name, temperature=temperature,  api_key="AIzaSyDM4NZMOyQXRnRDudCZMJbnwBn28ECt764")


## Crear Prompt template con comportamiento especifico

prompt_template = PromptTemplate(
    input_variables = ["mensaje", "historial"],
    template= """Eres un asistente util y confiable llamado chat pro.
    
    Historial de conversacion: 
    {historial}

    Responde de manera clara y concisa a la siguiente pregunta: {mensaje}
    """
)


## crear cadena usando LCEL(Langchain Expression Language)
cadena = prompt_template | chat_model

# Inicializar historial de mensajes 

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

# Mostrar mensajes previos en la interfaz
for msg in st.session_state.mensajes:
    if isinstance(msg , SystemMessage):
        # No muestro el mensaje por pantalla porque son de systema como prompting
        continue

    role = "assistant" if isinstance(msg, AIMessage) else "user"

    with st.chat_message(role):
        st.markdown(msg.content)

## Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escriba tu mensaje: ")

if pregunta:
    # Mostar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)
    
    # Almacenamos el mensaje en la memoria de streamlist
    st.session_state.mensajes.append(HumanMessage(content=pregunta))

    respuesta = llm.invoke(st.session_state.mensajes)

    # Mostrar respuesta en la interfaz

    with st.chat_message("assistant"):
        st.markdown(respuesta.content)

    st.session_state.mensajes.append(respuesta)




