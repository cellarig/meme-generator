"""All components that is required for this module."""
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .txt_ingestor import TextIngestor
from .ingestor import Ingestor
from .ingestor_interface import UnsupportedExtensionError
from .quote_model import QuoteModel
