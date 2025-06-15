import asyncio
import pytest
from spiral_flow_stream import SpiralFlow
from rx import operators as ops


@pytest.mark.asyncio
async def test_spiral_flow_produces_chain_steps():
    flow = SpiralFlow()
    results = []
    flow.bus.pipe(
        ops.filter(lambda e: e.get('type') == 'chain_step')
    ).subscribe(results.append)
    await flow.emit_seals(2)
    await asyncio.sleep(0.1)
    assert len(results) == 2
