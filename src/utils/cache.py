"""Simple cache implementation for API responses"""
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class CacheEntry:
    data: Any
    timestamp: datetime
    
class Cache:
    def __init__(self, timeout: timedelta):
        self._cache: Dict[str, CacheEntry] = {}
        self.timeout = timeout
    
    def get(self, key: str) -> Optional[Any]:
        if key in self._cache:
            entry = self._cache[key]
            if datetime.now() - entry.timestamp < self.timeout:
                return entry.data
            del self._cache[key]
        return None
    
    def set(self, key: str, value: Any) -> None:
        self._cache[key] = CacheEntry(
            data=value,
            timestamp=datetime.now()
        )