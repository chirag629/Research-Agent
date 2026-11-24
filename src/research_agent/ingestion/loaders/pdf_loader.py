
from research_agent.ingestion.schemas import Document
from pathlib import Path
import pymupdf

class PDFLoader:

    def load(self,file_path:str) -> Document :
        exact_path = Path(file_path)

        if not exact_path.exists():
            raise FileNotFoundError(f"PDF not found at {file_path}")

        if exact_path.suffix.lower() != ".pdf" :
            raise ValueError("File Must be a PDF")

        pages = []

        with pymupdf.open(exact_path) as pdf :

            for page_number, page in enumerate(pdf,start=1):
                text = page.get_text("text")

                pages.append( f"\n--- Page {page_number} ---\n {text}")

            metadata = pdf.metadata or {}
            page_count = len(pdf)

        content = "\n".join(pages)

        return Document(
            document_id=exact_path.stem ,
            source_path= str(exact_path.resolve()),
            document_type = "pdf",
            title=metadata.get("title") or exact_path.stem,
            content=content,
            page_count=page_count,
            metadata=metadata
            )