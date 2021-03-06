"""Implementation for docx file format using python-docx."""
from typing import List
from docx import Document

from .ingestor_interface import IngestorInterface, UnsupportedExtensionError
from .quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """An ingestor that processes docx format.

    Passing other extension will raise UnsupportedExtensionError
    """

    supported_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse qoutes from docx file with specified path."""
        if not cls.can_ingest(path):
            raise UnsupportedExtensionError('Cannot ingest this extension')

        quotes = []
        doc = Document(path)

        for paragraph in doc.paragraphs:
            if paragraph.text:
                body, author = paragraph.text.replace('"', '').split(' - ')
                quote = QuoteModel(body, author)
                quotes.append(quote)

        return quotes
