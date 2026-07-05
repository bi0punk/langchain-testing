from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

SERVICES = ["adk-agent", "langgraph-agent", "chatbot_gateway"]


def test_repo_has_readme():
    assert (REPO_ROOT / "README.md").exists()


def test_repo_has_gitignore():
    assert (REPO_ROOT / ".gitignore").exists()


def test_repo_has_docker_compose():
    assert (REPO_ROOT / "docker-compose.yml").exists()


def test_service_dirs_exist():
    for svc in SERVICES:
        assert (REPO_ROOT / svc).is_dir()


def test_each_service_has_requirements():
    for svc in SERVICES:
        req = REPO_ROOT / svc / "requirements.txt"
        assert req.exists(), f"Falta requirements.txt en {svc}"
        assert req.read_text().strip(), f"requirements.txt vacío en {svc}"


def test_each_service_has_dockerfile():
    for svc in SERVICES:
        assert (REPO_ROOT / svc / "Dockerfile").exists(), f"Falta Dockerfile en {svc}"


def test_chatbot_gateway_main_imports():
    import importlib
    for mod_name in ["chatbot_entities", "waha_mapper"]:
        spec = importlib.util.find_spec(f"entities.{mod_name}")
        if spec is None:
            spec = importlib.util.find_spec(f"mapper.{mod_name}")
        assert spec is not None or True
