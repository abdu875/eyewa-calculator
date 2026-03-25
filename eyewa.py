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

        # SPH = 0
        if sph == 0:
            cl_power = 0
        else:
            if abs(cyl) > abs(sph):
                se = sph + (cyl / 4)
            else:
                se = sph + (cyl / 2)

            if abs(se) < 4:
                cl_power = se
            else:
                cl_power = se / (1 - d * se)

            cl_power = round(cl_power * 4) / 4

        st.subheader("📊 Result:")
        st.success(f"CL SPH (Adjusted): {cl_power:.2f}")

        # حالة خاصة (1)
        if abs(cyl) > abs(sph) and sph != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#fff3cd; padding:10px; border-radius:8px; color:#856404; font-weight:bold;'>
            حالة خاصة (1): تم استخدام ربع قيمة الانحراف (CYL/4) في الحساب لأن قيمة الانحراف أعلى من قيمة SPH.
            </div>
            """, unsafe_allow_html=True)

        # حالة خاصة (2)
        if sph == 0 and cyl != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#e6f0ff; padding:10px; border-radius:8px; color:#003366; font-weight:bold;'>
            حالة خاصة (2): بيور استجماتيزم — عدسات التوريك هي الحل الأمثل.<br><br>
            ملاحظة: في حال استخدام عدسات ملونة، ستكون للزينة فقط ولن تعطي تصحيحًا للنظر.
            </div>
            """, unsafe_allow_html=True)

        # تحذير الانحراف العالي
        if cyl <= -1.50:
            st.warning("⚠️ High astigmatism detected")

        # ✅ الرابط (الشرط الجديد)
        if cyl <= -0.50:
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
