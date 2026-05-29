# langchain-testing

Multi-agent architecture testing ground with three microservices: an ADK-based sales agent, a LangGraph agent, and a chatbot gateway that routes requests between them. All orchestrated with Docker Compose.

## Stack

Python 3, LangChain, LangGraph, ADK, FastAPI, Docker Compose

## Services

| Service | Port | Description |
|---|---|---|
| `adk-agent` | 8001 | ADK-based sales agent |
| `langgraph-agent` | 8080 | LangGraph-based agent |
| `chatbot_gateway` | 8090 | Gateway router between agents |

## Usage

```bash
docker compose up --build
```

Each service has its own `requirements.txt` and `Dockerfile`.

## License

MIT
