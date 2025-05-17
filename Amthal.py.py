import streamlit as st
import random


st.title("لعبة اكمل المثل")


# مجموعة أمثال مصرية (الجزء الأول : التكملة)
proverbs = {
    "اللي اختشوا ماتوا": ".",
    "امشي عدل": "يعدلك",
    "اللي يعيش ياما يشوف": ".",
    "يا بخت اللي": "يعرف قدر نفسه",
    "الغايب عذره": "معاه",
    "ربنا معاك": ".",
    "كل تأخيرة": "وفيها خيرة",
    "الوقت كالسيف": "إن لم تقطعه قطعك"
}


if "current_proverb" not in st.session_state:
    st.session_state.current_proverb = random.choice(list(proverbs.keys()))


st.write(f"اكمل المثل: **{st.session_state.current_proverb}**")


user_answer = st.text_input("اكتب تكملة المثل هنا:")


if st.button("تأكد الإجابة"):
    correct_answer = proverbs[st.session_state.current_proverb].strip().lower()
    user_answer_clean = user_answer.strip().lower()


    if user_answer_clean == correct_answer:
        st.success("أشطر كتكوت!")
        # نبدأ مثل جديد
        st.session_state.current_proverb = random.choice(list(proverbs.keys()))
    else:
        st.error("حاول تاني متزعلش")