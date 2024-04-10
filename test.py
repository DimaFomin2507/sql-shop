"""Задание."""

data = {
    "A": [("Саша", [2, 3]), ("Коля", [5])],
    "Б": [("Вова", [4, 5]), ("Женя", [3, 4, 5])],
}
best_group = None
best_average = 0

worst_student = None
worst_result = float("inf")

for group, students in data.items():
    total_scores = 0
    num_students = 0

    for student, scores in students:
        avg_score = sum(scores) / len(scores)
        total_scores += avg_score
        num_students += 1

        if avg_score < worst_result:
            worst_student = student
            worst_result = avg_score

    average_group_score = total_scores / num_students

    if average_group_score > best_average:
        best_group = group
        best_average = average_group_score

print(f"Группа {best_group} лучшая, в ней хуже всех {worst_student}")

# Вывести имя группы, c лучшим результатом
# (лучшая средняя оценка всех учеников)
# и имя худшего ученика в этой группе.
# -> Группа Б лучшая, в ней хуже всех Женя
