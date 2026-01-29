import streamlit as st
import random

st.title("Isotopes and Atomic Structure Quiz")
st.write("A multiple‑choice quiz for first‑year college students learning about isotopes and atomic structure.")

# -----------------------------
# Quiz Questions + Explanations
# -----------------------------
questions = [
    {
        "q": "What is the definition of an isotope?",
        "options": [
            "Atoms with different numbers of electrons",
            "Atoms with the same number of protons but different numbers of neutrons",
            "Atoms with different numbers of protons",
            "Atoms with the same mass number"
        ],
        "answer": "Atoms with the same number of protons but different numbers of neutrons",
        "explanation": "Isotopes always have the same number of protons but differ in neutrons."
    },
    {
        "q": "What determines the identity of an atom?",
        "options": ["Number of neutrons", "Number of electrons", "Number of protons", "Mass number"],
        "answer": "Number of protons",
        "explanation": "The atomic number (protons) defines the element."
    },
    {
        "q": "What is the atomic number?",
        "options": [
            "Number of neutrons",
            "Number of protons",
            "Number of electrons",
            "Sum of protons and neutrons"
        ],
        "answer": "Number of protons",
        "explanation": "Atomic number = number of protons."
    },
    {
        "q": "What is the mass number?",
        "options": [
            "Number of protons",
            "Number of neutrons",
            "Sum of protons and neutrons",
            "Sum of protons and electrons"
        ],
        "answer": "Sum of protons and neutrons",
        "explanation": "Mass number counts only protons + neutrons."
    },
    {
        "q": "Why are atomic weights (on the periodic table) not whole numbers?",
        "options": [
            "Because electrons have mass",
            "Because protons and neutrons change mass",
            "Because they are averages of isotopes",
            "Because atoms lose mass over time"
        ],
        "answer": "Because they are averages of isotopes",
        "explanation": "Atomic weights reflect the weighted average of all natural isotopes."
    },
    {
        "q": "Protium has how many neutrons?",
        "options": ["0", "1", "2", "3"],
        "answer": "0",
        "explanation": "Protium is hydrogen‑1: 1 proton, 0 neutrons."
    },
    {
        "q": "Deuterium has how many neutrons?",
        "options": ["0", "1", "2", "3"],
        "answer": "1",
        "explanation": "Deuterium is hydrogen‑2: 1 proton, 1 neutron."
    },
    {
        "q": "Tritium has how many neutrons?",
        "options": ["0", "1", "2", "3"],
        "answer": "2",
        "explanation": "Tritium is hydrogen‑3: 1 proton, 2 neutrons."
    },
    {
        "q": "Which hydrogen isotope is radioactive?",
        "options": ["Protium", "Deuterium", "Tritium", "All of them"],
        "answer": "Tritium",
        "explanation": "Tritium is radioactive; the others are stable."
    },
    {
        "q": "Which hydrogen isotope has the greatest mass?",
        "options": ["Protium", "Deuterium", "Tritium", "They all have the same mass"],
        "answer": "Tritium",
        "explanation": "Tritium has 1 proton + 2 neutrons, making it the heaviest."
    },
    {
        "q": "If an atom has atomic number 8, how many protons does it have?",
        "options": ["6", "7", "8", "16"],
        "answer": "8",
        "explanation": "Atomic number = number of protons."
    },
    {
        "q": "If an atom has atomic number 8, how many electrons does a neutral atom have?",
        "options": ["6", "7", "8", "16"],
        "answer": "8",
        "explanation": "Neutral atoms have equal protons and electrons."
    },
    {
        "q": "If an atom has mass number 16 and atomic number 8, how many neutrons does it have?",
        "options": ["6", "8", "16", "24"],
        "answer": "8",
        "explanation": "Neutrons = mass number − atomic number = 16 − 8."
    },
    {
        "q": "A positive ion (cation) has:",
        "options": [
            "More electrons than protons",
            "More protons than electrons",
            "Equal numbers of protons and electrons",
            "More neutrons than protons"
        ],
        "answer": "More protons than electrons",
        "explanation": "Losing electrons creates a positive charge."
    },
    {
        "q": "A negative ion (anion) has:",
        "options": [
            "More electrons than protons",
            "More protons than electrons",
            "Equal numbers of protons and electrons",
            "More neutrons than electrons"
        ],
        "answer": "More electrons than protons",
        "explanation": "Gaining electrons creates a negative charge."
    },
    {
        "q": "If an atom has 11 protons and 10 electrons, what is its charge?",
        "options": ["+1", "-1", "0", "+2"],
        "answer": "+1",
        "explanation": "One fewer electron gives a +1 charge."
    },
    {
        "q": "If an atom has 17 protons and 18 electrons, what is its charge?",
        "options": ["+1", "-1", "0", "-2"],
        "answer": "-1",
        "explanation": "One extra electron gives a -1 charge."
    },
    {
        "q": "Two atoms are isotopes if they have:",
        "options": [
            "Different numbers of protons",
            "Different numbers of electrons",
            "Different numbers of neutrons",
            "Different charges"
        ],
        "answer": "Different numbers of neutrons",
        "explanation": "Isotopes differ only in neutrons."
    },
    {
        "q": "Which of the following is true about isotopes?",
        "options": [
            "They have identical chemical behavior",
            "They have different atomic numbers",
            "They have different numbers of protons",
            "They are different elements"
        ],
        "answer": "They have identical chemical behavior",
        "explanation": "Chemical behavior depends on electrons, not neutrons."
    },
    {
        "q": "If carbon‑12 has 6 neutrons, how many neutrons does carbon‑14 have?",
        "options": ["6", "7", "8", "14"],
        "answer": "8",
        "explanation": "Carbon‑14 has mass number 14 → 14 − 6 = 8 neutrons."
    },
    {
        "q": "If chlorine‑35 has 18 neutrons, how many neutrons does chlorine‑37 have?",
        "options": ["17", "18", "19", "20"],
        "answer": "20",
        "explanation": "Chlorine‑37 has 2 more neutrons than chlorine‑35."
    },
    {
        "q": "Which statement about isotopes is correct?",
        "options": [
            "They have different numbers of protons",
            "They have different mass numbers",
            "They have different atomic numbers",
            "They have different numbers of electrons"
        ],
        "answer": "They have different mass numbers",
        "explanation": "Mass number changes when neutrons change."
    },
    {
        "q": "If an atom has 20 protons, what element is it?",
        "options": ["Calcium", "Potassium", "Neon", "Argon"],
        "answer": "Calcium",
        "explanation": "Calcium’s atomic number is 20."
    },
    {
        "q": "If an atom has 15 protons and 16 neutrons, what is its mass number?",
        "options": ["15", "16", "30", "31"],
        "answer": "31",
        "explanation": "Mass number = 15 + 16."
    },
    {
        "q": "If an atom has 12 protons and 10 electrons, it is:",
        "options": ["A neutral atom", "A +2 ion", "A -2 ion", "A +1 ion"],
        "answer": "A +2 ion",
        "explanation": "Losing 2 electrons gives a +2 charge."
    },
    {
        "q": "If an atom has 9 protons and 10 electrons, it is:",
        "options": ["A neutral atom", "A +1 ion", "A -1 ion", "A -2 ion"],
        "answer": "A -1 ion",
        "explanation": "Gaining 1 electron gives a -1 charge."
    },
    {
        "q": "Which isotope of hydrogen has one proton and one neutron?",
        "options": ["Protium", "Deuterium", "Tritium", "Hydronium"],
        "answer": "Deuterium",
        "explanation": "Deuterium = hydrogen‑2."
    },
    {
        "q": "Which isotope of hydrogen has one proton and two neutrons?",
        "options": ["Protium", "Deuterium", "Tritium", "Hydronium"],
        "answer": "Tritium",
        "explanation": "Tritium = hydrogen‑3."
    },
    {
        "q": "Which isotope of hydrogen has one proton and zero neutrons?",
        "options": ["Protium", "Deuterium", "Tritium", "Hydronium"],
        "answer": "Protium",
        "explanation": "Protium = hydrogen‑1."
    },
    {
        "q": "Isotopes of the same element always have the same:",
        "options": ["Mass number", "Number of neutrons", "Number of protons", "Number of electrons"],
        "answer": "Number of protons",
        "explanation": "Protons define the element."
    }
]

