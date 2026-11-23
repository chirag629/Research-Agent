
from research_agent.ingestion.schemas import Document
from pathlib import Path
import fitz

class PDFLoader:

    def load(self,file_path:str) -> Document :
        exact_path = Path(file_path)

        if not exact_path.exists():
            raise FileNotFoundError(f"PDF not found at {file_path}")

        if exact_path.suffix.lower() != ".pdf" :
            raise ValueError("File Must be a PDF")

        pages = []

        with fitz.open(exact_path) as pdf :

            for page_number, page in enumerate(pdf,start=1):
                text = page.get_text("text")

                pages.append( f"\n--- Page {page_number} ---\n {text}")

            metadata = pdf.metadata or {}
            page_count = len(pdf)

        content = "\n".join(pages)


loader = PDFLoader()
loader.load("C://Users//cga5//Desktop//a.pdf")