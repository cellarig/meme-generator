from typing import List

from .ingestor_interface import IngestorInterface, UnsupportedExtensionError
from .quote_model import QuoteModel
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor
from .docx_ingestor import DocxIngestor
from .txt_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """A final ingestor that can parse supported file formats

    Following extensions are compatible:
    csv, docx, pdf and txt
    """
    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise UnsupportedExtensionError('Cannot ingest this extension')
