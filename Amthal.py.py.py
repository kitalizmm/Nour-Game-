import streamlit as st
import random


st.set_page_config(page_title="لعبة اكمل المثل", page_icon="🧠")


st.title("🧩 لعبة اكمل المثل")
st.write("حاول تكمل المثل الشعبي... لو جاوبت صح هتاخد لقب **أشطر كتكوت**!")


# مجموعة الأمثال
proverbs = {
    "اللي اختشوا": "ماتوا",
    "امشي عدل": "يحتار عدوك فيك",
    "اللي يعيش ياما": "يشوف",
    "يا بخت اللي": "يعرف قدر نفسه",
    "الغايب عذره": "معاه",
    "يارب": "اتجوزك",
    "كل تأخيرة": "وفيها خيرة",
    "الوقت كالسيف": "إن لم تقطعه قطعك"
}


# تهيئة الحالة
if "current_proverb" not in st.session_state:
    st.session_state.current_proverb = random.choice(list(proverbs.keys()))
    st.session_state.attempts = 0
    st.session_state.revealed = False


# عرض المثل
st.markdown(f"### اكمل المثل: **{st.session_state.current_proverb} ...**")


# إدخال المستخدم
user_answer = st.text_input("اكتب التكملة هنا (بالعربي):")


# زر التحقق
if st.button("تأكد الإجابة"):
    correct_answer = proverbs[st.session_state.current_proverb].strip().lower()
    user_answer_clean = user_answer.strip().lower()


    if user_answer_clean == "":
        st.warning("اكتب حاجة يا حمودي!")
    elif user_answer_clean == correct_answer:
        st.success("أشطر كتكوت!")
        # نبدأ مثل جديد
        st.session_state.current_proverb = random.choice(list(proverbs.keys()))
        st.session_state.attempts = 0
        st.session_state.revealed = False
    else:
        st.session_state.attempts += 1
        st.error("حاول تاني متزعلش")


        if st.session_state.attempts >= 3:
            if not st.session_state.revealed:
                st.info(f"الإجابة الصحيحة كانت: **{correct_answer}**")
                st.session_state.revealed = True


# زر لتغيير المثل يدويًا
if st.button("عايز مثل جديد"):
    st.session_state.current_proverb = random.choice(list(proverbs.keys()))
    st.session_state.attempts = 0
    st.session_state.revealed = False
    st.experimental_rerun()


# تذييل
st.caption("لعبة مصرية خفيفة من تصميم حمودي")