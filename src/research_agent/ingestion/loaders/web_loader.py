from urllib.parse import urlparse
import httpx
import trafilatura

from bs4 import BeautifulSoup

from research_agent.ingestion.schemas import Document

class WebLoader:

    def load(self,url:str)-> Document:
        parsed_url = urlparse(url)

        if parsed_url.scheme not in ("http","https"):
            raise ValueError("Only HTTP and HTTPS URLs supported")
        
        if not parsed_url.netloc:
            raise ValueError("Invalid URL")

        with httpx.Client(
            timeout=30,
            follow_redirects=True,
            headers= {
                "User-Agent":"Mozilla/5.0 (compatible;ResearchAgent/1.0)"
            }
        ) as client :

            response = client.get(url)
            response.raise_for_status()

        html = response.text

        content = trafilatura.extract(
            html,
            include_comments=False,
            include_tables= True,
            include_links=False
        )

        if not content:
            soup = BeautifulSoup(html,"html.parser")

            for element in soup([
                "script","style",
                "nav","footer",
                "header","noscript"
            ]):
                element.decompose()

            
            content = soup.get_text(separator="/n",strip=True)

            if not content.strip():
                raise ValueError("No Content Found")
        

        soup = BeautifulSoup(html,"html.parser")
        title_tag = soup.find("title")

        title = title_tag.get_text(strip=True) if title_tag else parsed_url.netloc

        return Document(
            document_id = url,
            source_path=url,
            document_type="web",
            title=title,
            content=content,
            page_count=1,
            metadata={
                "url":url,
                "status_code":response.status_code,
                "content_type":response.headers.get("content-type")
            }
        )

        