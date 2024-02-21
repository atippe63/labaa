import streamlit as st
import sqlite3
import pandas as pd
import os

# เชื่อมต่อกับฐานข้อมูล SQLite
conn = sqlite3.connect('ข้อมูลบุคคล')
cursor = conn.cursor()

# สร้างตาราง
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ข้อมูลบุคคล (
        ชื่อ TEXT,
        อายุ INTEGER,
        สาขา TEXT
    )
''')

# ฟังก์ชันสำหรับเพิ่มข้อมูล
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา):
    cursor.execute("INSERT INTO ข้อมูลบุคคล VALUES (?, ?, ?)", (ชื่อ, อายุ, สาขา))
    conn.commit()

# ฟังก์ชันสำหรับดึงข้อมูลทั้งหมด
def ดึงข้อมูล():
    cursor.execute("SELECT * FROM ข้อมูลบุคคล")
    return cursor.fetchall()

# Streamlit App
st.title('ข้อมูลบุคคล')

# เพิ่มข้อมูลในฟอร์ม
ชื่อ = st.text_input('ชื่อ:')
อายุ = st.number_input('อายุ:')
สาขา = st.text_input('สาขา:')
if st.button('เพิ่มข้อมูล'):
    เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)

# ปุ่มรีเซ็ตข้อมูล
if st.button('รีเซ็ตข้อมูล'):
    # เพิ่มคำสั่ง SQL สำหรับลบข้อมูลทั้งหมดในตาราง
    cursor.execute("DELETE FROM ข้อมูลบุคคล")
    conn.commit()
    st.warning('รีเซ็ตข้อมูลสำเร็จ!')

# แสดงข้อมูลทั้งหมด
ข้อมูลทั้งหมด = ดึงข้อมูล()
st.write('ข้อมูลทั้งหมด:')
for row in ข้อมูลทั้งหมด:
    st.write(f"ชื่อ: {row[0]}, อายุ: {row[1]}, สาขา: {row[2]}")

# ปิดการเชื่อมต่อกับฐานข้อมูล
cursor.close()
conn.close()

# เชื่อมโยงข้อมูลกับ Excel
df = pd.DataFrame(ข้อมูลทั้งหมด, columns=['ชื่อ', 'อายุ', 'สาขา'])
excel_file_path = 'ข้อมูลบุคคล.xlsx'
df.to_excel(excel_file_path, index=False)

#ฉบับแก้ไข
