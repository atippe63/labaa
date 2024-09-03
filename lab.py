import sqlite3
import streamlit as st
import pandas as pd

# ฟังก์ชันสำหรับสร้างตารางหากยังไม่มี
def create_table():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ข้อมูลบุคคล (
            ชื่อ TEXT,
            อายุ INTEGER,
            สาขา TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ฟังก์ชันสำหรับเพิ่มข้อมูล
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา):
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ข้อมูลบุคคล VALUES (?, ?, ?)", (ชื่อ, อายุ, สาขา))
    conn.commit()
    conn.close()

# ฟังก์ชันสำหรับดึงข้อมูลทั้งหมดเป็น Pandas DataFrame
def ดึงข้อมูล():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    df = pd.read_sql_query("SELECT * FROM ข้อมูลบุคคล", conn)
    conn.close()
    return df

# ฟังก์ชันสำหรับนับจำนวนข้อมูลทั้งหมด
def นับข้อมูล():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM ข้อมูลบุคคล")
    count = cursor.fetchone()[0]
    conn.close()
    return count

# ฟังก์ชันสำหรับล้างข้อมูลทั้งหมด
def clear_all_data():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ข้อมูลบุคคล")
    conn.commit()
    conn.close()

# Streamlit App
st.title('Project')

# สร้างตารางหากยังไม่มี
create_table()

# หน้าแรก
st.sidebar.title('')
page = st.sidebar.radio('ไปที่', ['หน้าหลัก', 'เพิ่มข้อมูล', 'ดูข้อมูล', 'ล้างข้อมูล'])

if page == 'หน้าหลัก':
    st.title('จำนวนรายชื่อ')
    จำนวนข้อมูล = นับข้อมูล()
    st.write(f'จำนวนข้อมูลทั้งหมด: {จำนวนข้อมูล} รายการ')

elif page == 'เพิ่มข้อมูล':
    st.title('เพิ่มข้อมูลบุคคล')

    # สร้างตาราง
    create_table()

    # แสดงแบบฟอร์มเพื่อเพิ่มข้อมูล
    ชื่อ = st.text_input('ชื่อ:')
    อายุ = st.number_input('อายุ:')
    สาขา_options = ['วศ.บ.วิศวกรรมเมคคาทรอนิกส์', 'วศ.บ.การผลิตและนวัตกรรมอาหาร', ]
    if สาขา_options:
        สาขา = st.selectbox('สาขา:', สาขา_options)
    if st.button('เพิ่มข้อมูล'):
        เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)
        st.warning('เพิ่มข้อมูลทั้งหมดสำเร็จ!')

elif page == 'ดูข้อมูล':
    st.title('ดูข้อมูลบุคคล')

    # แสดงข้อมูลทั้งหมดโดยใช้ Pandas DataFrame
    ข้อมูลทั้งหมด = ดึงข้อมูล()
    st.write('ข้อมูลทั้งหมด:')
    st.write(ข้อมูลทั้งหมด)

elif page == 'ล้างข้อมูล':
    st.title('ล้างข้อมูลทั้งหมดของบุคคล')
    
    # แสดงปุ่มล้างข้อมูล
    if st.button('ล้างข้อมูลทั้งหมด'):
            clear_all_data()
            st.warning('ล้างข้อมูลทั้งหมดสำเร็จ!')
import os
from PIL import Image
import streamlit as st

path = 'C:\\Users\\Admin\\OneDrive\\เดสก์ท็อป\\รายงานสหกิจศึกษา\\S__12509191.jpg'

if os.path.exists(path):
    jpg_file = Image.open(path)
    st.image(jpg_file)
else:
    st.error('ไม่พบรูปภาพใน Path ที่ระบุ')


