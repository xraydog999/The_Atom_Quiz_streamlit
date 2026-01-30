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
        "q": "In the above figure, identify the symbols A, Z, X, and n:
Mass number, atomic number, chemical symbol, charge.
Atomic number, mass number, chemical symbol, charge.
charge, Mass number, atomic number, chemical symbol
",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer A"
    },
    {
        "image": "2.png",
        "q": "Question 2 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer B"
    },
    {
        "image": "3.png",
        "q": "Question 3 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer C"
    },
    {
        "image": "4.png",
        "q": "Question 4 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer A"
    },
    {
        "image": "5.png",
        "q": "Question 5 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer B"
    },
    {
        "image": "6.png",
        "q": "Question 6 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer C"
    },
    {
        "image": "7.png",
        "q": "Question 7 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer A"
    },
    {
        "image": "8.png",
        "q": "Question 8 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer B"
    },
    {
        "image": "9.png",
        "q": "Question 9 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
        "answer": "Answer C"
    },
    {
        "image": "10.png",
        "q": "Question 10 text goes here.",
        "options": ["Answer A", "Answer B", "Answer C"],
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

