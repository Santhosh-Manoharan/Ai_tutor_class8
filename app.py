# app.py
import streamlit as st
import joblib
import os
import faiss
from sentence_transformers import SentenceTransformer

# --- Configuration ---
st.set_page_config(page_title="Class 8 Science AI Tutor", page_icon="📘", layout="centered")

# --- Load AI Model ---

@st.cache_resource
def load_ai_tutor_model():
    """Load the AI Tutor model from joblib file, handling CPU-only loading"""
    try:
        if os.path.exists('tutor_model.joblib'):
           
            tutor_components = joblib.load('tutor_model.joblib')
            st.success("✅ AI Tutor model loaded successfully!")
            return tutor_components
        else:
            st.warning("⚠️ AI Tutor model file 'tutor_model.joblib' not found.")
            return None
    except Exception as e:
        error_msg = str(e)
       
        if "Attempting to deserialize object on a CUDA device" in error_msg and torch.cuda.is_available() == False:
            st.warning("⚠️ Detected CUDA/CPU compatibility issue during loading.")
            try:
                
                import pickle
                with open('tutor_model.joblib', 'rb') as f:
                    
                    data = joblib.load(f)
                
                st.success("✅ AI Tutor model loaded successfully (attempt 2)!")
                return data
            except Exception as e2:
                st.error(f"❌ Failed to load AI Tutor model (attempt 2 also failed): {e2}")
       
        st.error(f"❌ Failed to load AI Tutor model: {error_msg}")
        if "Attempting to deserialize object on a CUDA device" in error_msg:
            st.info("💡 This is a CUDA/CPU compatibility issue. The model was likely saved on a GPU machine. "
                    "Standard reloading failed. You might need to modify how the model is saved in the notebook.")
        else:
            st.info("💡 An unexpected error occurred while loading the model.")
        return None

tutor_model = load_ai_tutor_model()


def get_answer(question, model_data):
    """Get answer using the loaded RAG model."""
    if not model_data:
        return "AI model not loaded.", []

    try:
        index = model_data['index']
        chunks = model_data['chunks']
        embedding_model = model_data['embedding_model']

        # 1. Encode the question
        query_embedding = embedding_model.encode([question])
        faiss.normalize_L2(query_embedding)

        # 2. Search the FAISS index
        scores, indices = index.search(query_embedding.astype('float32'), k=3)

        # 3. Retrieve relevant chunks
        relevant_chunks = []
        for i, idx in enumerate(indices[0]):
            if idx < len(chunks):
                chunk_data = chunks[idx]
                relevant_chunks.append({
                    'content': chunk_data['content'],
                    'chapter': chunk_data['chapter'],
                    'title': chunk_data['title'],
                    'score': float(scores[0][i])
                })

        # 4. Combine context 
        if relevant_chunks:
            
            context_parts = [chunk['content'] for chunk in relevant_chunks]
            combined_context = " ".join(context_parts)
            
           
            answer = f"Based on the textbook content:\n\n{combined_context[:500]}..." 
            
            
            
        else:
            answer = "I couldn't find relevant information in the textbook."
        
        return answer, relevant_chunks

    except Exception as e:
        return f"An error occurred during processing: {e}", []

# --- UI ---
st.title("📘 Class 8 Science AI Tutor")
st.caption("Ask questions about your NCERT Class 8 Science textbook.")

# Status
if tutor_model:
    st.success("AI Tutor is Ready!", icon="✅")
else:
    st.warning("Running in Demo Mode (AI model not loaded).", icon="⚠️")

# Input
question = st.text_input("Your Question:", placeholder="e.g., What is photosynthesis?")

# Button
if st.button("Get Answer", type="primary", use_container_width=True):
    if not question:
        st.warning("Please enter a question.")
    elif tutor_model:
        with st.spinner("Thinking..."):
            answer, sources = get_answer(question, tutor_model)
        st.write("### Answer")
        st.info(answer)
        if sources:
            with st.expander("Show Sources"):
                for i, source in enumerate(sources):
                    st.markdown(f"""
                    **Source {i+1} (Score: {source['score']:.4f})**
                    - **Chapter:** {source['chapter']}
                    - **Title:** {source['title']}
                    """)
    else:
        st.info("This is a demo. In the full version, your question would be answered using the AI model.")


st.markdown("---")
st.caption("Powered by Retrieval-Augmented Generation (RAG) and NCERT Curriculum.")