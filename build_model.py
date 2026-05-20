import json
import joblib
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def split_document_into_chunks(document, chunk_size=200, overlap=20):
    """Split document content into smaller chunks"""
    content = document['content']
    words = content.split()
    chunks = []

    for i in range(0, len(words), chunk_size - overlap):
        chunk_words = words[i:i + chunk_size]
        if len(chunk_words) > overlap:
            chunk_text = ' '.join(chunk_words)
            chunk = {
                'chapter': document['chapter'],
                'title': document['title'],
                'content': chunk_text,
                'chunk_id': len(chunks)
            }
            chunks.append(chunk)

    return chunks

def build_model():
    # 1. Load documents
    print("Loading documents from class8_science.jsonl...")
    documents = []
    with open('class8_science.jsonl', 'r') as f:
        for line in f:
            documents.append(json.loads(line))

    # 2. Chunk documents
    print(f"Chunking {len(documents)} documents...")
    all_chunks = []
    for doc in documents:
        all_chunks.extend(split_document_into_chunks(doc))
    print(f"Created {len(all_chunks)} chunks.")

    # 3. Generate embeddings
    print("Loading embedding model...")
    embedding_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    chunk_texts = [chunk['content'] for chunk in all_chunks]
    print(f"Generating embeddings for {len(chunk_texts)} chunks...")
    embeddings = embedding_model.encode(chunk_texts, show_progress_bar=True)

    # 4. Create FAISS index
    print("Creating FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    faiss.normalize_L2(embeddings)
    index.add(embeddings.astype('float32'))

    # 5. Save model
    print("Saving model to tutor_model.joblib...")
    tutor_components = {
        'index': index,
        'chunks': all_chunks,
        'embedding_model': embedding_model
    }
    joblib.dump(tutor_components, 'tutor_model.joblib', compress=3)
    print("Done!")

if __name__ == "__main__":
    build_model()
