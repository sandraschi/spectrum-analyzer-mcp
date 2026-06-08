async def run_stdio(mcp_app) -> None:
    await mcp_app.run_stdio_async(show_banner=False)
