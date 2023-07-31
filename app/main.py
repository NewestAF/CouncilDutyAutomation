# import random
#
# import pandas as pd
# import numpy as np
# import sqlite3 as sql
#
# from app import db
# import models
#
# file = open("studentList.txt", "rt", encoding='UTF8')
# studentList = file.readline().strip().split(", ")
#
# print(studentList)
#
# studentList1 = []
# studentList2 = []
#
# for i in range(0, 5):
#     student = random.choice(studentList)
#     studentList1.append(student)
#     studentList.remove(student)
#
# for i in range(0, 5):
#     student = random.choice(studentList)
#     studentList2.append(student)
#     studentList.remove(student)
#
# studentArray = np.array([studentList1, studentList2])
#
# dataFrame = pd.DataFrame(data=studentArray, columns=['월요일', '화요일', '수요일', '목요일', '금요일'], index=['점심', '흡연'])
#
# connection = sql.connect("student.db")
# dataFrame.to_sql("student", connection, if_exists="replace")
#
# connection.close()
#
# for i in range(0, 2):
#     for j in range(0, 5):
#         if i == 0:
#             pt = models.PatrolStudent(name=dataFrame.iloc[i, j], day=j, type="점심")
#             db.session.add(pt)
#             print(dataFrame.iloc[i, j], j, "점심")
#         else:
#             pt = models.PatrolStudent(name=dataFrame.iloc[i, j], day=j, type="흡연")
#             db.session.add(pt)
#             print(dataFrame.iloc[i, j], j, "흡연")
#
# db.session.commit()
#
# print(dataFrame)
