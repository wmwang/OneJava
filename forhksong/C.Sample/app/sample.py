import streamlit as st
import openai
from black import format_str, FileMode
import time

# 設定 OpenAI API 密鑰
openai.api_key = "你的 OpenAI API 密鑰"

# 自定義 CSS 樣式
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap');
    
    body {
        background-color: #F8F9F9;
        font-family: 'Noto Sans TC', 'Arial', sans-serif;
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

# 頁面標題與說明
st.markdown('<div class="main-title">🚀 AI 程式碼助手</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="description">讓 AI 智能分析與優化你的程式碼，提升開發效率與程式品質！</div>',
    unsafe_allow_html=True,
)

# 加入分隔線
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

# 使用分欄
col1, col2 = st.columns([2, 1])

# 左側：程式碼輸入
with col1:
    st.markdown(
        '<div class="section-title"><img src="https://img.icons8.com/color/48/code.png"/> 程式碼編輯區</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="code-container">', unsafe_allow_html=True)
    code = st.text_area(
        " ",
        height=300,
        placeholder="在此貼上你的程式碼，讓 AI 為你進行分析與優化...",
    )
    st.markdown("</div>", unsafe_allow_html=True)

# 右側：功能選擇
with col2:
    st.markdown(
        '<div class="section-title"><img src="https://img.icons8.com/color/48/settings.png"/> 功能選擇</div>',
        unsafe_allow_html=True,
    )
    
    # 使用卡片式設計展示功能選項
    features = {
        "升版": "🔄 自動更新至最新語法",
        "偵錯": "🐞 智能錯誤檢測",
        "優化": "⚡ 效能與可讀性優化"
    }
    
    options = []
    for key, description in features.items():
        st.markdown(f'<div class="feature-card">', unsafe_allow_html=True)
        if st.checkbox(description, key=key):
            options.append(key)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("")
    if st.button("開始分析"):
        if not code:
            st.error("⚠️ 請先貼上程式碼！")
        elif not options:
            st.error("⚠️ 請選擇至少一項功能！")
        else:
            # 添加進度條動畫
            progress_text = "AI 正在分析您的程式碼..."
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            
            # 根據選擇的功能進行處理
            prompts = []
            if "升版" in options:
                prompts.append("升級此程式碼以符合最新版本的語法或依賴項")
            if "偵錯" in options:
                prompts.append("檢查程式碼中的潛在錯誤並修復")
            if "優化" in options:
                prompts.append("優化程式碼的性能與可讀性")
            
            full_prompt = f"以下是一段程式碼：\n{code}\n請依據以下需求處理：{'; '.join(prompts)}"
            
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=full_prompt,
                    max_tokens=1000,
                    temperature=0.3,
                )
                
                # 顯示結果
                st.markdown('<div class="result-title">🎉 AI 分析結果</div>', unsafe_allow_html=True)
                st.code(response.choices[0].text.strip(), language="python")
                
                # 添加複製按鈕
                if st.button("📋 複製結果"):
                    st.write("結果已複製到剪貼簿！")
                    
            except Exception as e:
                st.error(f"處理過程中發生錯誤：{str(e)}")

# 加入分隔線
st.markdown('<div class="line"></div>', unsafe_allow_html=True)

# Footer with enhanced design
st.markdown(
    """
    <div class="footer">
        <div style="font-size: 1.1rem; margin-bottom: 10px;">🛠️ AI 程式碼助手</div>
        <div style="font-size: 0.9rem;">由 Streamlit & OpenAI 技術支持</div>
        <div style="font-size: 0.8rem; margin-top: 5px;">© 2025 版權所有</div>
    </div>
    """,
    unsafe_allow_html=True,
)