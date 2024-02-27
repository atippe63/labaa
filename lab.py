import streamlit as st
import pandas as pd

# สร้างตารางหากยังไม่มี
def create_table():
    return pd.DataFrame(columns=['ชื่อ', 'อายุ', 'สาขา'])

# ตั้งค่าลักษณะของหน้าแอป
st.set_page_config(page_title='ข้อมูลบุคคล', page_icon='🧑‍💼', layout='wide')

# ฟังก์ชันสำหรับเพิ่มข้อมูล
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา, df):
    new_data = pd.DataFrame({'ชื่อ': [ชื่อ], 'อายุ': [อายุ], 'สาขา': [สาขา]})
    df = pd.concat([df, new_data], ignore_index=True)
    return df

# ฟังก์ชันสำหรับลบข้อมูลทั้งหมด
def ลบข้อมูลทั้งหมด(df):
    return pd.DataFrame(columns=['ชื่อ', 'อายุ', 'สาขา'])

# ฟังก์ชันสำหรับลบข้อมูลตามชื่อ
def ลบข้อมูลตามชื่อ(ชื่อ, df):
    df = df[df['ชื่อ'] != ชื่อ]
    return df

# ฟังก์ชันสำหรับนับจำนวนผู้ใช้
def count_users(df):
    return len(df)

# Streamlit App
st.title('ข้อมูลบุคคล')

# สร้างตารางหากยังไม่มี
if 'data' not in st.session_state:
    st.session_state.data = create_table()

# ตรวจสอบว่าผู้ใช้เข้าสู่ระบบหรือไม่
is_logged_in = st.session_state.is_logged_in if 'is_logged_in' in st.session_state else False

# แสดงฟอร์มสำหรับเพิ่มข้อมูล
if is_logged_in:
    ชื่อ = st.text_input('ชื่อ:')
    อายุ = st.number_input('อายุ:')
    สาขา = st.text_input('สาขา:')
    if st.button('เพิ่มข้อมูล'):
        st.session_state.data = เพิ่มข้อมูล(ชื่อ, อายุ, สาขา, st.session_state.data)

    # แสดงข้อมูลทั้งหมดเป็น Pandas DataFrame
    st.write('ข้อมูลทั้งหมด:')
    st.write(st.session_state.data)

    # ปุ่มลบข้อมูลทั้งหมด
    if st.button('ล้างข้อมูลทั้งหมด'):
        st.session_state.data = ลบข้อมูลทั้งหมด(st.session_state.data)
        st.warning('ล้างข้อมูลทั้งหมดสำเร็จ!')

    # แสดงจำนวนผู้ใช้
    st.write(f'จำนวนผู้ใช้งาน: {count_users(st.session_state.data)}')

# แสดงปุ่มเข้าสู่ระบบถ้ายังไม่ได้เข้าสู่ระบบ
else:
    if st.button('เข้าสู่ระบบ'):
        # แสดงจำนวนผู้ใช้
        st.write(f'จำนวนผู้ใช้งาน: {count_users(st.session_state.data)}')
        st.session_state.is_logged_in = True