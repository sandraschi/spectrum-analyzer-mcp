set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
serve:
    uv run python -m spectrum_analyzer_mcp
lint:
    uv run ruff check .
test:
    uv run pytest tests/ -v
mcpb-pack:
    $ver = "0.1.0"
    New-Item -ItemType Directory -Path dist -Force
    npx --yes @anthropic-ai/mcpb@latest validate .
    npx --yes @anthropic-ai/mcpb@latest pack . "dist/spectrum-analyzer-mcp-v$ver.mcpb"
