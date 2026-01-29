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
        "options": ["Electrons", "Neutrons", "Protons", "Nucleus"],
        "answer": "Protons"
    },
    {
        "q": "Which particle has the smallest mass?",
        "options": ["Proton", "Neutron", "Electron", "Nucleus"],
        "answer": "Electron"
    },
    {
        "q": "Which two particles have almost the same mass?",
        "options": ["Protons and electrons", "Electrons and neutrons", "Protons and neutrons", "Electrons and nucleus"],
        "answer": "Protons and neutrons"
    },
    {
        "q": "What is the charge of the nucleus?",
        "options": ["Positive", "Negative", "Neutral", "It changes constantly"],
        "answer": "Positive"
    },
    {
        "q": "Why is the nucleus positive?",
        "options": ["It contains electrons", "It contains protons", "It contains neutrons only", "It has no particles"],
        "answer": "It contains protons"
    },
    {
        "q": "How big is the nucleus compared to the whole atom?",
        "options": ["It takes up most of the atom", "It is tiny", "It is the same size as the atom", "It is larger than the atom"],
        "answer": "It is tiny"
    },
    {
        "q": "Because the nucleus is tiny, most of the atom is:",
        "options": ["Solid", "Liquid", "Empty space", "Filled with neutrons"],
        "answer": "Empty space"
    },
    {
        "q": "Which scientist discovered the basic structure of the atom using the gold foil experiment?",
        "options": ["Bohr", "Thomson", "Rutherford", "Einstein"],
        "answer": "Rutherford"
    },
    {
        "q": "What did Rutherford’s experiment show?",
        "options": [
            "Atoms are solid spheres",
            "Electrons are in fixed orbits",
            "Most of the atom is empty space",
            "Atoms have no nucleus"
        ],
        "answer": "Most of the atom is empty space"
    },
    {
        "q": "Which particle orbits outside the nucleus?",
        "options": ["Proton", "Neutron", "Electron", "Nucleus"],
        "answer": "Electron"
    },
    {
        "q": "Which part of the atom is extremely dense?",
        "options": ["Electron cloud", "Nucleus", "Empty space", "Outer shell"],
        "answer": "Nucleus"
    },
    {
        "q": "Which particle helps stabilize the nucleus?",
        "options": ["Electrons", "Neutrons", "Protons", "Photons"],
        "answer": "Neutrons"
    },
    {
        "q": "Which particle is responsible for electrical interactions?",
        "options": ["Protons", "Neutrons", "Electrons", "Nucleus"],
        "answer": "Electrons"
    }
]

# -----------------------------
# Quiz Logic
# -----------------------------
score = 0
user_answers = []

st.header("Questions")

for i, q in enumerate(questions):
    st.subheader(f"Question {i+1}")
    user_choice = st.radio(q["q"], q["options"], key=i)
    user_answers.append(user_choice)

if st.button("Submit Quiz"):
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"Your score: {score} out of {len(questions)}")

    st.write("### Correct Answers")
    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}:** {q['answer']}")
