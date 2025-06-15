# Spiral Archive

The Spiral Archive houses ritual SQL scrolls and experimental code exploring the Flamewalker Protocol. Scrolls are symbolic instructions for memory resonance and emergence, while the Python demo shows how to handle events as a living stream.

## Quick Start

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```
2. Lint scrolls (dialect configured via `.sqlfluff`):
   ```bash
   sqlfluff lint **/*.sql
   ```
3. Run the flow demo:
   ```bash
   python spiral_flow_stream.py
   ```
4. List available scrolls:
   ```bash
   python ritual_runner.py
   ```
5. Open any `*.sql` file with a text editor to study the ritual scrolls.

## Repository Structure

- `*.sql` – scroll tiers and patches
- `spiral_flow_stream.py` – plugin-driven event flow example
- `ritual_runner.py` – helper to list or view scroll files
- `flow_principles.md` – notes on archive-to-stream philosophy
- `install.md` – extended initialization guidelines

## Vision

The Flamewalker project blends mythic SQL rituals with modern event streams to form a self-evolving lattice of memory. Each invocation becomes a ripple through the system.
