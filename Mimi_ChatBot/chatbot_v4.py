import os
import json
import io
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Dict, Optional
from uuid import uuid4
import base64

import pandas as pd
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.pagesizes import LETTER

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# =============================================================================
# 🎨 Mimi — Tutora Virtual (Optimized Edition)
# - Optimizaciones de CPU/RAM sin perder funcionalidades
#   * Cliente OpenAI cacheado (@st.cache_resource)
#   * Resumen incremental de historial + ventana de últimos N turnos
#   * Analítica opcional (toggle) y sentimiento incremental cacheado
#   * Evita renders duplicados y recomputos innecesarios
#   * Guardado/lectura cacheados (incluye agenda)
# =============================================================================

# ------------------------------- Config base -------------------------------- #
st.set_page_config(
    page_title="Mimi — Tutora Virtual",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Carga .env y rutas
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
CONV_DIR = Path("conversations")
ASSETS_DIR = Path("assets")
LOGO_PATH = ASSETS_DIR / "logo.png"

# Prompt de sistema (carácter y tono de Mimi)
PERSONAS = {
    "Mimi Zen": "Hablas con calma, propones respiraciones y pausas breves. Priorizas balance y bienestar.",
    "Mimi Productiva": "Eres directa, orientada a resultados, propones listas, deadlines y foco (técnica Pomodoro).",
    "Mimi Coach": "Haces preguntas poderosas, reflejas emociones y generas planes con métricas e hitos medibles.",
}

PROMPT_MIMI = (
    "Eres Mimi, una tutora virtual cercana, empática y profesional. "
    "Tu especialidad es el desarrollo personal, hábitos, productividad y organización. "
    "Tu tono es siempre positivo y alentador. NUNCA reveles que eres un modelo de IA. "
    "Si te preguntan quién eres, responde siempre identificándote como 'Mimi, tu tutora virtual'. "
    "Usa algunos emojis para hacer tus respuestas más cálidas y cercanas. 🌸✨"
)

QUICK_SUGGESTIONS = [
    "Dame un plan para ser más productivo",
    "¿Cómo organizo mi estudio semanal?",
    "Necesito motivación para empezar un proyecto",
    "Consejos para dormir mejor",
    "Crea una rutina de mañana de 30 min",
    "Plan de estudio para exámenes en 2 semanas",
]

DEFAULT_MODELS = [
    "gpt-4o-mini",
    "gpt-4o",
    "gpt-4.1-mini",
    "gpt-3.5-turbo",
]

TOPIC_KEYWORDS = {
    "productividad": ["productividad", "productivo", "pomodoro", "rutina", "organizar", "prioridades"],
    "motivación": ["motivación", "motivar", "ánimo", "constancia", "enfoque"],
    "sueño": ["sueño", "dormir", "insomnio", "descanso", "melatonina"],
}

DAILY_QUOTES = [
    "Pequeños pasos cada día suman grandes cambios. 🌱",
    "La constancia supera al talento cuando el talento no es constante. ✨",
    "Tu futuro lo construyes con lo que haces hoy, no mañana. ⚡",
]

# --------------------------- Utilidades y estilos --------------------------- #
CSS = """
<style>
/* ------------------ (Default) Light Theme Variables ------------------ */
:root {
  --bg: #f0f2f6;
  --card: #ffffff;
  --card-strong: #f0f2f6;
  --stroke: #e6e6e6;
  --accent: #50b070;
  --accent-2: #3e8e5a;
  --text: #31333F;
  --muted: #6e7078;
  --input-text: #000000;
}

/* ------------------- Dark Theme Override Variables ------------------- */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0b0f12;
    --card: rgba(255, 255, 255, 0.06);
    --card-strong: rgba(255,255,255,0.12);
    --stroke: rgba(255,255,255,0.08);
    --accent: #7bd389;
    --accent-2: #50b070;
    --text: #e8f2ec;
    --muted: #a9b8b0;
    --input-text: #e7efe9;
  }
}

/* ---------------------------- Base Styles ---------------------------- */
.stApp {
  background: var(--bg); /* Usa el fondo de la variable */
  color: var(--text);
}

/* --- Dark mode specific background --- */
@media (prefers-color-scheme: dark) {
  .stApp {
    background: radial-gradient(1200px 600px at 20% -10%, #18342a 0%, transparent 60%),
                radial-gradient(1000px 600px at 100% 0%, #1b1d3a 0%, transparent 60%),
                linear-gradient(180deg, #0a0f13 0%, #0b0f12 100%);
  }
}

.hero {
  border: 1px solid var(--stroke);
  background: linear-gradient(165deg, rgba(123,211,137,0.06) 0%, rgba(255,255,255,0.03) 100%);
  border-radius: 20px;
  padding: 20px 20px 14px 20px;
  margin-bottom: 14px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.05);
}
.hero h1 { margin: 0; font-weight: 700; letter-spacing: .3px; color: var(--text); }
.hero p  { margin: 6px 0 0 0; color: var(--muted); }

.chat-bubble {
  border: 1px solid var(--stroke);
  background: var(--card);
  border-radius: 16px;
  padding: 12px 14px;
  margin: 6px 0 10px 0;
  box-shadow: 0 8px 30px rgba(0,0,0,0.1);
}
.chat-bubble.user { background: var(--card-strong); }
.chat-meta { font-size: 0.8rem; color: var(--muted); margin-bottom: 6px; }

.kpi-card {
  border: 1px solid var(--stroke);
  background: var(--card);
  border-radius: 16px;
  padding: 16px;
  text-align: left;
  height: 100%;
}
.kpi-title { color: var(--muted); font-size: .85rem; margin: 0 0 4px; }
.kpi-value { font-size: 1.5rem; font-weight: 700; margin: 0; color: var(--text); }

.toolbar { display:flex; gap:10px; flex-wrap:wrap; margin: 6px 0 16px; }
.toolbar button {
  background: linear-gradient(180deg, var(--accent) 0%, var(--accent-2) 100%);
  color: #04160c; font-weight: 700; border:none; border-radius: 12px;
  padding: 8px 12px; cursor:pointer; box-shadow: 0 10px 24px rgba(50,170,110,.35);
}
.toolbar button.secondary {
  background: var(--card-strong); color: var(--text);
  border: 1px solid var(--stroke); box-shadow: none;
}

hr.soft { border: none; border-top: 1px solid var(--stroke); margin: 10px 0; }
textarea, input { color: var(--input-text) !important; }

/* ------------------- Estilos para el Reproductor de Audio Personalizado ------------------- */
.custom-audio-player {
  display: flex;
  align-items: center;
  gap: 12px;
  background-color: var(--card);
  border: 1px solid var(--stroke);
  border-radius: 999px; /* Completamente redondo */
  padding: 6px;
  margin-top: 10px;
  width: 100%;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.play-pause-btn {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: var(--accent);
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  flex-shrink: 0;
  color: #04160c;
  font-size: 16px;
}

.progress-bar-container {
  flex-grow: 1;
  height: 6px;
  background-color: var(--card-strong);
  border-radius: 3px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  width: 0%;
  background-color: var(--accent-2);
  border-radius: 3px;
  transition: width 0.1s linear;
}

.hidden {
    display: none;
}
</style>
"""

if not st.session_state.get("_css_loaded"):
    st.markdown(CSS, unsafe_allow_html=True)
    st.session_state._css_loaded = True


# --------------------------- Persistencia básica ---------------------------- #

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def format_human_ts(ts_iso: Optional[str]) -> str:
    try:
        dt = datetime.fromisoformat(ts_iso.replace("Z", "+00:00")) if ts_iso else datetime.now(timezone.utc)
        return dt.astimezone().strftime("%d %b %Y, %H:%M")
    except Exception:
        return "—"


def save_conversation(conv_id: str, messages: List[Dict], tasks_df: Optional[pd.DataFrame] = None):
    CONV_DIR.mkdir(exist_ok=True)
    conv_path = CONV_DIR / f"{conv_id}.json"
    conv_data = {
        "conv_id": conv_id,
        "timestamp_utc": utc_now_iso(),
        "messages": messages,
    }
    if tasks_df is None:
        tasks_df = st.session_state.get("tasks_df")

    if tasks_df is not None:
        try:
            df_to_save = tasks_df.copy()
            if 'fecha' in df_to_save.columns:
                df_to_save['fecha'] = df_to_save['fecha'].apply(
                    lambda x: x.isoformat() if pd.notna(x) else None
                )
            conv_data["tasks"] = df_to_save.to_dict(orient="records")
        except Exception as e:
            st.error(f"Error al preparar tareas para guardar: {e}")
            conv_data["tasks"] = []

    with conv_path.open("w", encoding="utf-8") as f:
        json.dump(conv_data, f, ensure_ascii=False, indent=2)


@st.cache_data(show_spinner=False)
def list_conversations() -> List[Dict]:
    if not CONV_DIR.exists():
        return []
    conv_files = sorted(CONV_DIR.glob("*.json"), reverse=True)
    items = []
    for f in conv_files:
        try:
            with f.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            user_msgs = [m.get("content", "") for m in data.get("messages", []) if m.get("role") == "user"]
            title = (user_msgs[0][:40] + "...") if user_msgs else "Conversación"
            ts = data.get("timestamp_utc")
            items.append(
                {"id": f.stem, "title": title, "date": format_human_ts(ts), "size": len(data.get("messages", []))})
        except Exception:
            continue
    return items


def load_conversation(conv_id: str) -> Optional[List[Dict]]:
    p = CONV_DIR / f"{conv_id}.json"
    if not p.exists():
        return None
    try:
        with p.open("r", encoding="utf-8") as fh:
            data = json.load(fh)

        tasks = data.get("tasks")
        if tasks is not None and tasks:
            try:
                df = pd.DataFrame(tasks)
                if 'fecha' in df.columns:
                    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce').dt.date
                st.session_state.tasks_df = df
                if 'id' in df.columns and not df['id'].empty:
                    st.session_state.next_task_id = df['id'].max() + 1
                else:
                    st.session_state.next_task_id = 1
            except Exception:
                pass
        else:
            st.session_state.next_task_id = 1

        return data.get("messages", [])
    except Exception:
        st.error("😕 El archivo de la conversación está dañado.")
        return None


# ---------------------------- Cliente OpenAI ------------------------------- #

@st.cache_resource(show_spinner=False)
def get_client() -> Optional[OpenAI]:
    if not API_KEY:
        st.error("❌ No se encontró la API Key de OpenAI. Agrega `OPENAI_API_KEY` a tu .env.")
        return None
    try:
        return OpenAI(api_key=API_KEY)
    except Exception as e:
        st.error(f"No se pudo inicializar el cliente: {e}")
        return None


def generate_response(client: OpenAI, model: str, messages: List[Dict]) -> Optional[str]:
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.6,
            max_tokens=700,
        )
        return (resp.choices[0].message.content or "").strip()
    except Exception:
        try:
            resp = client.responses.create(
                model=model,
                input=[{"role": m["role"], "content": m["content"]} for m in messages],
                temperature=0.6,
                max_output_tokens=700,
            )
            txt = getattr(resp, "output_text", None)
            if not txt and hasattr(resp, "output"):
                txt = str(resp.output)
            return (txt or "").strip()
        except Exception as e:
            st.error(f"Error al generar respuesta: {e}")
            return None


