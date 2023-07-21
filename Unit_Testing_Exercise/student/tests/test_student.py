from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("TestGuy1")
        self.student_with_course = Student("TestGuy2", {"math": ["some note"]})

    def test_correct_initialization(self):
        self.assertEqual("TestGuy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["some note"]}, self.student_with_course.courses)

    def test_enroll_and_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll("math", ["math is kinda fun", "just geometry tho"])

        self.assertEqual(
            ["some note", "math is kinda fun", "just geometry tho"],
            self.student_with_course.courses["math"]
        )
        self.assertEqual(
            "Course already added. Notes have been updated.",
            result
        )

    def test_enroll_and_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll("python db", ["python db is cool"])

        self.assertEqual(["python db is cool"], self.student.courses["python db"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_notes_to_non_existing_course_with_third_param_Y(self):
        result = self.student.enroll("python db", ["python db is cool"], "Y")

        self.assertEqual(["python db is cool"], self.student.courses["python db"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_and_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll("python db", ["python db is cool"], "n")

        self.assertEqual([], self.student.courses["python db"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("math", "x + y = z")

        self.assertEqual(
            ["some note", "x + y = z"],
            self.student_with_course.courses["math"]
        )
        self.assertEqual(
            "Notes have been updated",
            result
        )

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("python", "python is cool")

        self.assertEqual(
            "Cannot add notes. Course not found.",
            str(ex.exception)
        )

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")

        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")

        self.assertEqual(
            "Cannot remove course. Course not found.",
            str(ex.exception)
        )


if __name__ == "__main__":
    main()