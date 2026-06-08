from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from spectrum_analyzer_mcp import __version__
from spectrum_analyzer_mcp.app import mcp
from spectrum_analyzer_mcp.web import setup_webapp
import spectrum_analyzer_mcp.tools  # noqa: F401

app = FastAPI(title="SpectrumAnalyzerMCP", version=__version__)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
setup_webapp(app, mcp)
app.mount("/mcp", mcp.http_app(path="/"))

def main() -> None:
    import asyncio
    from spectrum_analyzer_mcp.transport import run_stdio
    asyncio.run(run_stdio(mcp))

if __name__ == "__main__":
    main()