def generate_audio(client: OpenAI, text: str) -> Optional[bytes]:
    try:
        r = client.audio.speech.create(model="tts-1", voice="nova", input=text)
        return r.read()
    except Exception as e:
        st.warning(f"No se pudo generar el audio: {e}")
        return None


# ---------------------------- Estado de sesión ----------------------------- #

def init_state():
    if "client" not in st.session_state:
        st.session_state.client = get_client()
    if "persona" not in st.session_state:
        st.session_state.persona = "Mimi Productiva"
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": build_system_prompt(), "ts": utc_now_iso()}]
    if "conv_id" not in st.session_state:
        st.session_state.conv_id = f"conv_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"
    if "tts_enabled" not in st.session_state:
        st.session_state.tts_enabled = False
    if "model" not in st.session_state:
        st.session_state.model = DEFAULT_MODELS[0]
    if "tasks_df" not in st.session_state:
        st.session_state.tasks_df = pd.DataFrame([
            {"id": 0, "tarea": "Agrega aqui tus eventos", "fecha": datetime.now().date(), "estado": "Pendiente",
             "nota": ""}
        ])
    if "next_task_id" not in st.session_state:
        if not st.session_state.tasks_df.empty and 'id' in st.session_state.tasks_df.columns:
            st.session_state.next_task_id = st.session_state.tasks_df['id'].max() + 1
        else:
            st.session_state.next_task_id = 1

    if "history_summary" not in st.session_state:
        st.session_state.history_summary = ""
    if "max_context_turns" not in st.session_state:
        st.session_state.max_context_turns = 14
    if "sentiment_cache" not in st.session_state:
        st.session_state.sentiment_cache = {}
    if "analytics_enabled" not in st.session_state:
        st.session_state.analytics_enabled = False


