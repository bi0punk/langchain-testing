# langchain-testing

Multi-agent architecture testing ground with three microservices: an ADK-based sales agent, a LangGraph agent, and a chatbot gateway that routes requests between them. All orchestrated with Docker Compose.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![CI](https://github.com/bi0punk/langchain-testing/actions/workflows/ci.yml/badge.svg)](https://github.com/bi0punk/langchain-testing/actions/workflows/ci.yml)

## Tabla de Contenidos

- [Características](#características)
- [Stack](#stack)
- [Arquitectura](#arquitectura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Configuración](#configuración)
- [CI](#ci)
- [Seguridad](#seguridad)
- [Limitaciones / Roadmap](#limitaciones--roadmap)
- [Licencia](#licencia)

## Características

- Tres microservicios independientes con agentes de IA
- ADK Agent: agente de ventas conversacional
- LangGraph Agent: agente con flujo de grafo basado en LangGraph
- Chatbot Gateway: router inteligente entre agentes
- Comunicación entre servicios via red Docker interna
- CORS restringido (no wildcard) para desarrollo local

## Stack

- Python 3.11+, LangChain, LangGraph, ADK, FastAPI, Docker Compose

## Arquitectura

```
langchain-testing/
├── adk-agent/              # ADK sales agent
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── langgraph-agent/        # LangGraph agent
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── chatbot_gateway/        # Gateway router
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── docker-compose.yml
├── tests/
├── pyproject.toml
├── .env.example
└── README.md
```

## Servicios

| Servicio           | Puerto | Descripción                    |
|--------------------|--------|--------------------------------|
| `adk-agent`        | 8001   | Agente de ventas ADK           |
| `langgraph-agent`  | 8080   | Agente LangGraph               |
| `chatbot_gateway`  | 8090   | Gateway router entre agentes   |

## Requisitos

- Docker Engine 24+
- Docker Compose v2
- API keys para LLMs (OpenAI, etc.)

## Instalación

```bash
git clone https://github.com/bi0punk/langchain-testing.git
cd langchain-testing
cp .env.example .env
# Editar .env con API keys
```

## Uso

```bash
docker compose up --build
```

Los servicios se inician y el gateway centraliza las peticiones en `http://localhost:8090`.

## Tests

```bash
docker compose run --rm chatbot_gateway pytest
docker compose run --rm adk-agent pytest
docker compose run --rm langgraph-agent pytest
```

## Configuración

CORS y comunicación entre servicios:

| Variable          | Default          | Descripción                        |
|-------------------|------------------|------------------------------------|
| `ALLOW_ORIGINS`   | `localhost`      | Orígenes CORS permitidos           |
| `OPENAI_API_KEY`  | —                | API key de OpenAI                  |

## CI

GitHub Actions ejecuta ruff lint + pytest en cada push y PR.

## Seguridad

- CORS origins restringidos (no wildcard)
- Servicios se comunican sobre red interna Docker bridge
- Los puertos individuales de agentes no se exponen externamente

## Limitaciones / Roadmap

- [ ] Añadir más agentes (RAG, herramientas externas)
- [ ] Autenticación entre servicios (API keys)
- [ ] Monitoreo con tracing distribuido (LangSmith)
- [ ] Despliegue en Kubernetes

## Licencia

MIT
