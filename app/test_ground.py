import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 27],
    'Occupation': ['Engineer', 'Teacher', 'Doctor', 'Artist']
}
df = pd.DataFrame(data)
print(df)
