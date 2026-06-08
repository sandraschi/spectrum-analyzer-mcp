from fastmcp import FastMCP

mcp = FastMCP(
    "SpectrumAnalyzerMCP",
    instructions="RTL-SDR / TinySA spectrum tools and simulator. Portmanteau: spec_device, spec_run, spec_help.",
    on_duplicate="replace",
)

@mcp.resource("resource://spec/quickstart")
def quickstart() -> str:
    return "1. spec_device(operation='connect') 2. spec_run(operation='scan')"

@mcp.resource("resource://spec/capabilities")
def capabilities() -> str:
    return "# spectrum-analyzer-mcp\nSimulator + planned hardware backends."
