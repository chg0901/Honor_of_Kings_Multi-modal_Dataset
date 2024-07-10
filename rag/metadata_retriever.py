from typing import Any, List

from langchain_core.callbacks import (
    AsyncCallbackManagerForRetrieverRun,
    CallbackManagerForRetrieverRun,
)
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever



class MetadataRetriever(BaseRetriever):
    """Retriever that wraps a base retriever and compresses the results."""

    base_retriever: BaseRetriever
    """Base Retriever to use for getting relevant documents."""

    class Config:
        """Configuration for this pydantic object."""

        arbitrary_types_allowed = True

    def _get_relevant_documents(
            self,
            query: str,
            *,
            run_manager: CallbackManagerForRetrieverRun,
            **kwargs: Any,
    ) -> List[Document]:
        """Get documents relevant for a query.

        Args:
            query: string to find relevant documents for

        Returns:
            Sequence of relevant documents
        """
        docs = self.base_retriever.get_relevant_documents(
            query, callbacks=run_manager.get_child(), **kwargs
        )
        if docs:
            docs = list(docs)
            for i in range(len(docs)):
                if "detail" in docs[i].metadata:
                    docs[i].page_content = docs[i].metadata["detail"]
                    docs[i].metadata = {}
            return docs
        else:
            return []

    async def _aget_relevant_documents(
            self,
            query: str,
            *,
            run_manager: AsyncCallbackManagerForRetrieverRun,
            **kwargs: Any,
    ) -> List[Document]:
        """Get documents relevant for a query.

        Args:
            query: string to find relevant documents for

        Returns:
            List of relevant documents
        """
        docs = await self.base_retriever.aget_relevant_documents(
            query, callbacks=run_manager.get_child(), **kwargs
        )
        if docs:
            docs = list(docs)
            for i in range(len(docs)):
                if "detail" in docs[i].metadata:
                    docs[i].page_content = docs[i].metadata["detail"]
                    docs[i].metadata = {}
            return docs
        else:
            return []