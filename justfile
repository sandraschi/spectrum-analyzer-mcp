set windows-shell := ["powershell.exe", "-NoProfile", "-Command"]
import 'scripts/just/fleet.just'
serve:
    uv run python -m spectrum_analyzer_mcp
lint:
    uv run ruff check .
test:
    uv run pytest tests/ -v
