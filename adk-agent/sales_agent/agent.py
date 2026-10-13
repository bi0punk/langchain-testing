from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from .prompts import MODEL_SYSTEM_MESSAGE
from .tools import contar_registros, get_current_date, registrar_cliente

root_agent = LlmAgent(
    name="sales_agent",
    model=LiteLlm(model="openai/gpt-4o-mini"),
    description=("Agente de ventas."),
    instruction=(MODEL_SYSTEM_MESSAGE),
    tools=[registrar_cliente, contar_registros, get_current_date],
)
