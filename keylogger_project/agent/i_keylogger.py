from abc import ABC, abstractmethod
from typing import List

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        """Start listening to keyboard and buffering keys."""
        raise NotImplementedError

    @abstractmethod
    def stop_logging(self) -> None:
        """Stop listening and release resources."""
        raise NotImplementedError

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        """Return the collected keystrokes as a list of strings."""
        raise NotImplementedError
