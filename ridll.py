import streamlit as st
import random


st.set_page_config(page_title="فوازير حمودي", page_icon="🧠")


st.title("🧠 فوازير حمودي الحسابية")
st.write("حل الفزورة.. عندك 3 محاولات، وبعدها تقدر تعرف الحل!")


# مجموعة فوازير منطقية
riddles = [
    {"question": "ما هو الرقم التالي في السلسلة: 2, 4, 8, 16, ?", "answer": "32"},
    {"question": "إذا كان 3 + 2 × 2 = ?", "answer": "7"},
    {"question": "كم يكون ربع نصف 8؟", "answer": "1"},
    {"question": "فيه 5 تفاحات، أكلت 2، كم معاك؟", "answer": "3"},
    {"question": "ما هو الرقم الناقص: 1، 1، 2، 3، 5، ؟", "answer": "8"},
    {"question": "إذا كان أحمد عنده 3 أقلام، وأخذ منهم 2، كم تبقى معاه؟", "answer": "1"},
    {"question": "ما هو الرقم التالي: 10، 20، 30، ؟", "answer": "40"},
]


# تهيئة الحالة
if "riddle_index" not in st.session_state:
    st.session_state.riddle_index = 0
    st.session_state.attempts = 0
    st.session_state.show_answer = False


riddle = riddles[st.session_state.riddle_index]


st.markdown(f"### الفزورة: {riddle['question']}")


user_answer = st.text_input("اكتب إجابتك هنا:")


# زر تأكيد الإجابة
if st.button("تأكد الإجابة"):
    if user_answer.strip() == "":
        st.warning("اكتب إجابة الأول يا حمودي!")
    elif user_answer.strip() == riddle['answer']:
        st.success("برافو! إجابة صحيحة يا أشطر كتكوت!")
        st.session_state.attempts = 0
        st.session_state.show_answer = False
    else:
        st.session_state.attempts += 1
        st.error(f"غلط! دي المحاولة رقم {st.session_state.attempts}")
        if st.session_state.attempts >= 3:
            st.info("خسرت 3 محاولات، تقدر تشوف الحل أو تختار فزورة جديدة.")
            st.session_state.show_answer = True


# زر عرض الحل
if st.session_state.show_answer:
    if st.button("اعرف الحل"):
        st.markdown(f"### الحل الصحيح هو: **{riddle['answer']}**")


# زر فزورة جديدة
if st.button("فزورة جديدة"):
    st.session_state.riddle_index = (st.session_state.riddle_index + 1) % len(riddles)
    st.session_state.attempts = 0
    st.session_state.show_answer = False
    st.experimental_rerun()


st.caption("فوازير خفيفة من حمودي – فكّر قبل ما تجاوب!")