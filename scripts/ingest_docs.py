import pinecone import openai

def ingest_document(text_id, text_content): """ Chunks and embeds documentation into Pinecone for RAG retrieval """ embedding = openai.embeddings.create( input=text_content, model="text-embedding-3-small" ).data[0].embedding

index.upsert(vectors=[(text_id, embedding, {"text": text_content})])
print(f"Successfully ingested {text_id}")