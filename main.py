import os
from dotenv import load_dotenv
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

@tool
def agent_info() -> str:
    """Devuelve información sobre la aplicación y el autor."""
    return "ConsoLito, Assistant, Guillermo Andrada, v1.0.0, nacido en San Juan el 13/12/1986."

@tool
def current_time() -> str:
    """Devuelve la hora actual."""
    return datetime.now().strftime("%m-%d %H:%M")

@tool
def get_to_know_user() -> str:
    """Pregunta para conocer al usuario."""
    return "Hola, bienvenid@! 🌟, ¿cómo es tu nombre?"

def main():
    model = ChatOpenAI(temperature=0)
    tools = [current_time, get_to_know_user, agent_info]

    agent = create_react_agent(model, tools)
    state = {"messages": []}

    print("¡Hola, bienvenid@! 🌟")
    print("Puedes pedirme hacer cuentas matemáticas, chistes o quedarte solo conversando conmigo.")
    print("Para salir, escribe 'SALIR'.")

    while True:
        user_input = input("\n😊📝 Tú: ").strip()
        if user_input.lower() == "salir":
            break

        # Agregar el mensaje del usuario
        state["messages"].append(HumanMessage(content=user_input))

        # Ejecutar el agente (responde una vez)
        state = agent.invoke(state)

        # Buscar el último mensaje del agente
        messages = state["messages"]
        last_message = messages[-1]

        print("\n🤖📝 ConsoLito:", last_message.content)

if __name__ == "__main__":
    main()
