import streamlit as st
from difflib import get_close_matches

# ✅ Set page config FIRST (only once)
st.set_page_config(page_title="AI Tool Suggestion Bot 🤖", layout="centered")

# ✅ Load external CSS
def load_css(file_path):
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ✅ Tool suggestion dictionary
tool_suggestions = {
    "ai meeting notes": ["Fathom", "Fireflies.ai", "Otter.ai"],
    "ai research assistant": ["Consensus", "Elicit", "Research Rabbit"],
    "chatbot creation": ["Botpress", "ManyChat", "Rasa", "Tidio AI"],
    "code generation": ["Codeium", "GitHub Copilot", "Replit Ghostwriter", "Tabnine"],
    "content writing": ["Anyword", "Copy.ai", "Jasper", "Scalenut"],
    "data analysis": ["ChatGPT Advanced Data Analysis", "MonkeyLearn", "Obviously AI"],
    "document summarization": ["Humata.ai", "Scholarcy", "SciSpace", "Scribbr"],
    "data visualization": ["Dash", "Plotly", "Streamlit Charts"],
    "email writing": ["Flowrite", "Lavender AI", "Rytr"],
    "image generation": ["Bing Image Creator", "DALL·E", "Leonardo.Ai", "Midjourney"],
    "note taking": ["Mem AI", "Notion AI", "Taskade"],
    "pdf reading": ["ChatPDF", "Humata", "UPDF"],
    "presentation creation": ["Beautiful.ai", "Gamma App", "SlidesAI", "Tome"],
    "resume making and checking": ["Enhancv", "Kickresume AI", "Resume.io", "Zety AI Resume Builder", "Wezbor"],
    "text generation": ["ChatGPT", "Claude", "Copy.ai", "Writesonic"],
    "translation": ["ChatGPT", "DeepL", "Google Translate AI"],
    "video generation": ["HeyGen", "Pika Labs", "Runway ML", "Synthesia"],
    "voice generation": ["ElevenLabs", "Murf AI", "Play.ht"]
    "website creation": ["LLama"]
}

# ✅ Page content
st.title("🤖 AI Tool Suggestion Chatbot")

st.markdown("""
Describe your task (e.g., *generate images*, *summarize documents*, *create presentation*, etc.)
and I'll recommend AI tools to help you!
""")

# ✅ Alphabetically sorted task list
all_tasks = sorted(tool_suggestions.keys())

# ✅ User input
st.markdown('<div class="select-label">🧠 Select or type what you want to do:</div>', unsafe_allow_html=True)
user_input = st.selectbox("", options=[""] + all_tasks, index=0)


# ✅ Tool match and output
if user_input:
    matched_task = user_input.lower()
    if matched_task in tool_suggestions:
        tools = tool_suggestions[matched_task]
        st.markdown(f"""
    <div class="custom-success">
        ✨ For <strong>{matched_task}</strong>, try these AI tools:<br>
        {"<br>- ".join([""] + tools)}
    </div>
    """, unsafe_allow_html=True)

    else:
        closest = get_close_matches(matched_task, all_tasks, n=1, cutoff=0.6)
        if closest:
            tools = tool_suggestions[closest[0]]
            st.info(f"🔍 Did you mean **{closest[0]}**?\n\nHere are some tools you can use:\n\n- " + "\n- ".join(tools))
        else:
            st.warning("😕 I couldn't find a match. Try rephrasing or use a more common AI task like 'image generation' or 'email writing'.")
