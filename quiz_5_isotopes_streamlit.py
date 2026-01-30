import streamlit as st
from PIL import Image
import random

st.title("Image‑Based Multiple Choice Quiz")

# -----------------------------
# QUIZ DATA
# -----------------------------
# Update the question text and correct answers as needed.
# IMPORTANT: Image paths now reference files in the SAME folder.

questions = [
    {
        "image": "1.png",
        "q": "In the above figure, identify the symbols A, Z, X, and n:",
        "options": ["Mass number, atomic number, chemical symbol, charge.", "Atomic number, mass number, chemical symbol, charge.", "charge, Mass number, atomic number, chemical symbol,"],
        "answer": "Answer A"
    },
    {
        "image": "2.png",
        "q": "An atom contains: 35 protons, 36 electrons, and 45 neutrons. Using the figure above, what are the values of: A, Z, X and n? ",
        "options": ["80, 35, Br, 1-", "35, 80, Cl, 1+", "80, 35, Br, 0"],
        "answer": "Answer B"
    },
    {
        "image": "3.png",
        "q": "An atom contains: 8 protons, 8 neutrons, and 2 more electrons than protons. Using the figure above, what are the values of: A, Z, X and n? ",
        "options": ["8, 16, N, 1-", "16, 8, O, 0", "16, 8, O, 2-"],
        "answer": "Answer C"
    },
    {
        "image": "4.png",
        "q": "An atom contains: 26 protons, 29 neutrons, and 23 electrons.  Using the figure above, what are the values of: A, Z, X and n?",
        "options": ["9, 19, 0", "10, 9, 10", "19, 10, 11"],
        "answer": "Answer A"
    },
    {
        "image": "5.png",
        "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons. ",
        "options": ["9,19,0", "10,9,10", "19,10,11"],
        "answer": "Answer B"
    },
    {
        "image": "6.png",
        "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons",
        "options": ["20, 19, 18", "19, 20, 19", "19, 39, 20"],
        "answer": "Answer C"
    },
    {
        "image": "7.png",
        "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons. ","options": ["73, 19, 30", "31, 42, 42", "42, 31, 31"],
        "answer": "Answer A"
    },
    {
        "image": "8.png",
        "q": "Using the figure above, identify the numbers of neutrons, protons and electrons. ","options": ["73, 42, 45", "42, 73, 42", "42, 31, 28"],
        "answer": "Answer B"
    },
    {
        "image": "9.png",
        "q": "Using the figure above, identify the numbers of neutrons, proton and electrons. ", "options": ["51, 74, 71", "28, 23, 20", "23, 28, 28"],"answer": "Answer C"
    },
    {
        "image": "10.png",
        "q": "Using the figure above, identify the numbers of neutrons, proton and electrons. ","options": ["52, 76, 78", "76, 52, 56", "76, 128, 2"],
        "answer": "Answer A"
    }
]

# -----------------------------
# RANDOMIZE QUESTION ORDER
# -----------------------------
if "shuffled" not in st.session_state:
    st.session_state.shuffled = random.sample(questions, len(questions))

# -----------------------------
# QUIZ DISPLAY
# -----------------------------
user_answers = []
all_answered = True

for i, q in enumerate(st.session_state.shuffled):
    st.subheader(f"Question {i+1}")

    # Display image
    try:
        img = Image.open(q["image"])
        st.image(img, use_column_width=True)
    except FileNotFoundError:
        st.error(f"Image not found: {q['image']}")

    # Blank option at top
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
# SUBMIT BUTTON
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
            st.write("---")

        st.write(f"## Final Score: {score} out of {len(questions)}")

        if st.button("Try Again"):
            st.session_state.clear()
            st.experimental_rerun()
