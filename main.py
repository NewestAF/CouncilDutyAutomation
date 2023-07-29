import random

import pandas as pd
import numpy as np
import sqlite3 as sql

file = open("studentList.txt", "rt", encoding='UTF8')
studentList = file.readline().strip().split(", ")

print(studentList)

studentList1 = []
studentList2 = []

for i in range(0, 5):
    student = random.choice(studentList)
    studentList1.append(student)
    studentList.remove(student)

for i in range(0, 5):
    student = random.choice(studentList)
    studentList2.append(student)
    studentList.remove(student)

studentArray = np.array([studentList1, studentList2])

dataFrame = pd.DataFrame(data=studentArray, columns=['월요일', '화요일', '수요일', '목요일', '금요일'], index=['점심', '흡연'])

connection = sql.connect("student.db")

connection.execute("DROP TABLE IF EXISTS studentTest")

connection.execute("CREATE TABLE IF NOT EXISTS studentTest (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, "
                   "day TEXT, type TEXT)")

for i in range(0, 2):
    for j in range(0, 5):
        weekDay = ""
        match j:
            case 0:
                weekDay = "월요일"
            case 1:
                weekDay = "화요일"
            case 2:
                weekDay = "수요일"
            case 3:
                weekDay = "목요일"
            case 4:
                weekDay = "금요일"
        if i == 0:
            connection.execute(
                "INSERT INTO studentTest (name, day, type) VALUES (?, ?, ?)", (dataFrame.iloc[i, j], weekDay, "점심"))
            print(dataFrame.iloc[i, j], weekDay, "점심")
        else:
            connection.execute(
                "INSERT INTO studentTest (name, day, type) VALUES (?, ?, ?)", (dataFrame.iloc[i, j], weekDay, "흡연"))
            print(dataFrame.iloc[i, j], weekDay, "흡연")

connection.commit()

print(dataFrame)
