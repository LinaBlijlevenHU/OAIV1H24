import matplotlib.pyplot as plt

# [Name, ID, Attendance (%), Grade (%)]
students = [
    ['John Doe', 101, 85.5, 92.0],
    ['Jane Smith', 102, 78.0, 88.5],
    ['Alice Johnson', 103, 93.0, 95.0],
    ['Bob Brown', 104, 65.0, 70.0],
    ['Emily Davis', 105, 80.0, 82.5],
    ['Michael Wilson', 106, 72.5, 75.0],
    ['Sarah Lee', 107, 89.0, 91.5],
    ['David Green', 108, 95.0, 97.0],
    ['Laura White', 109, 70.5, 60.0],
    ['James Clark', 110, 88.0, 85.0]
]

# Isoleer de lijsten die we straks plotten
attendance = [student[2] for student in students]
grades = [student[3] for student in students]

# Maak wat schattingen op basis van een formule
schatting = [10 + 0.9*a for a in attendance]

# Maak een scatterplot
plt.scatter(
    x=attendance,
    y=grades,
    c="green"
)
# Plot ook de lijn voor de schatting
plt.plot(attendance, schatting, color="blue")

# Plot aankleding
plt.title("Student attendance vs. student grades")
plt.xlabel("Attendance (0-100)")
plt.ylabel("Grade (0-100)")

# Vergeet niet de figuur op te slaan of te laten zien
plt.savefig("scatterplot_voorbeeld.png")
plt.show()

