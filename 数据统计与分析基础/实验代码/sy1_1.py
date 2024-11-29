class Student:
    def __init__(self, name, age, birth_year, stats_grade):
        self.name = name
        self.age = age
        self.birth_year = birth_year
        self.stats_grade = stats_grade


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, birth_year, stats_grade):
        self.students.append(Student(name, age, birth_year, stats_grade))

    def calculate_averages(self, n):
        if n > len(self.students) or n <= 0:
            raise ValueError("n must be between 1 and the number of students.")
        selected_students = self.students[:n]
        avg_age = sum(student.age for student in selected_students) / n
        avg_stats_grade = sum(student.stats_grade for student in selected_students) / n
        return avg_age, avg_stats_grade


# 示例程序
if __name__ == "__main__":
    # 创建学生记录
    records = StudentRecords()
    # 添加10名学生
    records.add_student("Alice", 20, 2003, 85)
    records.add_student("Bob", 21, 2002, 90)
    records.add_student("Charlie", 22, 2001, 88)
    records.add_student("Daisy", 20, 2003, 92)
    records.add_student("Edward", 23, 2000, 75)
    records.add_student("Fiona", 19, 2004, 95)
    records.add_student("George", 21, 2002, 87)
    records.add_student("Helen", 20, 2003, 80)
    records.add_student("Ian", 22, 2001, 78)
    records.add_student("Jack", 19, 2004, 85)

    # 输入前n个学生
    try:
        n = int(input("请输入要统计的学生人数 (n): "))
        avg_age, avg_stats_grade = records.calculate_averages(n)
        print(f"前 {n} 名学生的年龄平均值: {avg_age:.2f}")
        print(f"前 {n} 名学生的数据统计分析课程实验成绩平均值: {avg_stats_grade:.2f}")
    except ValueError as e:
        print(f"输入错误: {e}")
