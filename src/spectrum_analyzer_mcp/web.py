from typing import Any
from fastapi import FastAPI
from spectrum_analyzer_mcp import __version__

def setup_webapp(app: FastAPI, mcp: Any) -> None:
    @app.get("/health")
    async def health():
        return {"status": "ok", "server": "spectrum-analyzer-mcp", "version": __version__}

    @app.get("/api/status")
    async def status():
        tools = await mcp.list_tools()
        return {"status": "ok", "tools": [t.name for t in tools], "version": __version__}

    @app.get("/api/capabilities")
    async def capabilities():
        tools = await mcp.list_tools()
        return {
            "status": "ok",
            "server": {"name": "spectrum-analyzer-mcp", "version": __version__},
            "tool_surface": {"total": len(tools)},
            "runtime": {"backend_port": 11007, "frontend_port": 11008},
        }
