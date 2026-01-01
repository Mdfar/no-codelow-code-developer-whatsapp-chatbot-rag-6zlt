from fastapi import FastAPI, Request import openai import pinecone from typing import List

app = FastAPI()

Initialize Pinecone and OpenAI

openai.api_key = "YOUR_OPENAI_API_KEY" pc = pinecone.Pinecone(api_key="YOUR_PINECONE_API_KEY") index = pc.Index("whatsapp-knowledge-base")

@app.post("/query") async def handle_whatsapp_query(request: Request): data = await request.json() user_query = data.get("text")

# 1. Generate Embedding for user query
query_vector = openai.embeddings.create(
    input=user_query,
    model="text-embedding-3-small"
).data[0].embedding

# 2. Retrieve Context from Pinecone
results = index.query(vector=query_vector, top_k=3, include_metadata=True)
context = " ".join([res.metadata['text'] for res in results.matches])

# 3. Generate Answer using RAG
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"Answer the user based on this context: {context}"},
        {"role": "user", "content": user_query}
    ]
)

return {"answer": response.choices[0].message.content}


if name == "main": import uvicorn uvicorn.run(app, host="0.0.0.0", port=8000)