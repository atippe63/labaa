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

# Streamlit App
st.title('ข้อมูลบุคคล')

# สร้างตารางหากยังไม่มี
create_table()

# แสดงแบบฟอร์มเพื่อเพิ่มข้อมูล
ชื่อ = st.text_input('ชื่อ:')
อายุ = st.number_input('อายุ:')
สาขา_options = ['วิศวกรรมเมคคาทรอนิกส์', 'วิศวกรรมอาหาร', ]
if สาขา_options:
    สาขา = st.selectbox('สาขา:', สาขา_options)
if st.button('เพิ่มข้อมูล'):
    เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)

# แสดงข้อมูลทั้งหมดโดยใช้ Pandas DataFrame
ข้อมูลทั้งหมด = ดึงข้อมูล()
st.write('ข้อมูลทั้งหมด:')
st.write(ข้อมูลทั้งหมด)

# แสดงจำนวนข้อมูลทั้งหมด
จำนวนข้อมูล = นับข้อมูล()
st.write(f'จำนวนข้อมูลทั้งหมด: {จำนวนข้อมูล} รายการ')

# ฟังก์ชันสำหรับล้างข้อมูลทั้งหมด
def ล้างข้อมูลทั้งหมด():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ข้อมูลบุคคล")
    conn.commit()
    conn.close()

# แสดงปุ่มล้างข้อมูล
if st.button('ล้างข้อมูลทั้งหมด'):
    ล้างข้อมูลทั้งหมด()
    st.warning('ล้างข้อมูลทั้งหมดสำเร็จ!')
