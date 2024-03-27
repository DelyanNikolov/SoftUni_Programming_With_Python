from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Adam")
        self.student2 = Student("Bobby", {"python": ["recursion", "function", "OOP"]})

    def test_correct_init(self):
        self.assertEqual("Adam", self.student.name)
        self.assertEqual({}, self.student.courses)

        self.assertEqual("Bobby", self.student2.name)
        self.assertEqual({"python": ["recursion", "function", "OOP"]}, self.student2.courses)

    def test_enroll_with_existing_course_expect_msg(self):
        expected_notes = ["recursion", "function", "OOP", "new note"]
        expected_msg = "Course already added. Notes have been updated."
        result = self.student2.enroll("python", ["new note"])
        self.assertEqual(expected_msg, result)
        self.assertEqual(expected_notes, self.student2.courses["python"])

    def test_enroll_with_non_existing_course_without_third_param(self):
        expected_msg = "Course and course notes have been added."
        result = self.student.enroll("math", ["x + 2 = 6"])
        self.assertEqual(expected_msg, result)

        self.assertEqual({"math": ["x + 2 = 6"]}, self.student.courses)

    def test_enroll_with_non_existing_course_and_Y_for_add_course_notes_expected_msg(self):
        expected_msg = "Course and course notes have been added."
        result = self.student.enroll("python", ["unit testing is hard"], "Y")
        self.assertEqual(expected_msg, result)

        self.assertEqual({"python": ["unit testing is hard"]}, self.student.courses)

    def test_enroll_with_non_existing_course_and_N_for_add_course_notes_expected_msg_and_not_added_notes(self):
        expected_msg = "Course has been added."
        result = self.student.enroll("python", ["unit testing is hard"], "N")
        self.assertEqual(expected_msg, result)

        self.assertEqual({"python": []}, self.student.courses)


    def test_add_notes_with_existing_course_expect_note_added_return_msg(self):
        expected_msg = "Notes have been updated"
        expected_notes = ["recursion", "function", "OOP", "few notes"]
        result = self.student2.add_notes("python", "few notes")
        self.assertEqual(expected_msg, result)
        self.assertEqual(expected_notes, self.student2.courses["python"])

    def test_add_notes_with_non_existing_course_expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("python", "few notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course_expect_remove_course_and_msg(self):
        expected_msg = "Course has been removed"
        result = self.student2.leave_course("python")
        self.assertEqual(expected_msg, result)
        self.assertEqual({}, self.student2.courses)

    def test_leave_course_with_non_existing_course_expect_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
