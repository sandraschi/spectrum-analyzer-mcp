from typing import Annotated, Literal
from fastmcp.tools import ToolResult
from pydantic import Field
from spectrum_analyzer_mcp.app import mcp

_CONNECTED = False

@mcp.tool()
async def spec_device(
    operation: Annotated[Literal["list", "connect", "disconnect", "status"], Field()],
    device_id: Annotated[str | None, Field()] = None,
) -> ToolResult:
    global _CONNECTED
    try:
        if operation == "list":
            return ToolResult(content={"success": True, "devices": [{"device_id": "sim-spec-001", "backend": "simulator"}]})
        if operation == "connect":
            _CONNECTED = True
            return ToolResult(content={"success": True, "device_id": device_id or "sim-spec-001"})
        if operation == "disconnect":
            _CONNECTED = False
            return ToolResult(content={"success": True})
        return ToolResult(content={"success": True, "connected": _CONNECTED})
    except Exception as exc:
        return ToolResult(content={"success": False, "error": str(exc)})

@mcp.tool()
async def spec_run(
    operation: Annotated[Literal["scan", "peak_find", "preview", "status"], Field()],
    value: Annotated[float | None, Field()] = None,
    address: Annotated[str | None, Field()] = None,
) -> ToolResult:
    try:
        data = {"operation": operation, "simulated": True, "value": value, "address": address}
        return ToolResult(content={"success": True, "data": data})
    except Exception as exc:
        return ToolResult(content={"success": False, "error": str(exc)})

@mcp.tool()
async def spec_help(
    operation: Annotated[Literal["quickstart", "discover", "status"], Field()] = "quickstart",
) -> ToolResult:
    return ToolResult(content={
        "success": True,
        "tools": ["spec_device", "spec_run", "spec_help"],
        "operation": operation,
    })