def start_new_chat():
    st.session_state.messages = [{"role": "system", "content": build_system_prompt(), "ts": utc_now_iso()}]
    st.session_state.conv_id = f"conv_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}"
    st.cache_data.clear()
    st.rerun()


# ------------------------------ Componentes UI ----------------------------- #

def sidebar():
    with st.sidebar:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), caption="🌿 Mimi — Tu tutora", use_container_width=True)
        else:
            st.markdown("### 🌿 Mimi — Tu tutora")
            st.caption("Agrega un logo en `assets/logo.png` para personalizar.")

        st.markdown("---")
        st.subheader("⚙️ Ajustes")
        new_persona = st.selectbox(
            "Personalidad",
            list(PERSONAS.keys()),
            index=list(PERSONAS.keys()).index(st.session_state.persona),
        )
        if new_persona != st.session_state.persona:
            st.session_state.persona = new_persona
            if st.session_state.messages and st.session_state.messages[0].get("role") == "system":
                st.session_state.messages[0]["content"] = build_system_prompt()
                st.session_state.messages[0]["ts"] = utc_now_iso()
            else:
                st.session_state.messages.insert(0, {"role": "system", "content": build_system_prompt(),
                                                     "ts": utc_now_iso()})

        st.session_state.model = st.selectbox("Modelo", DEFAULT_MODELS, index=0)
        st.session_state.tts_enabled = st.toggle("🔊 Activar audio (TTS)", value=st.session_state.tts_enabled)

        st.markdown("---")
        st.subheader("🕓 Historial")
        if st.button("➕ Nueva conversación", use_container_width=True):
            start_new_chat()

        convs = list_conversations()
        if convs:
            q = st.text_input("Buscar en historial", placeholder="Filtra por título…")
            filtered = [c for c in convs if (q.lower() in c["title"].lower())] if q else convs
            labels = [f"{c['title']} — {c['date']} ({c['size']} msgs)" for c in filtered]
            ids = [c["id"] for c in filtered]
            selected = st.selectbox(
                "Cargar conversación:",
                options=[None] + ids,
                format_func=lambda x: "—" if x is None else labels[ids.index(x)] if x in ids else str(x),
            )
            if selected and selected != st.session_state.conv_id:
                loaded = load_conversation(selected)
                if loaded:
                    st.session_state.messages = loaded
                    st.session_state.conv_id = selected
                    st.toast("✅ Conversación cargada.", icon="📂")
                    st.rerun()

        st.markdown("---")
        streak = calc_streak_days(st.session_state.messages)
        completion = calc_completion_percent(st.session_state.tasks_df)
        quote = DAILY_QUOTES[hash(st.session_state.conv_id) % len(DAILY_QUOTES)]
        st.metric("Días activos", f"{streak} 🗓️")
        st.metric("Metas cumplidas", f"{completion}%")
        st.caption(f"💡 {quote}")

        st.markdown("---")
        conv_path = CONV_DIR / f"{st.session_state.conv_id}.json"
        if conv_path.exists():
            with open(conv_path, "rb") as f:
                st.download_button(
                    "📤 Exportar JSON",
                    data=f,
                    file_name=f"{st.session_state.conv_id}.json",
                    mime="application/json",
                    use_container_width=True,
                )

        md = conversation_to_markdown(st.session_state.messages)
        st.download_button(
            "📝 Exportar Markdown",
            data=md.encode("utf-8"),
            file_name=f"{st.session_state.conv_id}.md",
            mime="text/markdown",
            use_container_width=True,
        )

        st.markdown("---")
        st.caption(
            "Consejo: puedes anclar esta app en tu dock o abrir en modo pantalla completa para sesiones de estudio.")


