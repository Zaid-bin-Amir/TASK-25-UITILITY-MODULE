import os
import tempfile

import utility_module as util


def run_validation_demo():
    print("=== Validation ===")
    print("Email valid:", util.is_valid_email("zaid@example.com"))
    print("Email invalid:", util.is_valid_email("zaid@@example"))
    print("Phone valid:", util.is_valid_phone("0300-1234567"))
    print("Strong password:", util.is_strong_password("Python@2026"))
    print("Weak password:", util.is_strong_password("python"))
    print("Positive number:", util.is_positive_number(25))


def run_formatting_demo():
    print("\n=== Formatting ===")
    print(util.format_currency(1250000.5))
    print(util.format_title("python programming track"))
    print(util.format_percentage(86.456, 2))
    print(util.format_phone("+923001234567"))
    print(util.truncate_text("Modular programming makes code reusable", 25))


def run_calculation_demo():
    print("\n=== Calculations ===")
    marks = [78, 85, 92, 66, 88]
    print("Average marks:", util.calculate_average(marks))
    print("Percentage:", util.calculate_percentage(430, 500))
    print("Price after discount:", util.calculate_discount(5000, 15))
    print("Compound interest:", util.calculate_compound_interest(100000, 8, 5, 4))
    print("BMI:", util.calculate_bmi(70, 1.75))


def run_file_demo():
    print("\n=== File Utilities ===")
    with tempfile.TemporaryDirectory() as folder:
        notes_path = os.path.join(folder, "notes.txt")
        data_path = os.path.join(folder, "student.json")

        util.write_text_file(notes_path, "Line one\n")
        util.append_text_file(notes_path, "Line two\n")
        print("Text file content:")
        print(util.read_text_file(notes_path))

        student = {"name": "Zaid", "track": "Python", "score": 92}
        util.write_json_file(data_path, student)
        print("JSON data:", util.read_json_file(data_path))

        print("File exists:", util.file_exists(notes_path))
        print("File size (bytes):", util.get_file_size(notes_path))
        print("Text files:", util.list_files_with_extension(folder, "txt"))


def main():
    run_validation_demo()
    run_formatting_demo()
    run_calculation_demo()
    run_file_demo()


if __name__ == "__main__":
    main()
