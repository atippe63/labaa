import streamlit as st
import sqlite3
import pandas as pd
import os

# Connect to SQLite database
conn = sqlite3.connect('ข้อมูลบุคคล')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ข้อมูลบุคคล (
        ชื่อ TEXT,
        อายุ INTEGER,
        สาขา TEXT
    )
''')

# Function to add data
def เพิ่มข้อมูล(ชื่อ, อายุ, สาขา):
    cursor.execute("INSERT INTO ข้อมูลบุคคล VALUES (?, ?, ?)", (ชื่อ, อายุ, สาขา))
    conn.commit()

# Function to fetch all data
def ดึงข้อมูล():
    cursor.execute("SELECT * FROM ข้อมูลบุคคล")
    return cursor.fetchall()

# Streamlit App
st.title('ข้อมูลบุคคล')

# List to store names
names_list = []

# Add data in the form
ชื่อ = st.text_input('ชื่อ:')
อายุ = st.number_input('อายุ:')
สาขา = st.text_input('สาขา:')
if st.button('เพิ่มข้อมูล'):
    เพิ่มข้อมูล(ชื่อ, อายุ, สาขา)
    names_list.append(ชื่อ)  # Update the list of names

# Reset data button
if st.button('รีเซ็ตข้อมูล'):
    cursor.execute("DELETE FROM ข้อมูลบุคคล")
    conn.commit()
    st.warning('รีเซ็ตข้อมูลสำเร็จ!')
    names_list = []  # Reset the list of names

# Display all data
ข้อมูลทั้งหมด = ดึงข้อมูล()
st.write('ข้อมูลทั้งหมด:')
for row in ข้อมูลทั้งหมด:
    st.write(f"ชื่อ: {row[0]}, อายุ: {row[1]}, สาขา: {row[2]}")

# Display list of names
st.write('รายชื่อ:')
st.write(names_list)

# Close the database connection
cursor.close()
conn.close()
