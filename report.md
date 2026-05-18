# Curriculum-Based AI Tutor - Class 8 Science (v1.2)
## Project Report

### 1. Introduction

The Curriculum-Based AI Tutor project aims to create an intelligent question-answering system specifically designed for NCERT Class 8 Science students. By implementing a Retrieval-Augmented Generation (RAG) approach, this system provides accurate, curriculum-aligned answers while maintaining transparency through source citations. Version 1.2 focuses on creating a self-contained system by integrating local LLM generation.

### 2. Approach

#### 2.1 Data Preparation
- **Source Material**: NCERT Class 8 Science textbook (13 chapters)
- **PDF Processing**: Extracted text from 14 PDF files including 13 chapter PDFs and 1 index PDF (pre-processed into `class8_science.jsonl`)
- **Content Organization**: Structured data into chapters with proper numbering and titles
- **Text Chunking**: Split documents into 200-word chunks with 20-word overlap for better retrieval

#### 2.2 Embedding and Indexing
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2` for efficient semantic encoding
- **Vector Storage**: FAISS (Facebook AI Similarity Search) for fast similarity search
- **Index Creation**: Generated 305 text chunks with 384-dimensional embeddings

#### 2.3 RAG Pipeline
- **Retrieval**: Semantic search using cosine similarity to find relevant textbook content
- **Generation (v1.2)**: Integration with local Hugging Face Transformers model (`distilgpt2`) for self-contained answer generation, replacing previous external dependencies.
- **Prompt Engineering**: Optimized prompts to guide the local LLM in using the retrieved context effectively.
- **Fallback Mechanisms**: Context-based responses when LLM generation is unavailable.

#### 2.4 System Architecture
- User Query - Semantic Search - Context Retrieval - Local LLM Generation - Answer + Sources

### 3. Implementation Details

#### 3.1 Key Components
1. **Data Processor**: Handles JSONL loading and chunking.
2. **Embedding Engine**: Creates semantic vectors for all text chunks.
3. **FAISS Index**: Enables fast similarity search for relevant content.
4. **Retrieval System**: Finds top-k most relevant chunks for any query.
5. **Generation Module (v1.2)**: Uses `distilgpt2` to create natural language answers from retrieved context.
6. **Web Interface**: Streamlit-based UI for easy interaction.

#### 3.2 Quality Controls
- **Curriculum Alignment**: Strict adherence to NCERT textbook content.
- **Source Transparency**: Every answer includes chapter citations.
- **Self-Containment**: Minimal external dependencies for core functionality.

### 4. Evaluation Results (v1.2)
The system was verified to correctly load the RAG components, retrieve relevant textbook sections (e.g., Chapter 8 for "force"), and generate readable natural language answers.

### 5. Challenges and Limitations
- **Local Model Capacity**: Lightweight models like `distilgpt2` may occasionally produce repetitive text, but provide a good balance for environment compatibility.
- **Dependency Management**: Successfully resolved environment-specific issues with `torchvision` and `transformers` versions.

### 6. Future Work
- **Model Upgrades**: Explore more advanced local models (e.g., Phi-3, Llama-3-8B) as environment resources allow.
- **Interactive UI**: Add more visualizations for retrieved sources.

### 7. Conclusion
Version 1.2 of the Class 8 Science AI Tutor successfully achieves a self-contained, RAG-powered educational tool. By moving to local Transformers-based generation, it ensures reliability and accessibility for students.
