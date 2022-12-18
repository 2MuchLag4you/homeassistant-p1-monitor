from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from custom_components.p1mon.tasks import fetch
from custom_components.p1mon.models import ( 
    Settings, 
    SmartMeter, 
    Phases
)

@dataclass
class p1mon:

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self._fetched_data = {}

    async def request(self) -> dict[str, Any]:
        if not bool(self._fetched_data):
            self._fetched_data = await fetch(self.host, self.port)

        return self._fetched_data

    async def clear(self) -> None:
        self._fetched_data = {}

    async def phases(self) -> Phases:
        fetched_data = await self.request()
        return Phases.process(fetched_data)
    
    async def settings(self) -> Settings:
        fetched_data = await self.request()
        return Settings.process(fetched_data)
    
    async def smartmeter(self) -> SmartMeter:
        fetched_data = await self.request()
        return SmartMeter.process(fetched_data)       

    async def __aenter__(self) -> p1mon:
        """Return p1 Object on Async enter"""
        return self

    async def __aexit__(self, *_exc_info) -> None:
        return None