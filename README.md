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

## Bench family

One bench, nine servers. `bench-orchestrator-mcp` conducts (`mcu_bringup` drives
its six wired peers); the rest are instruments. This server is family, not a
wired peer — it joins sessions manually (EMI and emissions around the target):

| Server | Role | Wired peer? |
|--------|------|-------------|
| [bench-orchestrator-mcp](https://github.com/sandraschi/bench-orchestrator-mcp) | Conductor — `bench_workflow` (`power_check`, `bus_check`, `debug_check`, `mcu_bringup`) | — (it conducts) |
| [jtag-swd-mcp](https://github.com/sandraschi/jtag-swd-mcp) | Halt / inspect / flash the CPU | yes (`dbg`) |
| [oscilloscope-mcp](https://github.com/sandraschi/oscilloscope-mcp) | Scope traces — signal integrity | yes (`scope`) |
| [logic-analyzer-mcp](https://github.com/sandraschi/logic-analyzer-mcp) | Digital capture + UART/I2C/SPI decode | yes (`la`) |
| [multimeter-mcp](https://github.com/sandraschi/multimeter-mcp) | DMM — rails, continuity | yes (`dmm`) |
| [power-supply-mcp](https://github.com/sandraschi/power-supply-mcp) | Bench PSU — target power | yes (`psu`) |
| [function-generator-mcp](https://github.com/sandraschi/function-generator-mcp) | AWG stimulus — clocks, reset, fault injection | yes (`fgen`) |
| [bench-camera-mcp](https://github.com/sandraschi/bench-camera-mcp) | Bench vision — LEDs, 7-segment | family (not wired) |
| `spectrum-analyzer-mcp` (here) | Spectrum — EMI around the target | family (not wired) |
