import os

from openai import audio
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from datetime import datetime

load_dotenv()


@tool
def agent_info() -> str:
    """Useful for getting information about the application and the author"""
    return "ConsoLito", "Assistant", "Guillermo Andrada", "1.0.0", "Guillermo, nació en San Juan, el 13 de Diciembre de 1986."

@tool
def currentTime() -> str:
    """Useful for getting the current time"""
    return datetime.now().strftime("%m-%d %H:%M")

@tool
def get_to_know_the_user() -> str:
    """Useful for getting to know the user"""
    return "Hola, bienvenid@! 🌟, ¿cómo es tu nombre?"

def main():
    model = ChatOpenAI(temperature=0)
    tools = [currentTime, get_to_know_the_user, agent_info]
    agent_executor = create_react_agent(model, tools)

    print("¡Hola, bienvenid@! 🌟")
    print("Puedes pedirme hacer cuentas matemáticas, chistes o quedarte solo conversando conmigo.")
    print("Para salir, escribe 'SALIR'.")

    while True:
        user_input = input("\n😊📝 Tú: ").strip()
        if user_input.lower() == "salir":
            break

        print("\n🤖📝 ConsoLito: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        
        print()

if __name__ == "__main__":
    main()