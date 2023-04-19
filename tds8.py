

import streamlit as st

st.write("Largest of three numbers")

def main():
    st.title("Find the largest number") 
    st.write("Enter three numbers and click the button to find the largest number")
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find the largest number"):
        if numl > num2 and num1 > num3:

            largest_num = numl
        elif num2 > numl and num2 > num3:

            largest_num = num2

        else:
            largest_num = num3

        st.write("The largest number is:", largest_num)

streamlit run largest number.py
