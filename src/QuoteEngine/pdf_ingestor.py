"""Implementation for pdf file format by creating pdftotext subprocess."""
import os
import random
import subprocess
from typing import List

from .ingestor_interface import IngestorInterface, UnsupportedExtensionError
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """An ingestor that processes pdf format.

    Passing other extension will raise UnsupportedExtensionError
    """

    supported_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse qoutes from pdf file with specified path."""
        if not cls.can_ingest(path):
            raise UnsupportedExtensionError('Cannot ingest this extension')

        quotes = []
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'

        try:
            call = subprocess.call(['pdftotext', path, tmp])
            with open(tmp, 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n\r').strip()
                    if len(line) > 0:
                        body, author = line.replace('"', '').split(' - ')
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        finally:
            os.remove(tmp)

        return quotes
