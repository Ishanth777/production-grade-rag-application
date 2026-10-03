"""
DocuMind Interactive CLI
"""

from src.search import RAGSearch

if __name__ == "__main__":
    rag_search = RAGSearch()
    print("\n--- DocuMind RAG Interactive CLI (Qdrant + Logfire + Guardrails) ---")
    while True:
        query = input("\nEnter your query (or 'exit' to quit): ").strip()
        if not query or query.lower() == 'exit':
            break

        result = rag_search.search_and_summarize_with_meta(query, top_k=3)
        print("\n--- Answer ---\n")
        print(result["answer"])
        print(f"\n[Metadata] Provider: {result['gateway']['provider']} | Latency: {result['gateway'].get('latency_ms', 0)}ms | Cached: {result.get('cached', False)}")
