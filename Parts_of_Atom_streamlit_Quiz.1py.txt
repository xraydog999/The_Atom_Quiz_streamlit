import streamlit as st

st.title("Atomic Structure Basics Quiz")
st.write("A friendly quiz for first‑year college students learning about atoms.")

# -----------------------------
# Quiz Questions
# -----------------------------
questions = [
    {
        "q": "Which particle has a positive charge?",
        "options": ["Electron", "Neutron", "Proton", "Nucleus"],
        "answer": "Proton"
    },
    {
        "q": "Which particle has a negative charge?",
        "options": ["Proton", "Electron", "Neutron", "Nucleus"],
        "answer": "Electron"
    },
    {
        "q": "Which particle has no charge?",
        "options": ["Proton", "Electron", "Neutron", "Nucleus"],
        "answer": "Neutron"
    },
    {
        "q": "Where are protons located?",
        "options": ["Outside the atom", "In the nucleus", "Orbiting the nucleus", "In empty space"],
        "answer": "In the nucleus"
    },
    {
        "q": "Where are neutrons located?",
        "options": ["Orbiting the nucleus", "In the nucleus", "Outside the atom", "In electron clouds"],
        "answer": "In the nucleus"
    },
    {
        "q": "Where are electrons located?",
        "options": ["In the nucleus", "In electron clouds around the nucleus", "Inside protons", "Inside neutrons"],
        "answer": "In electron clouds around the nucleus"
    },
    {
        "q": "Which particle takes part in chemical reactions?",
        "options": ["Protons", "Neutrons", "Electrons", "Nucleus"],
        "answer": "Electrons"
    },
    {
        "q": "Which particle determines the identity of an element?",
        "options": ["Elect