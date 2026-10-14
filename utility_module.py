import json
import os
import re


def is_valid_email(email):
    if not isinstance(email, str):
        return False
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email.strip()) is not None


def is_valid_phone(phone):
    if not isinstance(phone, str):
        return False
    cleaned = re.sub(r"[\s-]", "", phone)
    pattern = r"^(\+92|0)3\d{9}$"
    return re.match(pattern, cleaned) is not None


def is_strong_password(password, min_length=8):
    if not isinstance(password, str) or len(password) < min_length:
        return False
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)
    return has_upper and has_lower and has_digit and has_special


def is_positive_number(value):
    if isinstance(value, bool):
        return False
    return isinstance(value, (int, float)) and value > 0


def format_currency(amount, symbol="Rs."):
    return f"{symbol} {amount:,.2f}"


def format_title(text):
    return " ".join(word.capitalize() for word in text.strip().split())


def format_percentage(value, decimals=1):
    return f"{value:.{decimals}f}%"


def format_phone(phone):
    digits = re.sub(r"\D", "", phone)
    if digits.startswith("92") and len(digits) == 12:
        digits = "0" + digits[2:]
    if len(digits) != 11:
        raise ValueError("Phone number must have 11 digits")
    return f"{digits[:4]}-{digits[4:]}"


def truncate_text(text, max_length, suffix="..."):
    if max_length < len(suffix):
        raise ValueError("max_length is smaller than the suffix")
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list")
    return sum(numbers) / len(numbers)


def calculate_percentage(part, whole):
    if whole == 0:
        raise ZeroDivisionError("Whole value cannot be zero")
    return (part / whole) * 100


def calculate_discount(price, discount_percent):
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount_percent / 100)


def calculate_compound_interest(principal, rate, years, times_per_year=1):
    if principal < 0 or rate < 0 or years < 0 or times_per_year <= 0:
        raise ValueError("Invalid values for compound interest")
    amount = principal * (1 + rate / (100 * times_per_year)) ** (times_per_year * years)
    return round(amount, 2)


def calculate_bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive")
    return round(weight_kg / (height_m ** 2), 2)


def file_exists(path):
    return os.path.isfile(path)


def get_file_size(path):
    if not file_exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return os.path.getsize(path)


def read_text_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_text_file(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def append_text_file(path, content):
    with open(path, "a", encoding="utf-8") as file:
        file.write(content)


def read_json_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json_file(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def list_files_with_extension(folder, extension):
    if not os.path.isdir(folder):
        raise NotADirectoryError(f"Folder not found: {folder}")
    if not extension.startswith("."):
        extension = "." + extension
    return sorted(
        name for name in os.listdir(folder)
        if name.lower().endswith(extension.lower())
    )
