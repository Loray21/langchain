from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

chat = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", temperature=0.7, api_key="AIzaSyDM4NZMOyQXRnRDudCZMJbnwBn28ECt764")

plantilla = PromptTemplate(
    input_variables=["nombre"],
    template = "Saluda usuario con su nombre.\n Nombre del usuario: {nombre}\Asistente:"

)


chain = plantilla | chat


resultado = chain.invoke({"nombre": "Carlos"})


print(resultado.content)


