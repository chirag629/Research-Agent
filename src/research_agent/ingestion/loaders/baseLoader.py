from typing import Protocol
from research_agent.ingestion.schemas import Document

class baseLoader(Protocol):
    def load(self,file_path:str)-> Document:
        ...
