from pathlib import Path


from research_agent.ingestion.schemas import Document
from research_agent.ingestion.loaders.registry import LoaderRegistry
class IngestionPipeline :

    def __init__(self,registry=None):
        self.registry = registry or LoaderRegistry()

    def ingest(self , file_path:str) -> Document:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found : {file_path}"
            )
        
        loader = self.registry.getLoader(str(path))
        return loader.load(str(path.resolve()))
