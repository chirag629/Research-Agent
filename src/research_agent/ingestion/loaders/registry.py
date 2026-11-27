from pathlib import Path
from research_agent.ingestion.loaders.pdf_loader import PDFLoader
from research_agent.ingestion.loaders.text_loader import TextLoader
class LoaderRegistry :

    def __init__(self):
        self._loaders = {}

        self.register(".pdf",PDFLoader())
        self.register(".txt",TextLoader())
        self.register(".md",TextLoader())

    def register(self,extension: str, loader):
        extension = extension.lower()

        if not extension.startswith("."):
            extension = f".{extension}"

        self._loaders[extension] = loader

    def getLoader(self , file_path:str):
        
        extension = Path(file_path).suffix.lower()

        loader = self._loaders.get(extension)

        if loader is None:
            raise ValueError(
                f"No loader registered for extension :{extension}"
            )

        return loader

