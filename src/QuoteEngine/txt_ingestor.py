"""Implementation for txt file format."""
from typing import List

from .ingestor_interface import IngestorInterface, UnsupportedExtensionError
from .quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """An ingestor that processes txt format.

    Passing other extension will raise UnsupportedExtensionError
    """

    supported_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse qoutes from txt file with specified path."""
        if not cls.can_ingest(path):
            raise UnsupportedExtensionError('Cannot ingest this extension')

        quotes = []
        with open(path, 'r') as f:
            for line in f:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    body, author = line.replace('"', '').split(' - ')
                    quote = QuoteModel(body, author)
                    quotes.append(quote)

        return quotes
