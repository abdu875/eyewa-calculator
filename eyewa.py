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

        # ✅ حساب Spherical Equivalent (أخذ الانحراف بالحسبان)
        se = sph + (cyl / 2)

        # ✅ تطبيق Vertex Distance
        if abs(se) < 4:
            cl_power = se
        else:
            cl_power = se / (1 - d * se)

        # تقريب لأقرب 0.25
        cl_power = round(cl_power * 4) / 4

        # عرض النتيجة
        st.subheader("📊 Result:")
        st.success(f"CL SPH (Adjusted): {cl_power:.2f}")

        # ✅ تنبيه حسب قيمة CYL
        if cyl <= -1.50:
            st.warning("⚠️ High astigmatism detected: Toric lenses are recommended.")
        elif cyl <= -1.00:
            st.info("ℹ️ Moderate astigmatism: Vision may be slightly reduced with spherical lenses.")

        st.markdown("---")

st.markdown("""
<div style='direction: rtl; text-align: right;'>

### Instructions

يرجى الانتباه:
 1. إذا كان الانحراف أقل من او يساوي 1.00D- فقد يكون الوضوح بالعدسات اللاصقة أقل من النظارة، ويصل تقريباً إلى 80% من وضوح النظارة.
 2. إذا كان الانحراف  من 1.25D- الى 1.50-  فغالباً سيكون الوضوح بالعدسات بين 60% إلى 70% تقريباً مقارنة بالنظارة.
 3. إذا كان الانحراف أعلى من 1.50D-  فعدسات Toric (عدسات للانحراف) هي الخيار الأفضل، لأن الوضوح بالعدسات العادية سيكون ضعيفاً.
 4. إذا ظهر لك مقاس العدسات اللاصقة أكثر من ±4.00D الرجاء الرجوع إلى دكتور البصريات لتحديد المقاس المناسب
</div>
""", unsafe_allow_html=True)
