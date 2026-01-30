import streamlit as st
from PIL import Image

st.title("Image‑Based Multiple Choice Quiz")

# -----------------------------
# QUIZ DATA
# -----------------------------
questions = [
    {"image": "1.png", "q": "In the above figure, identify the symbols A, Z, X, and n", 
     "options": ["Mass number, atomic number, chemical symbol, charge.", 
                 "Atomic number, mass number, chemical symbol, charge.", 
                 "Charge, Mass number, atomic number, chemical symbol."], 
     "answer": "Mass number, atomic number, chemical symbol, charge."},

    {"image": "2.png", "q": "An atom contains: 35 protons, 36 electrons, and 45 neutrons. Using the figure above, what are the values of: A, Z, X and n?", 
     "options": ["80, 35, Br, 1-", "35, 80, Cl, 1+", "80, 35, Br, 0"], 
     "answer": "80, 35, Br, 1-"},

    {"image": "3.png", "q": "An atom contains: 8 protons, 8 neutrons, and 2 more electrons than protons. Using the figure above, what are the values of: A, Z, X and n?", 
     "options": ["8, 16, N, 1-", "16, 8, O, 0", "16, 8, O, 2-"], 
     "answer": "16, 8, O, 2-"},

    {"image": "4.png", "q": "An atom contains: 26 protons, 29 neutrons, and 23 electrons. Using the figure above, what are the values of: A, Z, X and n?", 
     "options": ["26, 55, Co, 0", "55, 26, Fe, 3", "55, 26, Fe, 3+"], 
     "answer": "55, 26, Fe, 3+"},

    {"image": "5.png", "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons.", 
     "options": ["9, 19, 0", "10, 9, 10", "19, 10, 11"], 
     "answer": "10, 9, 10"},

    {"image": "6.png", "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons.", 
     "options": ["20, 19, 18", "19, 20, 19", "19, 39, 20"], 
     "answer": "20, 19, 18"},

    {"image": "7.png", "q": "Using the figure above, identify the numbers of neutrons, protons, and electrons.", 
     "options": ["73, 19, 30", "31, 42, 42", "42, 31, 31"], 
     "answer": "42, 31, 31"},

    {"image": "8.png", "q": "Using the figure above, identify the numbers of neutrons, protons and electrons.", 
     "options": ["73, 42, 45", "42, 73, 42", "42, 31, 28"], 
     "answer": "42, 31, 28"},

    {"image": "9.png", "q": "Using the figure above, identify the numbers of neutrons, proton and electrons.", 
     "options": ["51, 74, 71", "28, 23, 20", "23, 28, 28"], 
     "answer": "28, 23, 20"},

    {"image": "10.png", "q": "Using the figure above, identify the numbers of neutrons, proton and electrons.", 
     "options": ["52, 76, 78", "76, 52, 54", "76, 128, 2"], 
     "answer": "76, 52, 54"},
]

# -----------------------------
# QUIZ DISPLAY (NO SHUFFLING)
# -----------------------------
user_answers = []
all_answered = True

for i, q in enumerate(questions):

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

        for i, q in enumerate(questions):

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

