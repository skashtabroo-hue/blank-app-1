import streamlit as st
from datetime import datetime

# تنظیمات اصلی صفحه
st.set_page_config(
    page_title="سامانه جامع مدیریت تجاری و لجستیک دنغره",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# اعمال تم رنگی سبز، طلایی، کرم و فونت‌های استاندارد
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lalezar&family=Vazirmatn:wght@300;400;700&display=swap');

    /* استایل کلی و رنگ پس‌زمینه کرم روشن */
    .stApp {
        background-color: #FDFBF7 !important;
    }
    
    html, body, [class*="css"], .stMarkdown, p, div, span, label {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        color: #1E293B;
        font-size: 16px;
    }

    /* عناوین با فونت لاله‌زار و رنگ سبز تیره / طلایی */
    h1, h2, h3, h4, .stTitle, .stHeader {
        font-family: 'Lalezar', cursive !important;
        color: #064E3B !important;
        letter-spacing: 0.5px;
    }

    h1 { font-size: 2.5rem !important; color: #064E3B !important; }
    h2 { font-size: 2rem !important; color: #064E3B !important; }
    h3 { font-size: 1.6rem !important; color: #B45309 !important; }

    /* دکمه‌های با تم طلایی و سبز */
    .stButton > button {
        font-family: 'Lalezar', cursive !important;
        font-size: 1.2rem !important;
        background: linear-gradient(135deg, #064E3B 0%, #047857 100%) !important;
        color: #FDFBF7 !important;
        border-radius: 12px !important;
        padding: 10px 24px !important;
        border: 1px solid #D97706 !important;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #D97706 0%, #B45309 100%) !important;
        color: white !important;
    }

    /* نوار کناری (Sidebar) با تم کرم و حاشیه سبز */
    section[data-testid="stSidebar"] {
        background-color: #F4F1EA !important;
        border-left: 2px solid #D97706;
    }
    section[data-testid="stSidebar"] .stRadio label {
        font-size: 1.1rem !important;
        font-weight: bold;
        color: #064E3B !important;
    }

    /* کارت‌ها و باکس‌ها */
    div.stAlert {
        background-color: #FEF3C7 !important;
        border: 1px solid #D97706 !important;
        color: #78350F !important;
    }
    </style>
    """, unsafe_allow_html=True)

# مدیریت حافظه موقت برای ذخیره پارتنرها در طول نشست
if "partners" not in st.session_state:
    st.session_state["partners"] = [
        {
            "name": "مجتمع فولاد اصفهان (نمونه)",
            "rep": "مهندس رضایی",
            "product": "میلگرد آجدار (A3)",
            "capacity": "5000 تن در ماه",
            "phone": "09120000000"
        }
    ]

# عنوان اصلی نرم‌افزار
st.title("🏛️ سامانه جامع مدیریت لجستیک و جذب شرکای تجاری (دنغره - سرخس)")
st.caption("طراحی‌شده برای توسعه زیرساخت‌های تجاری، صدور دعوت‌نامه‌ها و پروپوزال‌های تخصصی BOT")

# منوی ناوبری اصلی برنامه
menu_choice = st.sidebar.radio(
    "📌 انتخاب بخش اصلی سامانه:",
    [
        "📋 نقشه راه و چک‌لیست‌های اجرایی",
        "🏭 مدیریت کارخانجات و ثبت شرکا",
        "✉️ صدور خودکار دعوت‌نامه رسمی",
        "📊 پروپوزال‌ساز هوشمند BOT",
        "🛠 ابزارهای مالی و اینکوترمز"
    ]
)

# ----------------------------------------------------
# بخش ۱: نقشه راه و چک‌لیست‌ها
# ----------------------------------------------------
if menu_choice == "📋 نقشه راه و چک‌لیست‌های اجرایی":
    st.header("📋 نقشه راه گام‌به‌گام عملیاتی‌سازی هولدینگ")
    
    STAGES = {
        "مرحله ۱: زیرساخت حقوقی و استراتژی": [
            "ثبت شرکت و علامت تجاری (منطقه آزاد دنغره / سرخس)",
            "افتتاح حساب‌های بانکی و صرافی‌های معتبر",
            "تنظیم توافق‌نامه سهام‌داران (SHA) و عدم افشا (NDA)",
            "تحقیقات بازار مقصد و قوانین گمرکی تاجیکستان"
        ],
        "مرحله ۲: بازاریابی و جذب مشتری/شریک": [
            "آماده‌سازی کاتالوگ و پروپوزال‌های مشارکت (BOT)",
            "ارسال دعوت‌نامه رسمی برای کارخانجات فولاد و مصالح‌فروشان",
            "برگزاری جلسات هماهنگی در اتاق بازرگانی مشهد",
            "امضای تفاهم‌نامه اولیه (MoU) با تولیدکنندگان"
        ],
        "مرحله ۳: امور گمرکی و استانداردها": [
            "اخذ استانداردهای کیفی محصول برای صادرات",
            "استعلام کد HS و تعرفه‌های گمرکی مسیر ترانزیت",
            "تنظیم پروفرما (پیش‌فاکتور) طبق اصول Incoterms 2020",
            "اخذ مجوزهای صادراتی و کارت بازرگانی"
        ],
        "مرحله ۴: لجستیک، زنجیره تامین و انبارداری": [
            "مدیریت زمین ۱۳,۰۰۰ متری در منطقه آزاد دنغره",
            "هماهنگی ترانزیت ریلی و جاده‌ای از مرز سرخس",
            "صدور کارنه تیر (TIR Carnet) و بیمه بین‌المللی بار",
            "راه‌اندازی انبار و محوطه دپوی مصالح در مقصد"
        ]
    }

    selected_stage = st.selectbox("انتخاب مرحله جهت پیگیری:", list(STAGES.keys()))
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(f"🔍 اقدامات: {selected_stage}")
        completed = 0
        for task in STAGES[selected_stage]:
            if st.checkbox(task, key=f"t_{selected_stage}_{task}"):
                completed += 1
        
        progress = completed / len(STAGES[selected_stage])
        st.write(f"**پیشرفت این مرحله:** {int(progress * 100)}%")
        st.progress(progress)

    with col2:
        st.subheader("📝 یادداشت‌های اجرایی")
        st.text_area("ثبت نکات و پیگیری‌های این گام:", height=180, key=f"note_{selected_stage}")
        if st.button("ذخیره یادداشت"):
            st.success("یادداشت با موفقیت ثبت شد.")

# ----------------------------------------------------
# بخش ۲: مدیریت کارخانجات و ثبت شرکا
# ----------------------------------------------------
elif menu_choice == "🏭 مدیریت کارخانجات و ثبت شرکا":
    st.header("🏭 ثبت و مدیریت کارخانجات و تولیدکنندگان متقاضی")
    st.write("در این بخش می‌توانید اطلاعات کارخانجات فولاد و مصالحی که برای همکاری اعلام آمادگی کرده‌اند را ثبت کنید.")

    with st.form("partner_form"):
        col1, col2 = st.columns(2)
        with col1:
            p_name = st.text_input("نام کارخانه / شرکت:")
            p_rep = st.text_input("نام شخص مسئول / نماینده:")
        with col2:
            p_product = st.text_input("محصول اصلی (مثلاً میلگرد A3، پروفیل):")
            p_capacity = st.text_input("ظرفیت پیشنهادی صادراتی:")
        
        p_phone = st.text_input("شماره تماس / راه‌های ارتباطی:")
        
        submitted = st.form_submit_button("➕ ثبت اطلاعات کارخانه در سامانه")
        if submitted:
            if p_name and p_product:
                st.session_state["partners"].append({
                    "name": p_name,
                    "rep": p_rep,
                    "product": p_product,
                    "capacity": p_capacity,
                    "phone": p_phone
                })
                st.success(f"شرکت '{p_name}' با موفقیت در لیست شرکا ذخیره شد!")
            else:
                st.warning("لطفاً حداقل نام کارخانه و محصول را وارد کنید.")

    st.subheader("📋 لیست شرکت‌های ثبت‌شده آماده همکاری:")
    for idx, partner in enumerate(st.session_state["partners"]):
        with st.expander(f"🏢 {partner['name']} - محصول: {partner['product']}"):
            st.write(f"**نماینده محترم:** {partner['rep']}")
            st.write(f"**ظرفیت پیشنهادی:** {partner['capacity']}")
            st.write(f"**اطلاعات تماس:** {partner['phone']}")

# ----------------------------------------------------
# بخش ۳: صدور خودکار دعوت‌نامه رسمی
# ----------------------------------------------------
elif menu_choice == "✉️ صدور خودکار دعوت‌نامه رسمی":
    st.header("✉️ صدور خودکار دعوت‌نامه همکاری تجاری")
    st.write("با انتخاب نام شرکت از لیست زیر، دعوت‌نامه رسمی و تخصصی مشارکت در پروژه لجستیکی دنغره به صورت خودکار صادر می‌شود.")

    if not st.session_state["partners"]:
        st.warning("ابتدا حداقل یک کارخانه را در بخش «مدیریت کارخانجات» ثبت کنید.")
    else:
        partner_names = [p["name"] for p in st.session_state["partners"]]
        selected_p_name = st.selectbox("انتخاب شرکت هدف:", partner_names)
        
        # پیدا کردن اطلاعات پارتنر انتخابی
        selected_partner = next(p for p in st.session_state["partners"] if p["name"] == selected_p_name)

        # متن دعوت‌نامه خودکار
        invitation_text = f"""
جناب آقای/سرکار خانم {selected_partner['rep']}
مدیرعامل محترم محترم {selected_partner['name']}

موضوع: دعوت به مشارکت استراتژیک و ایجاد هاب لجستیک و توزیع مصالح ساختمانی در منطقه آزاد دنغره (تاجیکستان)

با سلام و احترام؛
پیرو مذاکرات و بررسی‌های به‌عمل‌آآمده پیرامون ظرفیت‌های صادراتی محصولات آن مجموعه وزین ({selected_partner['product']}) به بازارهای مستعد آسیای میانه، به استحضار می‌رساند هولدینگ تجاری ما با در اختیار داشتن **۱۳,۰۰۰ متر مربع زمین اختصاصی در منطقه آزاد تجاری دنغره (تاجیکستان)** و تسلط بر زنجیره تأمین مرزی (پایانه مرزی سرخس)، آمادگی خود را جهت انعقاد تفاهم‌نامه همکاری به روش **BOT و توزیع امانی (Consignment)** اعلام می‌دارد.

با توجه به ظرفیت پیشنهادی آن شرکت ({selected_partner['capacity']})، راه‌اندازی این هاب لجستیکی مشترک می‌تواند سهم عمده‌ای از بازار هدف را با کمترین ریسک ترانزیتی پوشش دهد. 

لذا از جنابعالی/سرکار عالی دعوت به عمل می‌آید جهت نهایی‌سازی شرایط همکاری و بازدید از زیرساخت‌های مرزی، در جلسه مشترک اتاق بازرگانی مشهد حضور به هم رسانید.

با تجدید احترام،
مدیریت هولدینگ لجستیک و بازرگانی دنغره-سرخس
تاریخ صدور: {datetime.now().strftime('%Y/%m/%d')}
        """

        st.text_area("متن دعوت‌نامه رسمی آماده‌شده:", value=invitation_text, height=350)
        st.info("💡 می‌توانید متن بالا را کپی کرده و به صورت رسمی برای شرکت مورد نظر ارسال نمایید.")

# ----------------------------------------------------
# بخش ۴: پروپوزال‌ساز هوشمند BOT
# ----------------------------------------------------
elif menu_choice == "📊 پروپوزال‌ساز هوشمند BOT":
    st.header("📊 تولید پروپوزال اختصاصی مشارکت (BOT / امانی)")
    st.write("پروپوزال تجاری اختصاصی بر اساس مشخصات و ظرفیت تولیدکننده.")

    if not st.session_state["partners"]:
        st.warning("لطفاً ابتدا شرکتی را در بخش مدیریت شرکا ثبت کنید.")
    else:
        p_names = [p["name"] for p in st.session_state["partners"]]
        chosen_partner = st.selectbox("انتخاب شرکت برای تهیه پروپوزال:", p_names)
        target_partner = next(p for p in st.session_state["partners"] if p["name"] == chosen_partner)

        if st.button("⚙️ تولید پروپوزال اختصاصی"):
            st.success("پروپوزال اختصاصی با موفقیت آماده شد!")
            
            st.markdown(f"""
            ---
            ### 📄 طرح پیشنهادی همکاری (Proposal)
            **مخاطب:** {target_partner['name']} ({target_partner['rep']})  
            **محصول محوری:** {target_partner['product']}  
            **ظرفیت توافقی:** {target_partner['capacity']}  

            #### ۱. مدل همکاری (BOT & Consignment)
            * **ساخت و توسعه (Build):** تجهیز انبارهای اختصاصی در زمین ۱۳,۰۰۰ متری دنغره متناسب با استانداردهای نگهداری فولاد و مصالح.
            * **بهره‌برداری (Operate):** دپوی امانی کالا، بازاریابی مستقیم در تاجیکستان و مدیریت ترانزیت از مرز سرخس.
            * **انتقال/تسویه (Transfer):** تسویه حساب ارزی به صورت دوره‌ای پس از فروش قطعی به پروژه‌های عمرانی مقصد.

#### ۲. مزیت‌های رقابتی پروژه
* معافیت‌های مالیاتی و گمرکی منطقه آزاد دنغره.
* حذف واسطه‌ها و فروش مستقیم به سازندگان کلان تاجیکستان.
* پشتیبانی لجستیک ریلی و جاده‌ای امن از طریق پایانه سرخس.
            ---
            """)

# ----------------------------------------------------
# بخش ۵: ابزارهای مالی و اینکوترمز
# ----------------------------------------------------
elif menu_choice == "🛠 ابزارهای مالی و اینکوترمز":
    st.header("🛠 ابزارهای محاسباتی و تجاری تاجر")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("📐 محاسبه‌گر سود صادراتی")
        buy_p = st.number_input("قیمت خرید در مبدأ (دلار):", value=1000)
        logistics_c = st.number_input("هزینه لجستیک تا دنغره (دلار):", value=250)
        sell_p = st.number_input("قیمت فروش نهایی در مقصد (دلار):", value=1600)
        
        net_profit = sell_p - (buy_p + logistics_c)
        st.success(f"سود خالص برآوردی هر واحد: **{net_profit} دلار**")

    with col_b:
        st.subheader("🌐 راهنمای اینکوترمز ۲۰۲۰")
        incoterm_type = st.selectbox("انتخاب قانون تجاری:", ["EXW", "FOB", "CFR", "CIF", "DDP"])
        descriptions = {
            "EXW": "تحویل در درب کارخانه فروشنده (حداقل مسئولیت فروشنده).",
            "FOB": "تحویل روی وسیله حمل در مبدأ (بندر/مرز).",
            "CFR": "ارزش کالا به اضافه کرایه حمل تا مرز مقصد.",
            "CIF": "ارزش کالا + بیمه بین‌المللی + کرایه حمل.",
            "DDP": "تحویل در انبار مقصد (دنغره) با پرداخت کامل عوارض توسط فروشنده."
        }
        st.warning(descriptions[incoterm_type])