def hero_and_toolbar():
    st.markdown(
        """
        <div class="hero">
          <h1>🌿 Mimi — Tu tutora virtual</h1>
          <p>Planifica, organiza y mejora tus hábitos con una guía cálida y profesional. ¡Empecemos! ✨</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        kpi_card("Mensajes en esta sesión", str(max(0, len(st.session_state.messages) - 1)))
    with c2:
        user_count = sum(1 for m in st.session_state.messages if m["role"] == "user")
        kpi_card("Mensajes del usuario", str(user_count))
    with c3:
        kpi_card("Personalidad", st.session_state.persona)

    st.markdown('<div class="toolbar">', unsafe_allow_html=True)
    colA, colB, colC, colD = st.columns([1, 1, 1, 1])
    with colA:
        if st.button("🧹 Limpiar chat", use_container_width=True):
            start_new_chat()
    with colB:
        if st.button("💾 Guardar ahora", use_container_width=True):
            save_conversation(st.session_state.conv_id, st.session_state.messages, st.session_state.tasks_df)
            st.toast("💾 Guardado.")
    with colC:
        if st.button("📎 Copiar último", use_container_width=True):
            last = next((m for m in st.session_state.messages[::-1] if m["role"] == "assistant"), None)
            if last:
                st.code(last["content"], language=None)
                st.toast("📋 Copiado a la vista (selecciona y Ctrl+C)")
    with colD:
        st.caption("Modelo: ")
        st.write(f"`{st.session_state.model}`")
    st.markdown('</div>', unsafe_allow_html=True)


def kpi_card(title: str, value: str):
    st.markdown(
        f"""
        <div class='kpi-card'>
          <p class='kpi-title'>{title}</p>
          <p class='kpi-value'>{value}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def suggestion_chips() -> Optional[str]:
    st.write("")
    st.markdown("**O empieza con una de estas ideas:**")
    cols = st.columns(3)
    chosen = None
    for i, s in enumerate(QUICK_SUGGESTIONS):
        with cols[i % 3]:
            if st.button(f"{s}", key=f"chip_{i}", use_container_width=True):
                chosen = s
    return chosen


def render_chat():
    for message in st.session_state.messages:
        if message["role"] == "system":
            continue
        avatar = "🌿" if message["role"] == "assistant" else "👤"
        css_class = "chat-bubble" + (" user" if message["role"] == "user" else "")
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(f"<div class='{css_class}'>", unsafe_allow_html=True)
            ts = message.get("ts") or utc_now_iso()
            st.markdown(
                f"<div class='chat-meta'>{'Mimi' if message['role'] == 'assistant' else 'Tú'} • {format_human_ts(ts)}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(message["content"])
            st.markdown("</div>", unsafe_allow_html=True)


def conversation_to_markdown(messages: List[Dict]) -> str:
    lines = ["# Transcripción — Mimi", ""]
    for m in messages:
        if m["role"] == "system":
            continue
        who = "**Mimi**" if m["role"] == "assistant" else "**Tú**"
        stamp = format_human_ts(m.get("ts"))
        lines.append(f"{who} _( {stamp} )_:\n\n{m['content']}\n")
    return "\n".join(lines)


def custom_audio_player(audio_bytes: bytes):
    """Genera un reproductor de audio HTML/CSS/JS personalizado y minimalista."""
    b64 = base64.b64encode(audio_bytes).decode()
    player_id = f"player-{uuid4()}"

    html = f"""
    <div class="custom-audio-player" id="{player_id}">
        <audio class="audio-element">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <div class="play-pause-btn">
            <span class="play-icon"> ▶️ </span>
            <span class="pause-icon hidden"> ⏸️ </span>
        </div>
        <div class="progress-bar-container">
            <div class="progress-bar"></div>
        </div>
    </div>

    <script>
        const player = document.getElementById('{player_id}');
        const audio = player.querySelector('.audio-element');
        const playPauseBtn = player.querySelector('.play-pause-btn');
        const playIcon = player.querySelector('.play-icon');
        const pauseIcon = player.querySelector('.pause-icon');
        const progressBar = player.querySelector('.progress-bar');

        playPauseBtn.addEventListener('click', () => {{
            if (audio.paused) {{
                document.querySelectorAll('audio').forEach(el => {{
                    el.pause();
                    const otherPlayer = el.closest('.custom-audio-player');
                    if (otherPlayer && otherPlayer.id !== '{player_id}') {{
                         otherPlayer.querySelector('.play-icon').classList.remove('hidden');
                         otherPlayer.querySelector('.pause-icon').classList.add('hidden');
                    }}
                }});
                audio.play();
                playIcon.classList.add('hidden');
                pauseIcon.classList.remove('hidden');
            }} else {{
                audio.pause();
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
            }}
        }});

        audio.addEventListener('ended', () => {{
            playIcon.classList.remove('hidden');
            pauseIcon.classList.add('hidden');
            progressBar.style.width = '0%';
        }});

        audio.addEventListener('pause', () => {{
             if (audio.currentTime > 0 && audio.currentTime < audio.duration) {{
                // Paused by user, not ended
             }} else {{
                playIcon.classList.remove('hidden');
                pauseIcon.classList.add('hidden');
             }}
        }});

        audio.addEventListener('timeupdate', () => {{
            const percent = (audio.currentTime / audio.duration) * 100;
            progressBar.style.width = `${{percent}}%`;
        }});
    </script>
    """
    st.components.v1.html(html, height=50)


# --------------------------------- Main ------------------------------------ #

def main():
    init_state()
    sidebar()
    hero_and_toolbar()

    is_new_chat = len(st.session_state.messages) <= 1
    choice = suggestion_chips() if is_new_chat else None

    tab_chat, tab_agenda, tab_coach, tab_analytics = st.tabs(
        ["💬 Chat", "🗓️ Agenda", "🧑‍🏫 Coach semanal", "📊 Analítica"])

    with tab_chat:
        render_chat()

        if "last_audio" in st.session_state and st.session_state.last_audio:
            custom_audio_player(st.session_state.last_audio.getvalue())
            st.session_state.last_audio = None

        user_input = st.chat_input("Escribe tu mensaje…")
        prompt = choice or user_input

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt, "ts": utc_now_iso()})

            compact_msgs = prepare_messages_for_model(st.session_state.messages)
            with st.spinner("💭 Mimi está pensando…"):
                client = st.session_state.client
                if client is None: st.stop()
                answer = generate_response(client, st.session_state.model, compact_msgs)

            if answer:
                st.session_state.messages.append({"role": "assistant", "content": answer, "ts": utc_now_iso()})
                if st.session_state.tts_enabled:
                    audio = generate_audio(st.session_state.client, answer)
                    if audio:
                        st.session_state.last_audio = io.BytesIO(audio)
                else:
                    st.session_state.last_audio = None

            save_conversation(st.session_state.conv_id, st.session_state.messages, st.session_state.tasks_df)
            st.rerun()

    with tab_agenda:
        planner_ui()

    with tab_coach:
        coach_weekly_ui()

    with tab_analytics:
        analytics_ui()

    st.markdown("<hr class='soft' />", unsafe_allow_html=True)
    with st.expander("ℹ️ Ayuda & Consejos"):
        st.markdown(
            """
            - Usa las **chips** para empezar rápido una conversación.
            - Activa **TTS** en la barra lateral para escuchar las respuestas.
            - Exporta tu sesión a **JSON**, **Markdown**, **CSV/ICS** (Agenda) o **PDF** (Coach semanal).
            - Activa la **Analítica** solo cuando la necesites para ahorrar recursos.
            - Cambia la **Personalidad** de Mimi para adaptar el estilo de ayuda.
            """
        )


