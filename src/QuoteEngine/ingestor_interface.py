from abc import ABC, abstractmethod
from typing import List

from .quote_model import QuoteModel


class IngestorInterface(ABC):
    """An abstract base class that defines the interfaces of an ingestor

    The helper classes must complete the parsing logic
    """
    supported_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check whether file extension is compatible"""
        extension = path.split('.')[-1]
        return extension in cls.supported_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file content and output it to a list of quote objects"""
        pass


class UnsupportedExtensionError(Exception):
    """Exception that will be raised if the file extension is not supported"""
    pass
