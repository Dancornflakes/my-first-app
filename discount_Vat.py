import streamlit as st

st.title("App for calculating discount and vat")

Price = st.number_input("Enter Your Price : ",min_value = 0.0, value = 0.0)
DiscountPercent = st.number_input("Enter Your Discount : ",min_value = 0.0, value = 0.0)

Discount = Price * DiscountPercent / 100
DiscountPrice = Price - Discount
Vat = DiscountPrice * 0.07

TotlePrice = DiscountPrice + Vat
st.header(f" Your PRice Totle to: **{TotlePrice:.2f}** บาท")

st.write("แดน วงศ์ไชย แสนสุวงศ์ เลขที่ 41 ม.4/5")
st.write("No AI all hand")