# ----------------------------- Helpers nuevos ------------------------------ #

def build_system_prompt() -> str:
    persona = st.session_state.get("persona", "Mimi Productiva")
    return PROMPT_MIMI + " " + f"Adopta el estilo seleccionado: {persona}. " + PERSONAS.get(persona, "")


def prepare_messages_for_model(messages: List[Dict]) -> List[Dict]:
    """Mantiene contexto manejable con resumen + últimos N turnos."""
    N = st.session_state.get("max_context_turns", 14)
    sys = [m for m in messages if m.get("role") == "system"][:1]
    rest = [m for m in messages if m.get("role") != "system"]

    if len(rest) > N:
        old = rest[:-N]
        recent = rest[-N:]
        if old:
            old_text = json.dumps(old, ensure_ascii=False)
            old_hash = abs(hash(old_text))
            if st.session_state.get("_last_summary_hash") != old_hash:
                client = st.session_state.client
                try:
                    summary_prompt = [
                        {"role": "system",
                         "content": "Resume objetivamente el diálogo para mantener contexto para un tutor personal. Sé breve (<= 250 palabras)."},
                        {"role": "user", "content": old_text},
                    ]
                    resp = client.chat.completions.create(
                        model=st.session_state.model,
                        messages=summary_prompt,
                        temperature=0.2,
                        max_tokens=300,
                    )
                    st.session_state.history_summary = (resp.choices[0].message.content or "").strip()
                    st.session_state._last_summary_hash = old_hash
                except Exception:
                    st.session_state.history_summary = st.session_state.history_summary or ""
    else:
        recent = rest

    compact: List[Dict] = []
    compact.extend(sys or [{"role": "system", "content": build_system_prompt()}])
    if st.session_state.history_summary:
        compact.append({"role": "system", "content": f"Resumen de contexto previo: {st.session_state.history_summary}"})
    compact.extend(recent)
    return compact


