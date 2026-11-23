import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# :red[💪 คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

#3 start calculating
if st.button("calculate BMI"):
  # CHANGE CM TO MAND CALCULATE BMI
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  st.write("---")
  st.header(f"your bmi is : **{bmi:.2f}**")

#4 bmi someting idk lol
  if bmi < 18.5:
    st.warning("eat food bro your too skinny")
  elif 18.5 <= bmi < 23.0:
    st.succeess("your normal boy")
  elif 23.0 <= bmi < 25.0:
    st.info("kinda starting to be fat")
  else:
    st.error("why are you so fat")


  st.divider()
  st.write("Dan Wongchai Saensuwong No.41 M4/5")
