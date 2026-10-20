
import streamlit as st
from datetime import datetime

# تنظیمات صفحه
st.set_page_config(
    page_title="دستیار هوشمند تاجر موفق",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# استایل‌دهی فارسی (RTL)
st.markdown("""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');
    html, body, [class*="css"]  {
        font-family: 'Vazirmatn', sans-serif;
        direction: rtl;
        text-align: right;
    }
    .stCheckbox { font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# عنوان نرم‌افزار
st.title("🚀 دستیار هوشمند و نقشه راه تاجر موفق")
st.caption("مدیریت گام‌به‌گام زنجیره تجارت، لوجستیک و صادرات (سرخس - دنغره)")

# تعریف مراحل ۶گانه تجارت موفق
STAGES = {
    "مرحله ۱: زیرساخت حقوقی و استراتژی": [
        "ثبت شرکت و علامت تجاری (در منطقه آزاد دنغره/سرخس)",
        "افتتاح حساب‌های بانکی و صرافی‌های معتبر",
        "تنظیم توافق‌نامه سهام‌داران (SHA) و عدم افشا (NDA)",
        "تعیین محصول هدف و حوزه فعالیت (مثل میلگرد و مصالح)",
        "تحقیقات بازار مقصد (قوانین گمرکی تاجیکستان)"
    ],
    "مرحله ۲: بازاریابی و جذب مشتری/شریک": [
        "آماده‌سازی کاتالوگ و پروپوزال‌های مشارکت (BOT)",
        "ارسال دعوت‌نامه برای کارخانجات فولاد و مصالح‌فروشان",
        "هماهنگی جلسات در اتاق بازرگانی مشهد",
        "امضای تفاهم‌نامه اولیه (MoU) با شرکا"
    ],
    "مرحله ۳: امور گمرکی و استانداردها": [
        "اخذ استانداردها و گواهی‌های کیفی محصول",
        "استعلام کد HS و تعرفه‌های گمرکی مسیر",
        "تنظیم پروفرما (پیش‌فاکتور) طبق اصول Incoterms 2020",
        "اخذ مجوزهای صادراتی و کارت بازرگانی"
    ],
    "مرحله ۴: لجستیک، زنجیره تامین و انبارداری": [
        "مدیریت زمین ۱۳,۰۰۰ متری در منطقه آزاد دنغره",
        "هماهنگی ترانزیت ریلی و جاده‌ای از مرز سرخس",
        "صدور کارنه تیر (TIR Carnet) و بیمه بین‌المللی بار",
        "راه‌اندازی انبار و محوطه دپوی کالا در مقصد"
    ],
    "مرحله ۵: مدیریت مالی و تسویه‌حساب": [
        "تعیین روش پرداخت و تسویه ارزی",
        "دریافت پیش‌پرداخت یا توافق فروش امانی (Consignment)",
        "تنظیم اسناد تجاری (سیاهه، پکینگ لیست، گواهی مبدأ)",
        "محاسبه سود خالص و مدیریت هزینه‌های پنهان"
    ],
    "مرحله ۶: توسعه و ارزیابی": [
        "نظرسنجی کیفیت و ارزیابی عملکرد لجستیکی",
        "توسعه ظرفیت سوله‌ها و جذب شرکای جدید",
        "بازسرمایه‌گذاری سود برای توسعه زیرساخت"
    ]
}

# نوار کناری برای انتخاب مرحله
st.sidebar.header("📌 مراحل تجارت")
selected_stage = st.sidebar.radio("انتخاب مرحله فعال:", list(STAGES.keys()))

# نمایش بخش اصلی نرم‌افزار
st.subheader(f"🔍 {selected_stage}")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### 📋 چک‌لیست اقدامات اجرایی:")
    completed_count = 0
    total_tasks = len(STAGES[selected_stage])
    
    for task in STAGES[selected_stage]:
        status = st.checkbox(task, key=f"{selected_stage}_{task}")
        if status:
            completed_count += 1

    progress = completed_count / total_tasks
    st.write("---")
    st.write(f"**میزان پیشرفت در این مرحله:** {int(progress * 100)}%")
    st.progress(progress)

with col2:
    st.write("### 📝 یادداشت‌ها و پیگیری‌ها:")
    notes = st.text_area(
        "یادداشت‌های مهم، تماس‌ها و پیگیری‌های این گام:",
        height=200,
        key=f"notes_{selected_stage}"
    )
    if st.button("ثبت و ذخیره یادداشت"):
        st.success("یادداشت شما با موفقیت ثبت شد.")

# بخش ابزارهای کاربردی تاجر
st.write("---")
st.header("🛠 ابزارهای کمکی سریع تاجر")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.write("#### 📐 محاسبه‌گر سود تقریبی")
    buy_price = st.number_input("قیمت خرید کالا (دلار):", value=1000)
    transit_cost = st.number_input("هزینه لجستیک و گمرک (دلار):", value=200)
    sell_price = st.number_input("قیمت فروش در مقصد (دلار):", value=1500)
    
    profit = sell_price - (buy_price + transit_cost)
    st.info(f"سود ناخالص برآوردی: **{profit} دلار**")

with col_b:
    st.write("#### 🌐 قوانین اینکوترمز ۲۰۲۰")
    incoterm = st.selectbox("انتخاب اینکوترمز:", ["FOB", "CIF", "CFR", "DDP", "FCA", "EXW"])
    incoterm_info = {
        "EXW": "تحویل در درب کارخانه فروشنده.",
        "FCA": "تحویل به حمل‌کننده در مبدأ.",
        "FOB": "تحویل روی عرشه کشتی/وسیله در مبدأ.",
        "CFR": "ارزش کالا + کرایه حمل تا مقصد.",
        "CIF": "ارزش کالا + بیمه + کرایه حمل.",
        "DDP": "تحویل در مقصد با پرداخت تمام عوارض."
    }
    st.warning(incoterm_info[incoterm])

with col_c:
    st.write("#### ⏰ یادآور گام بعدی")
    reminder_date = st.date_input("تاریخ جلسات یا پیگیری:")
    reminder_text = st.text_input("موضوع جلسه:")
    if st.button("افزودن به تقویم کاری"):
        st.success(f"یادآور '{reminder_text}' ثبت شد.")
