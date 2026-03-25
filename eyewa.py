import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Contact Lens Calculator", page_icon="👁️")

# اللوجو
st.image("logo.png", width=500)

st.title("👁️ Contact Lens Calculator")
st.markdown("Enter your spectacle prescription to calculate contact lens power.")

# إدخال البيانات
col1, col2, col3 = st.columns(3)

with col1:
    sph = st.number_input("SPH", value=0.00, step=0.25)

with col2:
    cyl = st.number_input("CYL", value=0.00, step=0.25)

with col3:
    axis = st.number_input("AXIS", value=0, min_value=0, max_value=180)

# زر الحساب
if st.button("Calculate"):

    if axis < 0 or axis > 180:
        st.error("AXIS must be between 0 and 180")
    else:
        d = 0.012

        # أخذ الانحراف بالحسبان
        se = sph + (cyl / 2)

        # حساب العدسة
        if abs(se) < 4:
            cl_power = se
        else:
            cl_power = se / (1 - d * se)

        # تقريب
        cl_power = round(cl_power * 4) / 4

        st.subheader("📊 Result:")
        st.success(f"CL SPH (Adjusted): {cl_power:.2f}")

        # ✅ تحذير: الانحراف أعلى من الاسفير
        if abs(cyl) > abs(sph):
            st.error("🚨 قيمة الانحراف أعلى من الاسفير — يرجى مراجعة أخصائي بصريات فورًا")

        # ✅ تحذير الانحراف العالي + رابط
        if cyl <= -1.50:
            st.warning("⚠️ High astigmatism detected")

            st.markdown("""
يرجى استخدام حاسبة العدسات التوريك من الرابط التالي:

🔗 https://www.jnjvisionpro.com/en-us/calculators/acuvue-fitting-calculator/
""")

        st.markdown("---")

# التعليمات
st.markdown("""
<div style='direction: rtl; text-align: right;'>

### Instructions

يرجى الانتباه:
 1. إذا كان الانحراف أقل من او يساوي 1.00D- فقد يكون الوضوح أقل.
 2. إذا كان الانحراف من 1.25D- الى 1.50- فالرؤية متوسطة.
 3. إذا كان الانحراف أعلى من 1.50D- يفضل استخدام عدسات Toric.
 4. إذا ظهر المقاس أكثر من ±4.00D الرجاء مراجعة أخصائي بصريات.

</div>
""", unsafe_allow_html=True)
