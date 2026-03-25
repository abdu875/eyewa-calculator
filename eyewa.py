import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="Contact Lens Calculator", page_icon="👁️")

# اللوجو
st.image("logo.png", width=300)

st.title("👁️ Contact Lens Calculator")
st.markdown("Enter prescription for each eye separately.")

# تقسيم الصفحة
col_right, col_left = st.columns(2)

# =========================
# 👁️ العين اليمنى (OD)
# =========================
with col_right:
    st.header("👁️ Right Eye (OD)")
    sph_r = st.number_input("SPH (OD)", value=0.00, step=0.25, key="sph_r")
    cyl_r = st.number_input("CYL (OD)", value=0.00, step=0.25, key="cyl_r")
    axis_r = st.number_input("AXIS (OD)", value=0, min_value=0, max_value=180, key="axis_r")

# =========================
# 👁️ العين اليسرى (OS)
# =========================
with col_left:
    st.header("👁️ Left Eye (OS)")
    sph_l = st.number_input("SPH (OS)", value=0.00, step=0.25, key="sph_l")
    cyl_l = st.number_input("CYL (OS)", value=0.00, step=0.25, key="cyl_l")
    axis_l = st.number_input("AXIS (OS)", value=0, min_value=0, max_value=180, key="axis_l")

# زر الحساب
if st.button("Calculate"):

    d = 0.012

    def calculate_eye(sph, cyl):
        # SPH = 0
        if sph == 0:
            return 0, False

        # حالة خاصة (1)
        if abs(cyl) > abs(sph):
            se = sph + (cyl / 4)
            case1 = True
        else:
            se = sph + (cyl / 2)
            case1 = False

        # Vertex
        if abs(se) < 4:
            cl_power = se
        else:
            cl_power = se / (1 - d * se)

        cl_power = round(cl_power * 4) / 4

        return cl_power, case1

    # حساب العينين
    result_r, case1_r = calculate_eye(sph_r, cyl_r)
    result_l, case1_l = calculate_eye(sph_l, cyl_l)

    st.markdown("---")

    col_res1, col_res2 = st.columns(2)

    # =========================
    # نتائج العين اليمنى
    # =========================
    with col_res1:
        st.subheader("👁️ Right Eye Result")
        st.success(f"CL SPH (Adjusted): {result_r:.2f}")

        # حالة خاصة (1)
        if abs(cyl_r) > abs(sph_r) and sph_r != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#fff3cd; padding:10px; border-radius:8px; color:#856404; font-weight:bold;'>
            حالة خاصة (1): تم استخدام ربع قيمة الانحراف (CYL/4) في الحساب لأن قيمة الانحراف أعلى من قيمة SPH.
            </div>
            """, unsafe_allow_html=True)

        # حالة خاصة (2)
        if sph_r == 0 and cyl_r != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#e6f0ff; padding:10px; border-radius:8px; color:#003366; font-weight:bold;'>
            حالة خاصة (2): بيور استجماتيزم — عدسات التوريك هي الحل الأمثل.<br><br>
            ملاحظة: في حال استخدام عدسات ملونة، ستكون للزينة فقط ولن تعطي تصحيحًا للنظر.
            </div>
            """, unsafe_allow_html=True)

        # تحذير
        if cyl_r <= -1.50:
            st.warning("⚠️ High astigmatism detected")

        # الرابط
        if cyl_r <= -0.50:
            st.markdown("🔗 https://www.jnjvisionpro.com/en-us/calculators/acuvue-fitting-calculator/")

    # =========================
    # نتائج العين اليسرى
    # =========================
    with col_res2:
        st.subheader("👁️ Left Eye Result")
        st.success(f"CL SPH (Adjusted): {result_l:.2f}")

        # حالة خاصة (1)
        if abs(cyl_l) > abs(sph_l) and sph_l != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#fff3cd; padding:10px; border-radius:8px; color:#856404; font-weight:bold;'>
            حالة خاصة (1): تم استخدام ربع قيمة الانحراف (CYL/4) في الحساب لأن قيمة الانحراف أعلى من قيمة SPH.
            </div>
            """, unsafe_allow_html=True)

        # حالة خاصة (2)
        if sph_l == 0 and cyl_l != 0:
            st.markdown("""
            <div style='direction: rtl; text-align: right; background-color:#e6f0ff; padding:10px; border-radius:8px; color:#003366; font-weight:bold;'>
            حالة خاصة (2): بيور استجماتيزم — عدسات التوريك هي الحل الأمثل.<br><br>
            ملاحظة: في حال استخدام عدسات ملونة، ستكون للزينة فقط ولن تعطي تصحيحًا للنظر.
            </div>
            """, unsafe_allow_html=True)

        # تحذير
        if cyl_l <= -1.50:
            st.warning("⚠️ High astigmatism detected")

        # الرابط
        if cyl_l <= -0.50:
            st.markdown("🔗 https://www.jnjvisionpro.com/en-us/calculators/acuvue-fitting-calculator/")

# =========================
# التعليمات (كما كانت)
# =========================
st.markdown("""
<div style='direction: rtl; text-align: right;'>

### Instructions

يرجى الانتباه:
 1. إذا كان الانحراف أقل من او يساوي 1.00D- فقد يكون الوضوح أقل من النظارة.
 2. إذا كان الانحراف من 1.25D- الى 1.50- فغالباً يكون الوضوح متوسط.
 3. إذا كان الانحراف أعلى من 1.50D- يفضل استخدام عدسات Toric.


</div>
""", unsafe_allow_html=True)
