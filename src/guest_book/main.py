# FastAPI
from fastapi import FastAPI

# Others
from guest_book.core.config import settings

app = FastAPI(title=settings.TITLE,
              openapi_tags=settings.TAGS_METADATA)