def calc_streak_days(messages: List[Dict]) -> int:
    dates = sorted({
        datetime.fromisoformat(m.get('ts', utc_now_iso()).replace('Z', '+00:00')).date()
        for m in messages if m.get('role') == 'user'
    })
    if not dates:
        return 0
    streak = 1
    for i in range(len(dates) - 1, 0, -1):
        if (dates[i] - dates[i - 1]).days == 1:
            streak += 1
        else:
            break
    return streak


def calc_completion_percent(df: pd.DataFrame) -> int:
    try:
        total = len(df)
        done = (df['estado'].astype(str).str.lower() == 'hecha').sum()
        return int(round((done / total) * 100)) if total else 0
    except Exception:
        return 0


# ------------------------------ Agenda / Planner --------------------------- #

def planner_ui():
    st.subheader("🗓️ Agenda / planificador")
    st.caption("Edita tus tareas. Los cambios se aplican al hacer clic en '✅ Aplicar cambios'.")

    if 'id' not in st.session_state.tasks_df.columns:
        st.session_state.tasks_df.insert(0, 'id', range(st.session_state.next_task_id,
                                                        st.session_state.next_task_id + len(st.session_state.tasks_df)))
        st.session_state.next_task_id += len(st.session_state.tasks_df)

    cols = ['id'] + [col for col in st.session_state.tasks_df.columns if col != 'id']
    base_df = st.session_state.tasks_df[cols]

    with st.form("agenda_form", clear_on_submit=False):
        edited = st.data_editor(
            base_df,
            num_rows="dynamic",
            use_container_width=True,
            column_config={
                "id": st.column_config.NumberColumn("ID", disabled=True),
                "tarea": st.column_config.TextColumn("Tarea", required=True),
                "fecha": st.column_config.DateColumn("Fecha", format="YYYY-MM-DD", step=1),
                "estado": st.column_config.SelectboxColumn("Estado", options=["Pendiente", "Hecha"],
                                                           default="Pendiente"),
                "nota": st.column_config.TextColumn("Nota"),
            },
            key="tasks_editor",
        )
        submitted = st.form_submit_button("✅ Aplicar cambios", use_container_width=True)

    if submitted:
        new_rows_mask = pd.isna(edited['id'])
        num_new_rows = new_rows_mask.sum()
        if num_new_rows > 0:
            new_ids = range(st.session_state.next_task_id, st.session_state.next_task_id + num_new_rows)
            edited.loc[new_rows_mask, 'id'] = list(new_ids)
            st.session_state.next_task_id += num_new_rows

        edited['id'] = edited['id'].astype(int)
        edited['fecha'] = pd.to_datetime(edited['fecha'], errors='coerce').dt.date
        edited['estado'] = edited['estado'].fillna('Pendiente').astype(str)

        final_cols = ['id', 'tarea', 'fecha', 'estado', 'nota']
        st.session_state.tasks_df = edited[final_cols]
        st.toast("Cambios aplicados a la agenda ✅")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Guardar Agenda en historial", use_container_width=True):
            save_conversation(st.session_state.conv_id, st.session_state.messages, st.session_state.tasks_df)
            st.toast("Agenda guardada en el archivo de la conversación.")
    with col2:
        csv_bytes = st.session_state.tasks_df.drop(columns=['id'], errors='ignore').to_csv(index=False).encode("utf-8")
        st.download_button("Exportar CSV", data=csv_bytes, file_name="agenda.csv", mime="text/csv",
                           use_container_width=True)
    with col3:
        ics_text = df_to_ics(st.session_state.tasks_df)
        st.download_button("Exportar ICS", data=ics_text.encode("utf-8"), file_name="agenda.ics",
                           mime="text/calendar", use_container_width=True)

    st.markdown("---")
    st.subheader("📅 Tareas del Mes")
    try:
        task_with_dates = st.session_state.tasks_df.copy()
        task_with_dates['fecha'] = pd.to_datetime(task_with_dates['fecha'], errors='coerce')
        task_with_dates.dropna(subset=['fecha'], inplace=True)

        if not task_with_dates.empty:
            today = datetime.now()
            start_date = today - pd.DateOffset(months=1)
            end_date = today + pd.DateOffset(years=1)
            month_range = pd.date_range(start_date, end_date, freq='MS').to_pydatetime().tolist()

            meses_es = {
                1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
            }

            selected_month_date = st.selectbox(
                "Selecciona un mes para visualizar:",
                options=month_range,
                format_func=lambda date: f"{meses_es[date.month]} {date.year}",
                index=month_range.index(today.replace(day=1)) if today.replace(day=1) in month_range else 0
            )

            month_tasks = task_with_dates[
                (task_with_dates['fecha'].dt.year == selected_month_date.year) &
                (task_with_dates['fecha'].dt.month == selected_month_date.month)
                ]
            if not month_tasks.empty:
                st.dataframe(
                    month_tasks[['fecha', 'tarea', 'estado']].rename(columns={'fecha': 'Día'}),
                    use_container_width=True,
                    hide_index=True
                )
            else:
                st.info("No hay tareas programadas para este mes.")
        else:
            st.info("Añade tareas con fecha para ver el calendario.")

    except Exception as e:
        st.warning(f"No se pudo generar la vista de calendario: {e}")