# -----------------------------
# Randomize question order
# -----------------------------
if "shuffled" not in st.session_state:
    st.session_state.shuffled = random.sample(questions, len(questions))

# -----------------------------
# Quiz Logic
# -----------------------------
st.header("Questions")

user_answers = []
all_answered = True

for i, q in enumerate(st.session_state.shuffled):
    st.subheader(f"Question {i+1}")

    options = [" "] + q["options"]

    choice = st.radio(
        q["q"],
        options,
        index=0,
        key=f"q{i}"
    )

    user_answers.append(choice)

    if choice == " ":
        all_answered = False

# -----------------------------
# Submit Button
# -----------------------------
if st.button("Submit Quiz"):
    if not all_answered:
        st.error("Please answer all questions before submitting.")
    else:
        score = 0
        st.success("Quiz Submitted!")

        for i, q in enumerate(st.session_state.shuffled):
            st.write(f"### Question {i+1}")
            st.write(f"**Your answer:** {user_answers[i]}")

            if user_answers[i] == q["answer"]:
                st.markdown(
                    "<span style='color:green; font-weight:bold;'>Correct ✔</span>",
                    unsafe_allow_html=True
                )
                score += 1
            else:
                st.markdown(
                    "<span style='color:red; font-weight:bold;'>Incorrect ✘</span>",
                    unsafe_allow_html=True
                )

            st.write(f"**Correct answer:** {q['answer']}")
            st.write(f"**Explanation:** {q['explanation']}")
            st.write("---")

        st.write(f"## Final Score: {score} out of {len(questions)}")

        if st.button("Try Again"):
            st.session_state.clear()
            st.experimental_rerun()


