import random
from .models import Department, Student, StudentID
from faker import Faker
import traceback

fake = Faker()

def seed_db(n=10) -> None:
    """
    Seeds the database with `n` random students, assigning them to random departments.
    """
    try:
        departments_objs = Department.objects.all()
        
        # Check if departments are available
        if not departments_objs.exists():
            print("No departments available to assign students.")
            return

        for _ in range(n):
            # Pick a random department
            random_index = random.randint(0, len(departments_objs) - 1)
            department = departments_objs[random_index]

            # Generate random student data
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            # Create student ID object
            student_id_obj = StudentID.objects.create(student_id=student_id)

            # Create student object
            student_obj = Student.objects.create(
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )
            print(f"Student {student_name} created successfully.")

    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
