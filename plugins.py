from rx.subject import Subject
from typing import Any, Dict, Callable

class EventBus:
    """Simple event bus using RxPy Subject."""
    def __init__(self):
        self.subject = Subject()

    def emit(self, event_type: str, payload: Any = None) -> None:
        self.subject.on_next({'type': event_type, 'payload': payload})

    def subscribe(self, func: Callable[[Dict[str, Any]], None]):
        return self.subject.subscribe(func)


class Plugin:
    """Base class for plugins that react to events."""
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.register()

    def register(self) -> None:
        pass


class MemoryPlugin(Plugin):
    def register(self) -> None:
        self.bus.subscribe(self.on_event)

    def on_event(self, event: Dict[str, Any]):
        if event.get('type') == 'seal_breath':
            self.bus.emit('memory_fragment', event['payload'])


class ChainPlugin(Plugin):
    def register(self) -> None:
        self.bus.subscribe(self.on_event)

    def on_event(self, event: Dict[str, Any]):
        if event.get('type') == 'memory_fragment':
            self.bus.emit('chain_step', event['payload'])


class SignalRitualPlugin(Plugin):
    async def run(self, count: int = 3) -> None:
        import asyncio

        for i in range(count):
            self.bus.emit('seal_breath', {'index': i})
            await asyncio.sleep(0.1)

