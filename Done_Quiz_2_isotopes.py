import streamlit as st
from PIL import Image
import random

st.title("Image‑Based Multiple Choice Quiz")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    {"image": "1.png", "q": "Question 1 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer A"},
    {"image": "2.png", "q": "Question 2 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer B"},
    {"image": "3.png", "q": "Question 3 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer C"},
    {"image": "4.png", "q": "Question 4 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer A"},
    {"image": "5.png", "q": "Question 5 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer B"},
    {"image": "6.png", "q": "Question 6 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer C"},
    {"image": "7.png", "q": "Question 7 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer A"},
    {"image": "8.png", "q": "Question 8 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer B"},
    {"image": "9.png", "q": "Question 9 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer C"},
    {"image": "10.png", "q": "Question 10 text goes here.", "options": ["Answer A", "Answer B", "Answer C"], "answer": "Answer A"},
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

    st.markdown(f"<h2 style='font-size: 32px;'>Question {i+1}</h2>", unsafe_allow_html=True)

    # Load and resize image to 50%
    img = Image.open(q["image"])
    w, h = img.size
    img = img.resize((w // 2, h // 2))
    st.image(img)

    # Larger question text
    st.markdown(
        f"<p style='font-size: 28px; font-weight: bold;'>{q['q']}</p>",
        unsafe_allow_html=True
    )

    # Blank option at top
    options = [" "] + q["options"]

    # Larger radio button labels
    choice = st.radio(
        "",
        options,
        index=0,
        key=f"q{i}",
        format_func=lambda x: f"   {x}" if x == " " else f"🔹 {x}"
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

            st.markdown(f"<h3 style='font-size: 28px;'>Question {i+1}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 24px;'><b>Your answer:</b> {user_answers[i]}</p>", unsafe_allow_html=True)

            if user_answers[i] == q["answer"]:
                st.markdown(
                    "<span style='color:green; font-size:24px; font-weight:bold;'>Correct ✔</span>",
                    unsafe_allow_html=True
                )
                score += 1
            else:
                st.markdown(
                    "<span style='color:red; font-size:24px; font-weight:bold;'>Incorrect ✘</span>",
                    unsafe_allow_html=True
                )

            st.markdown(f"<p style='font-size: 22px;'><b>Correct answer:</b> {q['answer']}</p>", unsafe_allow_html=True)
            st.write("---")

        st.markdown(f"<h2 style='font-size: 32px;'>Final Score: {score} / {len(questions)}</h2>", unsafe_allow_html=True)

        if st.button("Try Again"):
            st.session_state.clear()
            st.experimental_rerun()
