import fitz
import pytest

from research_agent.ingestion.loaders.pdf_loader import PDFLoader

def test_pdf_loader(tmp_path):
    pdf_path = tmp_path / "sample.pdf"

    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((50,50),"Hello Research Agent");
    doc.save(pdf_path)
    doc.close()

    loader = PDFLoader()
    result = loader.load(str(pdf_path))


    assert result.document_type == "pdf"
    assert result.page_count == 1
    assert "Hello Research Agent" in result.content
