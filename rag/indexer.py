# rag/indexer.py
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import AsyncQdrantClient

from .settings import *
from .configs.secret import (
    QDRANT_HOST,
    QDRANT_API_KEY,
    QDRANT_COLLECTION_NAME,
)

if __name__ == "__main__":
    DOCUMENT_DIR = "./data"
    documents = SimpleDirectoryReader(DOCUMENT_DIR).load_data()

    aclient = AsyncQdrantClient(
        host=QDRANT_HOST, port=6333, api_key=QDRANT_API_KEY, timeout=60
    )
    vector_store = QdrantVectorStore(
        aclient=aclient, collection_name=QDRANT_COLLECTION_NAME, prefer_grpc=True
    )
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        use_async=True,
    )
    print(index)
