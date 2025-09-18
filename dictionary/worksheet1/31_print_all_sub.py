students = {
    'Rahul': {'age': 16, 'marks': {'math': 90, 'english': 88}},
    'Simran': {'age': 15, 'marks': {'math': 95, 'english': 92}}
}

for name, info in students.items():
    print(f"Student: {name}")
    marks = info['marks']
    for subject, score in marks.items():
        print(f"  {subject}: {score}")

   