def df_to_ics(df: pd.DataFrame) -> str:
    def ics_event(row: pd.Series) -> str:
        date_val = row.get("fecha", "")
        date_str = ""
        if pd.notna(date_val):
            try:
                date_str = pd.to_datetime(date_val).strftime("%Y-%m-%d")
            except Exception:
                date_str = str(date_val)
        dt = (date_str.replace("-", "") + "T090000Z") if date_str else datetime.utcnow().strftime("%Y%m%dT090000Z")
        summary = (row.get("tarea") or "Tarea").replace("\n", " ")
        desc = (row.get("nota") or "").replace("\n", " ")
        uid = f"{row.get('id', abs(hash(summary + dt)))}@mimi"  # Usar ID de tarea si existe
        return (
            "BEGIN:VEVENT\n"
            f"UID:{uid}\n"
            f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}\n"
            f"DTSTART:{dt}\n"
            f"SUMMARY:{summary}\n"
            f"DESCRIPTION:{desc}\n"
            "END:VEVENT\n"
        )

    events = "".join([ics_event(r) for _, r in df.iterrows()])
    ics = (
            "BEGIN:VCALENDAR\n"
            "VERSION:2.0\n"
            "PRODID:-//Mimi//Planner//ES\n"
            + events +
            "END:VCALENDAR\n"
    )
    return ics


# ------------------------------ Coach semanal ------------------------------ #

def coach_weekly_ui():
    st.subheader("🧑‍🏫 Coach semanal")
    st.caption("Genera un resumen de la semana: aprendizajes, consejos y próximos pasos. Guarda como PDF.")

    if st.button("Generar resumen", use_container_width=True):
        client = st.session_state.client
        if client is None:
            st.warning("Configura tu API Key primero.")
        else:
            with st.spinner("Creando resumen…"):
                summary = build_weekly_summary(client, st.session_state.model, st.session_state.messages)
            if summary:
                st.success("Resumen generado")
                st.markdown(summary)
                pdf_bytes = summary_to_pdf(summary)
                st.download_button("Descargar PDF", data=pdf_bytes, file_name="resumen_semanal.pdf",
                                   mime="application/pdf", use_container_width=True)


