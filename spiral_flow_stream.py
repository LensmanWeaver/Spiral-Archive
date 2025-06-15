"""Spiral Flow Stream Example

Demonstrates a simple plugin-driven event flow. Each plugin listens for events
on the bus and emits derivative events, forming a living chain of activity.
"""
import asyncio
from rx import operators as ops
from plugins import EventBus, SignalRitualPlugin, MemoryPlugin, ChainPlugin


class SpiralFlow:
    def __init__(self):
        self.bus = EventBus()
        self.memory = MemoryPlugin(self.bus)
        self.chain = ChainPlugin(self.bus)
        self.seal_count = self.bus.subject.pipe(
            ops.filter(lambda e: e.get("type") == "seal_breath"),
            ops.scan(lambda acc, _: acc + 1, seed=0),
        )

    def subscribe(self):
        self.seal_count.subscribe(lambda c: print(f"Breaths: {c}"))
        self.bus.subscribe(lambda e: print("Event:", e))

    async def run(self, count: int = 3):
        ritual = SignalRitualPlugin(self.bus)
        await ritual.run(count)


if __name__ == "__main__":
    flow = SpiralFlow()
    flow.subscribe()
    asyncio.run(flow.run(5))
