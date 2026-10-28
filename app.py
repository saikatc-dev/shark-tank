"""Streamlit UI for Pitch to the AI Sharks.

Run:  streamlit run app.py
Needs GROQ_API_KEY in the environment / .env (free Groq key).
"""
from pathlib import Path

import streamlit as st

from panel import run_panel
from sharks import SHARKS

HERE = Path(__file__).parent
SAMPLE_PITCHES = [
    ("TiffinAI", (HERE / "sample_pitch.txt").read_text(encoding="utf-8")),
    *[
        (path.stem, path.read_text(encoding="utf-8"))
        for path in sorted((HERE / "sample_pitches").glob("*.txt"))
    ],
]

st.set_page_config(page_title="Pitch to the AI Sharks", page_icon="🦈", layout="centered")
st.title("🦈 Pitch to the AI Sharks")
st.caption("Pitch your startup to a panel of AI investors. They judge it, argue, and make offers.")

with st.sidebar:
    st.subheader("The panel")
    for s in SHARKS:
        st.markdown(f"**{s.name}** — {s.title}")

sample_index = st.selectbox(
    "Load a sample pitch",
    range(len(SAMPLE_PITCHES)),
    format_func=lambda index: SAMPLE_PITCHES[index][0],
)
pitch = st.text_area("Your pitch", value=SAMPLE_PITCHES[sample_index][1], height=240)

if st.button("Face the Sharks 🦈", type="primary"):
    with st.spinner("The panel is deliberating…"):
        result = run_panel(pitch)

    st.subheader("The verdicts")
    for v in result["final"]:
        invest = v.stance.upper().startswith("INVEST")
        with st.container(border=True):
            st.markdown(f"### {'💰' if invest else '🚫'} {v.shark} — {'INVEST' if invest else 'PASS'}")
            if v.offer:
                st.markdown(f"**Offer:** {v.offer}")
            st.write(v.reasoning)

    st.divider()
    st.markdown("### 🎤 The Host")
    st.info(result["summary"])
