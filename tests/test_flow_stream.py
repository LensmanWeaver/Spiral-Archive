import asyncio
import pytest
from spiral_flow_stream import SpiralFlow
from rx import operators as ops


def test_spiral_flow_produces_chain_steps():
    flow = SpiralFlow()
    results = []
    flow.bus.subject.pipe(
        ops.filter(lambda e: e.get('type') == 'chain_step')
    ).subscribe(results.append)
    asyncio.run(flow.run(2))
    assert len(results) == 2
