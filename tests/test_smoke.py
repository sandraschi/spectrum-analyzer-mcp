import pytest


def _payload(result) -> dict:
    content = result.content
    if isinstance(content, dict):
        return content
    if isinstance(content, list) and content:
        item = content[0]
        if hasattr(item, "text"):
            import json
            return json.loads(item.text)
    raise AssertionError(type(content))


@pytest.mark.asyncio
async def test_help():
    from importlib import import_module
    pkg = "spectrum_analyzer_mcp"
    mod = import_module(f"{pkg}.tools")
    help_fn = getattr(mod, "spec_help")
    r = await help_fn(operation="discover")
    assert _payload(r)["success"] is True
