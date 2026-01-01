WhatsApp AI RAG Chatbot
Setup

Vector DB: Create an index in Pinecone with 1536 dimensions (for OpenAI embeddings).

API: Deploy the api/main.py to a cloud provider (e.g., Render, Railway, or AWS Lambda).

No-Code: Import the make_blueprint into Make.com or set up a similar flow in Voiceflow.

Knowledge: Run the ingest_docs.py script to upload your PDFs/Text files into the AI's memory.

Architecture

WhatsApp: Frontend interface for user interaction.

RAG Microservice: Handles the intelligence layer (Vector search + LLM synthesis).

Pinecone: Acts as the long-term memory for the bot.