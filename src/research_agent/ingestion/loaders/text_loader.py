from research_agent.ingestion.schemas import Document
from pathlib import Path
class TextLoader:
    SUPPORTED_EXTENSIONS = {".txt",".md"}

    def load(self, file_path:str) -> Document :
        exact_path = Path(file_path)

        content = exact_path.read_text(encoding="utf8")

        return Document(
            document_id=exact_path.stem,
            source_path=str(exact_path.resolve()),
            document_type=exact_path.suffix.lower().lstrip("."),
            title = exact_path.stem,
            content=content,
            page_count=1,
            metadata={
                "file_extension":exact_path.suffix.lower(),
                "file_size" : exact_path.stat().st_size
            }
        )