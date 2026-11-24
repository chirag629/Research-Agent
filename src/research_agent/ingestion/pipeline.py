from pathlib import Path

from research_agent.ingestion.loaders.baseLoader import baseLoader
from research_agent.ingestion.schemas import Document
class IngestionPipeline :

    def __init__(self,loader:baseLoader):
        self.loader = loader

    def ingest(self , file_path:str) -> Document:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found : {file_path}"
            )
        
        return self.loader.load(str(path))
