import sqlite3
import streamlit as st

conn = sqlite3.connect('ข้อมูลบุคคล.db')
cursor = conn.cursor()
property
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ข้อมูลบุคคล (
        ชื่อ TEXT,
        อายุ INTEGER,
        สาขา TEXT
    )
''')

# ฟังก์ชันเพิ่มข้อมูลและดึงข้อมูล
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา):
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ข้อมูลบุคคล VALUES (?, ?, ?)", (ชื่อ, อายุ, สาขา))
    conn.commit()
    conn.close()

def ดึงข้อมูล():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ข้อมูลบุคคล")
    data = cursor.fetchall()
    conn.close()
    return data

# Streamlit App
st.title('ข้อมูลบุคคล')

# แสดงฟอร์มเพื่อเพิ่มข้อมูล
ชื่อ = st.text_input('ชื่อ:')
อายุ = st.number_input('อายุ:')
สาขา = st.text_input('สาขา:')
if st.button('เพิ่มข้อมูล'):
    เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)

# แสดงข้อมูลทั้งหมด
ข้อมูลทั้งหมด = ดึงข้อมูล()
st.write('ข้อมูลทั้งหมด:')
for row in ข้อมูลทั้งหมด:
    st.write(f"ชื่อ: {row[0]}, อายุ: {row[1]}, สาขา: {row[2]}")

conn.commit()
conn.close()