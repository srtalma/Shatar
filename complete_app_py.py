import streamlit as st
import requests
import json
import os

# Page configuration
st.set_page_config(
    page_title="مولد الشعر العربي",
    page_icon="🎭",
    layout="centered"
)

class ArabicPoetryGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.anthropic.com/v1/messages"
        self.headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01"
        }
        
        self.meters = {
            "البسيط": "مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ",
            "الطويل": "فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ",
            "الوافر": "مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ",
            "الكامل": "مُتَفَاعِلُنْ مُتَفَاعِلُنْ مُتَفَاعِلُنْ",
            "الهزج": "مَفَاعِيلُنْ مَفَاعِيلُنْ",
            "الرجز": "مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ",
            "المتقارب": "فَعُولُنْ فَعُولُنْ فَعُولُنْ فَعُولُنْ",
            "الرمل": "فَاعِلاتُنْ فَاعِلاتُنْ فَاعِلاتُنْ"
        }

    def generate_poem(self, theme: str, meter: str = "البسيط", num_verses: int = 4, style: str = "classical"):
        if meter not in self.meters:
            meter = "البسيط"
        
        style_instruction = "بأسلوب شعري حديث ومعاصر" if style == "modern" else "بأسلوب شعري كلاسيكي فصيح"
        
        prompt = f"""اكتب قصيدة عربية جميلة {style_instruction}

الموضوع: {theme}
البحر الشعري: {meter}
التفعيلة: {self.meters[meter]}
عدد الأبيات: {num_verses}

شروط مهمة:
- التزم بالوزن الشعري بدقة تامة
- استخدم قافية موحدة
- اجعل المعنى واضحاً وجميلاً
- تجنب التعقيد اللغوي المفرط
- اكتب القصيدة مباشرة بدون مقدمات أو تعليقات

القصيدة:"""

        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 1000,
            "temperature": 0.8,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(
                self.base_url, 
                headers=self.headers, 
                json=payload, 
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                poem_text = result['content'][0]['text'].strip()
                return True, poem_text
            else:
                return False, f"خطأ في إنشاء القصيدة: {response.status_code}"

        except Exception as e:
            return False, f"خطأ: {str(e)}"

# App Title
st.title("🎭 مولد الشعر العربي")
st.markdown("---")

# Get API key from Streamlit secrets or environment variables
try:
    # Try Streamlit secrets first
    api_key = st.secrets["ANTHROPIC_API_KEY"]
    api_key_available = True
except (KeyError, FileNotFoundError):
    try:
        # Try environment variable
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            api_key_available = True
        else:
            api_key_available = False
            st.error("❌ لم يتم العثور على مفتاح API. يرجى إعداد ANTHROPIC_API_KEY في المتغيرات البيئية.")
    except:
        api_key = None
        api_key_available = False
        st.error("❌ خطأ في تحميل مفتاح API.")

# Main interface
if api_key_available:
    # User input
    user_prompt = st.text_area(
        "اكتب موضوع القصيدة:",
        placeholder="مثال: الحب، الطبيعة، الوطن، الصداقة...",
        height=100
    )
    
    # Options in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        meter = st.selectbox(
            "البحر الشعري:",
            ["البسيط", "الطويل", "الوافر", "الكامل", "الهزج", "الرجز", "المتقارب", "الرمل"]
        )
    
    with col2:
        style = st.selectbox(
            "الأسلوب:",
            ["classical", "modern"],
            format_func=lambda x: "كلاسيكي" if x == "classical" else "حديث"
        )
    
    with col3:
        num_verses = st.number_input(
            "عدد الأبيات:",
            min_value=2,
            max_value=10,
            value=4
        )
    
    # Generate button
    if st.button("🎨 أنشئ القصيدة", type="primary", use_container_width=True):
        if user_prompt.strip():
            with st.spinner("جاري إنشاء القصيدة..."):
                try:
                    poet = ArabicPoetryGenerator(api_key)
                    success, result = poet.generate_poem(
                        theme=user_prompt.strip(),
                        meter=meter,
                        num_verses=num_verses,
                        style=style
                    )
                    
                    if success:
                        st.markdown("### 📜 القصيدة:")
                        # Display poem in a beautiful container
                        st.markdown(
                            f"""
                            <div style="
                                background-color: #f8f9fa;
                                border-right: 4px solid #007bff;
                                padding: 20px;
                                margin: 10px 0;
                                border-radius: 5px;
                                font-family: 'Amiri', serif;
                                font-size: 18px;
                                line-height: 2;
                                text-align: right;
                                direction: rtl;
                            ">
                            {result.replace(chr(10), '<br>')}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                        # Download button
                        st.download_button(
                            label="📥 تحميل القصيدة",
                            data=result,
                            file_name=f"قصيدة_{user_prompt[:20]}.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error(f"❌ {result}")
                        
                except Exception as e:
                    st.error(f"❌ خطأ غير متوقع: {str(e)}")
        else:
            st.warning("⚠️ يرجى إدخال موضوع للقصيدة")

else:
    st.info("⚠️ التطبيق غير جاهز - يرجى إعداد مفتاح API")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>مولد الشعر العربي باستخدام الذكاء الاصطناعي</div>",
    unsafe_allow_html=True
)