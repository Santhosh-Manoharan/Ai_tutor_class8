# Curriculum-Based AI Tutor - Class 8 Science
## Project Report

### 1. Introduction

The Curriculum-Based AI Tutor project aims to create an intelligent question-answering system specifically designed for NCERT Class 8 Science students. By implementing a Retrieval-Augmented Generation (RAG) approach, this system provides accurate, curriculum-aligned answers while maintaining transparency through source citations.

### 2. Approach

#### 2.1 Data Preparation
- **Source Material**: NCERT Class 8 Science textbook (13 chapters)
- **PDF Processing**: Extracted text from 14 PDF files including 13 chapter PDFs and 1 index PDF
- **Content Organization**: Structured data into chapters with proper numbering and titles
- **Text Chunking**: Split documents into 200-word chunks with 20-word overlap for better retrieval

#### 2.2 Embedding and Indexing
- **Embedding Model**: `sentence-transformers/all-MiniLM-L6-v2` for efficient semantic encoding
- **Vector Storage**: FAISS (Facebook AI Similarity Search) for fast similarity search
- **Index Creation**: Generated 305 text chunks with 384-dimensional embeddings

#### 2.3 RAG Pipeline
- **Retrieval**: Semantic search using cosine similarity to find relevant textbook content
- **Generation**: Integration with Ollama's Llama-2 model for answer generation
- **Prompt Engineering**: Carefully crafted prompts to ensure curriculum alignment and grade-appropriate responses
- **Fallback Mechanisms**: Context-based responses when LLM generation fails

#### 2.4 System Architecture
- User Query - Semantic Search - Context Retrieval - LLM Generation - Answer + Sources



### 3. Implementation Details

#### 3.1 Key Components
1. **Data Processor**: Handles PDF extraction, cleaning, and chunking
2. **Embedding Engine**: Creates semantic vectors for all text chunks
3. **FAISS Index**: Enables fast similarity search for relevant content
4. **Retrieval System**: Finds top-k most relevant chunks for any query
5. **Generation Module**: Uses Ollama Llama-2 to create natural language answers
6. **Response Formatter**: Ensures proper citation and grade-appropriate language

#### 3.2 Quality Controls
- **Curriculum Alignment**: Strict adherence to NCERT textbook content
- **Source Transparency**: Every answer includes chapter citations
- **Out-of-Scope Handling**: Graceful responses for non-curriculum queries
- **Grade-Appropriate Language**: Simple, clear explanations for Class 8 students

### 4. Evaluation Results

#### 4.1 Metrics Summary
- **Average BLEU Score**: 0.050
- **Average ROUGE-L Score**: 0.301

#### 4.2 Performance Analysis
The evaluation of 10 diverse Class 8 Science questions showed:
- Strong performance on factual questions with specific textbook content
- Effective handling of out-of-scope queries
- Accurate source citation for all responses
- Grade-appropriate language and explanations

#### 4.3 Key Strengths
 **Factual Accuracy**: All answers grounded in NCERT textbook content
 **Transparency**: Clear source citations for every response
 **Curriculum Compliance**: Strict adherence to Class 8 Science syllabus
 **Robustness**: Graceful handling of various query types

### 5. Challenges and Limitations

#### 5.1 Technical Challenges
- **Semantic Retrieval**: Some complex queries required expanded context retrieval
- **LLM Integration**: Balancing detailed responses with factual accuracy
- **Chunking Strategy**: Optimizing chunk size for different content types

#### 5.2 Content Limitations
- **Textbook Coverage**: Limited to available NCERT textbook content
- **Depth vs Breadth**: Some topics require more detailed explanation than available text

### 6. Future Work

#### 6.1 Immediate Improvements
- **Enhanced Chunking**: Implement hierarchical chunking for better context retrieval
- **Multi-Model Support**: Integrate additional lightweight models for specific topics
- **Interactive Features**: Add diagram explanation and visual learning aids

#### 6.2 Advanced Features
- **Progressive Learning**: Track student queries to identify learning patterns
- **Quiz Generation**: Automatically generate practice questions from textbook content
- **Multilingual Support**: Extend to regional languages for wider accessibility
- **Voice Interface**: Add speech-to-text and text-to-speech capabilities

#### 6.3 Scalability
- **Multi-Grade Support**: Extend to other classes (6-10) in the NCERT curriculum
- **Subject Expansion**: Add Mathematics, Social Science, and other subjects
- **Cloud Deployment**: Host on cloud platforms for wider accessibility

### 7. Conclusion

The Curriculum-Based AI Tutor successfully demonstrates the effectiveness of RAG approaches for educational applications. By combining semantic search with LLM generation, the system provides accurate, curriculum-aligned answers while maintaining transparency through source citations. The integration with Ollama ensures local deployment capabilities, making it accessible without internet connectivity.

The project achieves its core objectives of:
- Providing fact-based answers from NCERT curriculum
- Maintaining grade-appropriate language and explanations
- Ensuring transparency through source citations
- Handling out-of-scope queries gracefully

This foundation provides a robust platform for future enhancements and expansion to support comprehensive science education for Class 8 students.

---
