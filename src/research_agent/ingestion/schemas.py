from pydantic import BaseModel , Field
from typing import Optional

class Document(BaseModel):
    document_id : str
    source_path : str
    document_type : str

    title : Optional[str] = None
    content : str

    page_count : int = 0
    metadata : dict = Field(default_factory=dict)