from typing import List

from openagent.schema import BaseRetriever, Document
from openagent.knowledgebase.utilities.pupmed import PubMedAPIWrapper


class PubMedRetriever(BaseRetriever, PubMedAPIWrapper):
    """
    It is effectively a wrapper for PubMedAPIWrapper.
    It wraps load() to get_relevant_documents().
    It uses all PubMedAPIWrapper arguments without any change.
    """

    def get_relevant_documents(self, query: str) -> List[Document]:
        return self.load_docs(query=query)

    async def aget_relevant_documents(self, query: str) -> List[Document]:
        raise NotImplementedError("Pupmed retriever does not support async")