"""Implementation for csv file format using pandas."""
import pandas as pd
from typing import List

from .ingestor_interface import IngestorInterface, UnsupportedExtensionError
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """An ingestor that processes csv format.

    Passing other extension will raise UnsupportedExtensionError
    """

    supported_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse qoutes from csv file with specified path."""
        if not cls.can_ingest(path):
            raise UnsupportedExtensionError('Cannot ingest this extension')

        quotes = []
        df = pd.read_csv(path)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
