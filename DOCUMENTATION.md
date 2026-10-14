# Python Utility Module

## Overview

`utility_module.py` ek reusable Python module hai jisme validation, formatting, calculations aur file utilities ke functions diye gaye hain. Is project ka maqsad modular programming aur code reuse seekhna hai.

## Project Structure

| File | Description |
|------|-------------|
| `utility_module.py` | Main utility module |
| `main.py` | Example program jo module ko use karta hai |
| `DOCUMENTATION.md` | Har function ki documentation |

## How to Use

```python
import utility_module as util

print(util.is_valid_email("zaid@example.com"))
print(util.format_currency(2500))
```

Example program chalane ke liye:

```bash
python main.py
```

---

## 1. Validation Functions

### `is_valid_email(email)`
- **Purpose:** Email address ka format check karta hai.
- **Parameters:** `email` (str)
- **Returns:** `True` agar format sahi hai, warna `False`.
- **Example:** `is_valid_email("a@b.com")` -> `True`

### `is_valid_phone(phone)`
- **Purpose:** Pakistani mobile number check karta hai (`03XXXXXXXXX` ya `+923XXXXXXXXX`). Space aur dash ignore hote hain.
- **Parameters:** `phone` (str)
- **Returns:** `True` ya `False`.
- **Example:** `is_valid_phone("0300-1234567")` -> `True`

### `is_strong_password(password, min_length=8)`
- **Purpose:** Check karta hai ke password mein uppercase, lowercase, digit aur special character maujood hain aur length kam az kam `min_length` hai.
- **Parameters:** `password` (str), `min_length` (int, default 8)
- **Returns:** `True` ya `False`.
- **Example:** `is_strong_password("Python@2026")` -> `True`

### `is_positive_number(value)`
- **Purpose:** Check karta hai ke value int ya float hai aur zero se bari hai. Boolean ko number nahi maana jata.
- **Parameters:** `value` (any)
- **Returns:** `True` ya `False`.
- **Example:** `is_positive_number(10)` -> `True`

---

## 2. Formatting Functions

### `format_currency(amount, symbol="Rs.")`
- **Purpose:** Number ko commas aur 2 decimal places ke saath currency format mein badalta hai.
- **Parameters:** `amount` (int/float), `symbol` (str)
- **Returns:** Formatted string.
- **Example:** `format_currency(1250000.5)` -> `"Rs. 1,250,000.50"`

### `format_title(text)`
- **Purpose:** Har word ka pehla letter capital karta hai aur extra spaces hata deta hai.
- **Parameters:** `text` (str)
- **Returns:** Title-case string.
- **Example:** `format_title("python programming")` -> `"Python Programming"`

### `format_percentage(value, decimals=1)`
- **Purpose:** Number ko percentage string mein badalta hai.
- **Parameters:** `value` (int/float), `decimals` (int)
- **Returns:** String.
- **Example:** `format_percentage(86.456, 2)` -> `"86.46%"`

### `format_phone(phone)`
- **Purpose:** Phone number ko `03XX-XXXXXXX` format mein badalta hai. `+92` wale number ko bhi handle karta hai.
- **Parameters:** `phone` (str)
- **Returns:** Formatted string.
- **Raises:** `ValueError` agar digits 11 na hon.
- **Example:** `format_phone("+923001234567")` -> `"0300-1234567"`

### `truncate_text(text, max_length, suffix="...")`
- **Purpose:** Lamba text chhota karta hai aur end mein suffix lagata hai.
- **Parameters:** `text` (str), `max_length` (int), `suffix` (str)
- **Returns:** String jiski length `max_length` se zyada nahi hoti.
- **Raises:** `ValueError` agar `max_length` suffix se chhoti ho.

---

## 3. Calculation Functions

### `calculate_average(numbers)`
- **Purpose:** Numbers ki list ka average nikalta hai.
- **Parameters:** `numbers` (list)
- **Returns:** float
- **Raises:** `ValueError` agar list khali ho.
- **Example:** `calculate_average([80, 90, 100])` -> `90.0`

### `calculate_percentage(part, whole)`
- **Purpose:** `part`, `whole` ka kitna percent hai wo batata hai.
- **Parameters:** `part` (number), `whole` (number)
- **Returns:** float
- **Raises:** `ZeroDivisionError` agar `whole` zero ho.
- **Example:** `calculate_percentage(430, 500)` -> `86.0`

### `calculate_discount(price, discount_percent)`
- **Purpose:** Discount ke baad ki price batata hai.
- **Parameters:** `price` (number), `discount_percent` (0 se 100 tak)
- **Returns:** Final price.
- **Raises:** `ValueError` agar discount range se bahar ho.
- **Example:** `calculate_discount(5000, 15)` -> `4250.0`

### `calculate_compound_interest(principal, rate, years, times_per_year=1)`
- **Purpose:** Compound interest ke baad ki total amount nikalta hai.
- **Parameters:** `principal` (number), `rate` (annual percent), `years` (number), `times_per_year` (int)
- **Returns:** Total amount, 2 decimals tak round ki hui.
- **Raises:** `ValueError` agar koi value negative ya `times_per_year` zero ho.

### `calculate_bmi(weight_kg, height_m)`
- **Purpose:** Body Mass Index nikalta hai.
- **Parameters:** `weight_kg` (number), `height_m` (number)
- **Returns:** BMI, 2 decimals tak.
- **Raises:** `ValueError` agar weight ya height positive na ho.
- **Example:** `calculate_bmi(70, 1.75)` -> `22.86`

---

## 4. File Utility Functions

### `file_exists(path)`
- **Purpose:** Check karta hai ke file maujood hai ya nahi.
- **Returns:** `True` ya `False`.

### `get_file_size(path)`
- **Purpose:** File ka size bytes mein batata hai.
- **Returns:** int
- **Raises:** `FileNotFoundError` agar file na mile.

### `read_text_file(path)`
- **Purpose:** Text file ka poora content parhta hai (UTF-8).
- **Returns:** String.

### `write_text_file(path, content)`
- **Purpose:** File mein content likhta hai. Purana content replace ho jata hai.

### `append_text_file(path, content)`
- **Purpose:** File ke end mein content add karta hai.

### `read_json_file(path)`
- **Purpose:** JSON file ko Python dictionary ya list mein load karta hai.
- **Returns:** dict ya list.

### `write_json_file(path, data)`
- **Purpose:** Python data ko indent ke saath JSON file mein save karta hai.

### `list_files_with_extension(folder, extension)`
- **Purpose:** Folder mein diye gaye extension wali files ki sorted list deta hai. Extension `"txt"` ya `".txt"` dono chalte hain.
- **Returns:** List of file names.
- **Raises:** `NotADirectoryError` agar folder na mile.

---

## Design Notes

- Har function sirf ek kaam karta hai (single responsibility).
- Function names descriptive hain.
- Koi global variable use nahi hua.
- Galat input par clear exceptions raise hote hain.

## Interview Questions

**What is a Python module?**
Ek `.py` file jisme functions, classes aur variables hote hain aur jise `import` karke dusri files mein use kiya ja sakta hai.

**What is the difference between a module and a package?**
Module ek single `.py` file hoti hai. Package modules ka folder hota hai jisme aam taur par `__init__.py` file hoti hai.

**Why is code reusability important?**
Isse duplicate code kam hota hai, bugs fix karna asaan hota hai, maintenance sasti hoti hai aur development tez hoti hai.
