# spectrum-analyzer-mcp

FastMCP 3.2+ — **Spectrum Analyzer MCP**. RTL-SDR / TinySA spectrum tools and simulator.

## Quick start

```powershell
Set-Location D:\Dev\repos\spectrum-analyzer-mcp
uv sync --extra dev
uv run python -m spectrum_analyzer_mcp --stdio
```

## Tools

- `spec_device` — list, connect, disconnect, status
- `spec_run` — scan, peak_find, preview, status
- `spec_help` — quickstart, discover, status

## Ports

Backend: **11007** · Frontend: **11008** (webapp planned)

## Fleet

Part of the Sandra bench MCP family with oscilloscope-mcp and logic-analyzer-mcp.
