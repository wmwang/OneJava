import streamlit as st
import openai
from black import format_str, FileMode
import time

# Set OpenAI API key
openai.api_key = "your_openai_api_key"

# Custom CSS styles
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap');
    
    body {
        background-color: #F8F9F9;
        font-family: 'Poppins', 'Arial', sans-serif;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(120deg, #2E86C1, #3498DB, #85C1E9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 20px;
        animation: fadeIn 1.5s ease-in-out;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .description {
        font-size: 1.3rem;
        color: #34495E;
        text-align: center;
        margin-bottom: 30px;
        line-height: 1.6;
        animation: slideIn 1.5s ease-in-out;
    }
    
    @keyframes slideIn {
        0% { opacity: 0; transform: translateX(-20px); }
        100% { opacity: 1; transform: translateX(0); }
    }
    
    .section-title {
        font-size: 1.6rem;
        color: #2C3E50;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        padding: 10px;
        background: rgba(174, 214, 241, 0.1);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .section-title:hover {
        background: rgba(174, 214, 241, 0.2);
        transform: translateX(5px);
    }
    
    .section-title img {
        width: 30px;
        height: 30px;
        margin-right: 12px;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
    }
    
    .line {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent, #AED6F1, transparent);
        margin: 30px 0;
        animation: expand 2s ease-in-out;
    }
    
    @keyframes expand {
        0% { width: 0; }
        100% { width: 100%; }
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #5DADE2, #3498DB);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 1.1rem;
        font-weight: 500;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #3498DB, #2E86C1);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.3);
    }
    
    .code-container {
        border: 2px solid #AED6F1;
        border-radius: 12px;
        padding: 20px;
        background-color: #F7FBFE;
        box-shadow: 0 6px 15px rgba(174, 214, 241, 0.2);
        transition: all 0.3s ease;
    }
    
    .code-container:hover {
        box-shadow: 0 8px 25px rgba(174, 214, 241, 0.3);
        transform: translateY(-2px);
    }
    
    .result-title {
        color: #1F618D;
        font-weight: 700;
        margin-top: 25px;
        padding: 10px;
        background: linear-gradient(90deg, #EBF5FB, transparent);
        border-radius: 8px;
        animation: fadeIn 1s ease-in-out;
    }
    
    .feature-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    
    .status-message {
        padding: 10px;
        border-radius: 8px;
        margin: 10px 0;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    .footer {
        text-align: center;
        color: #95A5A6;
        margin-top: 30px;
        padding: 20px;
        background: linear-gradient(180deg, transparent, rgba(236, 240, 241, 0.5));
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page title and description
st.markdown('<div class="main-title">🚀 AI Code Assistant 🚀</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">Let AI analyze and optimize your code to enhance development efficiency and code quality!</div>',
    unsafe_allow_html=True,
)

# Add separator line
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

# Use columns
col1, col2 = st.columns([2, 1])

# Left side: Code input
with col1:
    st.markdown(
        '<div class="section-title"><img src="https://img.icons8.com/color/48/code.png"/> Code Editor</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="code-container">', unsafe_allow_html=True)
    code = st.text_area(
        " ",
        height=300,
        placeholder="Paste your code here for AI analysis and optimization...",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Right side: Feature selection
with col2:
    st.markdown(
        '<div class="section-title"><img src="https://img.icons8.com/color/48/settings.png"/> Features</div>',
        unsafe_allow_html=True,
    )
    
    # Card-style feature options
    features = {
        "Upgrade": "🔄 Update to Latest Syntax",
        "Debug": "🐞 Smart Error Detection",
        "Optimize": "⚡ Performance & Readability"
    }
    
    options = []
    for key, description in features.items():
        st.markdown(f'<div class="feature-card">', unsafe_allow_html=True)
        if st.checkbox(description, key=key):
            options.append(key)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("")
    if st.button("Start Analysis"):
        if not code:
            st.error("⚠️ Please paste your code first!")
        elif not options:
            st.error("⚠️ Please select at least one feature!")
        else:
            # Add progress bar animation
            progress_text = "AI is analyzing your code..."
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            
            # Process based on selected features
            prompts = []
            if "Upgrade" in options:
                prompts.append("upgrade the code to use latest syntax and dependencies")
            if "Debug" in options:
                prompts.append("check and fix potential errors in the code")
            if "Optimize" in options:
                prompts.append("optimize code performance and readability")
            
            full_prompt = f"Here's the code:\n{code}\nPlease process according to these requirements: {'; '.join(prompts)}"
            
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=full_prompt,
                    max_tokens=1000,
                    temperature=0.3,
                )
                
                # Show results
                st.markdown('<div class="result-title">🎉 AI Analysis Results</div>', unsafe_allow_html=True)
                st.code(response.choices[0].text.strip(), language="python")
                
                # Add copy button
                if st.button("📋 Copy Results"):
                    st.write("Results copied to clipboard!")
                    
            except Exception as e:
                st.error(f"An error occurred during processing: {str(e)}")

# Add separator line
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

# Footer with enhanced design
st.markdown(
    """
    <div class="footer">
        <div style="font-size: 1.1rem; margin-bottom: 10px;">🛠️ AI Code Assistant</div>
        <div style="font-size: 0.9rem;">Powered by Streamlit & OpenAI</div>
        <div style="font-size: 0.8rem; margin-top: 5px;">© 2025 All Rights Reserved</div>
    </div>
    """,
    unsafe_allow_html=True,
)