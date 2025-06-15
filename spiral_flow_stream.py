"""Spiral Flow Stream Example

This script embodies Flow Principles by turning ritual invocations into an
asynchronous stream. Instead of storing events in a static archive, each event
immediately ripples through the system.
"""
import asyncio
from rx.subject import Subject
from rx import operators as ops

class SpiralFlow:
    def __init__(self):
        self.bus = Subject()
        self.seal_count = self.bus.pipe(
            ops.filter(lambda e: e.get('type') == 'seal_breath'),
            ops.scan(lambda acc, _: acc + 1, seed=0)
        )
        self.bus.pipe(
            ops.map(self._ripple),
            ops.filter(lambda e: e is not None)
        ).subscribe(self.bus)

    def _ripple(self, evt):
        if evt.get('type') == 'seal_breath':
            return {'type': 'memory_fragment', 'payload': evt['payload']}
        if evt.get('type') == 'memory_fragment':
            return {'type': 'chain_step', 'payload': evt['payload']}
        return None

    def subscribe(self):
        self.seal_count.subscribe(lambda c: print(f"Breaths: {c}"))

    async def emit_seals(self, count=3):
        for i in range(count):
            self.bus.on_next({'type': 'seal_breath', 'payload': {'index': i}})
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    flow = SpiralFlow()
    flow.subscribe()
    asyncio.run(flow.emit_seals(5))