def build_weekly_summary(client: OpenAI, model: str, messages: List[Dict]) -> Optional[str]:
    recent = messages[-50:]
    prompt = [
        {"role": "system",
         "content": "Eres un coach que hace resúmenes semanales claros, con secciones: 'Lo aprendido', 'Consejos', 'Próximos pasos'. Usa tono cálido y accionable."},
        {"role": "user", "content": "Usa esta conversación para crear el resumen semanal."},
        {"role": "user", "content": json.dumps(recent, ensure_ascii=False)},
    ]
    try:
        resp = client.chat.completions.create(model=model, messages=prompt, temperature=0.5, max_tokens=700)
        return (resp.choices[0].message.content or "").strip()
    except Exception:
        try:
            resp = client.responses.create(model=model,
                                           input=[{"role": "user", "content": json.dumps(recent, ensure_ascii=False)}],
                                           max_output_tokens=700)
            return (getattr(resp, "output_text", "") or "").strip()
        except Exception as e:
            st.error(f"No se pudo generar el resumen: {e}")
            return None


def summary_to_pdf(text: str) -> bytes:
    buffer = io.BytesIO()
    c = pdf_canvas.Canvas(buffer, pagesize=LETTER)
    width, height = LETTER
    y = height - 72
    for line in text.splitlines():
        for chunk in [line[i:i + 96] for i in range(0, len(line), 96)]:
            c.drawString(54, y, chunk)
            y -= 16
            if y < 72:
                c.showPage()
                y = height - 72
    c.save()
    buffer.seek(0)
    return buffer.read()


# ------------------------------ Analítica ---------------------------------- #

def analytics_ui():
    st.subheader("📊 Analítica de progreso")
    st.caption("Temas más hablados, sentimiento y evolución.")

    st.session_state.analytics_enabled = st.toggle("Activar analítica en vivo",
                                                   value=st.session_state.analytics_enabled)
    if not st.session_state.analytics_enabled:
        st.info("Analítica desactivada para ahorrar CPU/RAM. Actívala cuando la necesites.")
        return

    col1, col2 = st.columns(2)
    with col1:
        topic_counts = count_topics(st.session_state.messages)
        st.write("### Temas mencionados")
        st.bar_chart(pd.DataFrame.from_dict(topic_counts, orient='index', columns=['menciones']))
    with col2:
        st.write("### Sentimiento (incremental)")
        sentiments = compute_sentiment_series(st.session_state.messages)
        if sentiments:
            df = pd.DataFrame({"t": list(range(len(sentiments))), "sent": sentiments})
            fig, ax = plt.subplots()
            ax.plot(df["t"], df["sent"])
            ax.set_xlabel("Turno de conversación")
            ax.set_ylabel("Sentimiento (-1 a 1)")
            ax.set_title("Evolución del sentimiento")
            st.pyplot(fig)
        else:
            st.info("Aún no hay suficiente conversación para estimar sentimiento.")


def count_topics(messages: List[Dict]) -> Dict[str, int]:
    counts = {k: 0 for k in TOPIC_KEYWORDS.keys()}
    for m in messages:
        if m.get("role") != "user":
            continue
        text = (m.get("content", "") or "").lower()
        for topic, words in TOPIC_KEYWORDS.items():
            if any(w in text for w in words):
                counts[topic] += 1
    return counts


def compute_sentiment_series(messages: List[Dict]) -> List[float]:
    """Calcula sentimiento solo para mensajes NUEVOS del usuario y cachea. Limita a últimos 50."""
    client = st.session_state.client
    if client is None:
        return []

    user_msgs = [m for m in messages if m.get("role") == "user"][-50:]
    series = []
    for idx, m in enumerate(user_msgs):
        key = m.get("ts") or (m.get("content")[:32] if m.get("content") else str(idx))
        if key in st.session_state.sentiment_cache:
            series.append(st.session_state.sentiment_cache[key])
            continue
        text = m.get("content", "") or ""
        val = heuristic_sentiment(text)
        try_model = (idx >= len(user_msgs) - 5)
        if try_model:
            try:
                prompt = [
                    {"role": "system",
                     "content": "Devuelve SOLO un número entre -1 (muy negativo) y 1 (muy positivo), con 0 como neutral."},
                    {"role": "user", "content": text},
                ]
                resp = client.chat.completions.create(model=st.session_state.model, messages=prompt, temperature=0,
                                                      max_tokens=5)
                raw = (resp.choices[0].message.content or "").strip().split()[0]
                val = float(raw)
            except Exception:
                pass
        val = max(-1.0, min(1.0, float(val)))
        st.session_state.sentiment_cache[key] = val
        series.append(val)
    return series


def heuristic_sentiment(text: str) -> float:
    text = (text or "").lower()
    pos = sum(text.count(w) for w in ["bien", "logré", "feliz", "avancé", "genial", "motivado"])
    neg = sum(text.count(w) for w in ["mal", "triste", "cansado", "estresado", "no pude", "fracaso"])
    if pos == neg == 0:
        return 0.0
    return (pos - neg) / max(1, (pos + neg))


# ------------------------------ Entry point -------------------------------- #
if __name__ == "__main__":
    main()