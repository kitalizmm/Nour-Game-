# file: nour_game.py
import streamlit as st
import random


st.title("لعبة نور")
st.subheader("نور فكرت في حاجة... وانت لازم تخمن هي فكرت في إيه!")


# الحاجات اللي ممكن نور تفكر فيها
categories = {
    "فاكهة": ["تفاح", "موز", "برتقال", "عنب", "مانجو"],
    "لون": ["أحمر", "أخضر", "أزرق", "أصفر", "بنفسجي"],
    "حيوان": ["قطة", "كلب", "أسد", "فيل", "نمر"]
}


if "category" not in st.session_state:
    st.session_state.category = random.choice(list(categories.keys()))
    st.session_state.answer = random.choice(categories[st.session_state.category])


st.write(f"نور فكرت في: {st.session_state.category}، حاول تخمن!")


user_guess = st.text_input("اكتب تخمينك بالعربي:")


if st.button("خمن"):
    if user_guess.strip() == "":
        st.warning("اكتب تخمينك الأول")
    elif user_guess.strip() == st.session_state.answer:
        st.success("برافو! خمنت اللي نور كانت بتفكر فيه")
        # نبدأ لعبة جديدة
        st.session_state.category = random.choice(list(categories.keys()))
        st.session_state.answer = random.choice(categories[st.session_state.category])
    else:
        st.error("غلط! نور مكنتش بتفكر في دي. جرب تاني.")


st.caption("كل مرة اللعبة هتتغير تلقائيًا لو خمنت صح.")