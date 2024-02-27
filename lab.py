import sqlite3
import streamlit as st
import pandas as pd

# Function to create table if not exists
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

# Function to add data
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา):
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ข้อมูลบุคคล VALUES (?, ?, ?)", (ชื่อ, อายุ, สาขา))
    conn.commit()
    conn.close()

# Function to fetch all data as Pandas DataFrame
def ดึงข้อมูล():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    df = pd.read_sql_query("SELECT * FROM ข้อมูลบุคคล", conn)
    conn.close()
    return df

# Function to delete all data
def ลบข้อมูลทั้งหมด():
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ข้อมูลบุคคล")
    conn.commit()
    conn.close()

# Function to delete specific row
def ลบข้อมูลตามชื่อ(ชื่อ):
    conn = sqlite3.connect('ข้อมูลบุคคล.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ข้อมูลบุคคล WHERE ชื่อ=?", (ชื่อ,))
    conn.commit()
    conn.close()

# Streamlit App
st.title('ข้อมูลบุคคล')

# Create table if not exists
create_table()

# Show form to add data
ชื่อ = st.text_input('ชื่อ:')
อายุ = st.number_input('อายุ:')
สาขา = st.text_input('สาขา:')
if st.button('เพิ่มข้อมูล'):
    เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)

# Display all data using Pandas DataFrame
ข้อมูลทั้งหมด = ดึงข้อมูล()
st.write('ข้อมูลทั้งหมด:')
st.write(ข้อมูลทั้งหมด)

# Button to delete specific row
if st.button('ลบข้อมูลตามชื่อ', key='delete_by_name'):
    # Assume the owner's username is 'admin'
    if st.text_input('กรุณากรอกชื่อผู้ใช้ (admin เท่านั้น):') == 'atip':
        ลบข้อมูลตามชื่อ(ชื่อ, อายุ, สาขา)
        st.warning('ลบข้อมูลสำเร็จ!')
    else:
        st.warning('ชื่อผู้ใช้ไม่ถูกต้อง')
