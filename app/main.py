import os
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import requests

load_dotenv()

# Configuration
st.set_page_config(
    page_title="LLM Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "not-needed")
BASE_URL = os.getenv("BASE_URL", "http://model-runner:12434/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "ai/smollm2:135M-Q4_K_M")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "500"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY, base_url=BASE_URL)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "model_status" not in st.session_state:
    st.session_state.model_status = "unknown"

# Function to check model health
def check_model_health():
    try:
        # Remove /v1 from base URL for health check
        health_url = BASE_URL.replace("/v1", "") + "/v1/models"
        response = requests.get(health_url, timeout=5)
        if response.status_code == 200:
            return "healthy", "🟢"
        return "unhealthy", "🔴"
    except Exception as e:
        return f"error: {str(e)}", "🔴"

# Header
st.title("🤖 Docker Model Runner Chatbot")
st.markdown("*Isolated LLM deployment using Docker Model Runner*")

# Sidebar
with st.sidebar:
    st.header("⚙️ System Status")
    
    # Model health check
    if st.button("🔄 Check Model Status"):
        status, indicator = check_model_health()
        st.session_state.model_status = status
    
    if st.session_state.model_status != "unknown":
        st.info(f"{indicator} Model Status: {st.session_state.model_status}")
    
    st.divider()
    
    # Configuration display
    st.header("📋 Configuration")
    st.code(f"Model: {MODEL_NAME}", language="text")
    st.code(f"Endpoint: {BASE_URL}", language="text")
    st.code(f"Max Tokens: {MAX_TOKENS}", language="text")
    st.code(f"Temperature: {TEMPERATURE}", language="text")
    
    st.divider()
    
    # Controls
    st.header("🎛️ Controls")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Stats
    st.header("📊 Statistics")
    st.metric("Total Messages", len(st.session_state.messages))
    st.metric("User Messages", len([m for m in st.session_state.messages if m["role"] == "user"]))
    st.metric("Assistant Messages", len([m for m in st.session_state.messages if m["role"] == "assistant"]))

# Main chat interface
st.markdown("---")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("💬 Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("🤔 Thinking..."):
            try:
                # Prepare messages
                api_messages = [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
                
                # Call the model
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=api_messages,
                    max_tokens=MAX_TOKENS,
                    temperature=TEMPERATURE,
                    stream=False
                )
                
                # Extract and display response
                assistant_message = response.choices[0].message.content
                message_placeholder.markdown(assistant_message)
                
                # Add to history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
            except Exception as e:
                error_msg = f"❌ **Error:** {str(e)}"
                message_placeholder.error(error_msg)
                
                # Add helpful debug info
                with st.expander("🔍 Debug Information"):
                    st.write("**Configuration:**")
                    st.json({
                        "base_url": BASE_URL,
                        "model_name": MODEL_NAME,
                        "error": str(e)
                    })
                    st.write("**Troubleshooting Steps:**")
                    st.markdown("""
                    1. Check if model runner is healthy: `docker-compose ps`
                    2. View logs: `docker-compose logs model-runner`
                    3. Verify network: `docker network ls`
                    4. Test endpoint: `curl http://localhost:12434/v1/models`
                    """)

# Footer
st.markdown("---")
st.caption("🐳 Powered by Docker Model Runner | 🚀 Built with Streamlit")