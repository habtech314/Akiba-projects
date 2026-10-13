"""
Task 02: Student ID Card
Akiba Technologies Software Engineering Bootcamp - Week 1

Demonstrates:
- String and integer data types
- Preserving leading zeros in identifiers/phone numbers (stored as str, not int)
- Dynamic box border formatting using Python f-string alignment
- PEP 8 snake_case conventions
"""


def main() -> None:
    # 1. Collect student credentials
    student_name = input("Name: ")
    student_id = input("ID: ")
    department = input("Department: ")
    year = int(input("Year: "))
    university = input("University: ")
    # Keep as str to protect leading zeros (e.g., 0912345678)
    phone_number = input("Phone number: ")

    # 2. Formatted ID Card Layout
    card_width = 44
    border = "+" + "-" * (card_width - 2) + "+"

    print(f"\n{border}")
    print(f"|{'AKIBA STUDENT CARD':^{card_width - 2}}|")
    print(border)
    print(f"| Name: {student_name:<{card_width - 10}}|")
    print(f"| ID: {student_id:<{card_width - 8}}|")
    print(f"| Department: {department:<{card_width - 16}}|")
    print(f"| Year: {year:<{card_width - 10}}|")
    print(f"| University: {university:<{card_width - 16}}|")
    print(f"| Phone: {phone_number:<{card_width - 11}}|")
    print(f"{border}\n")


if __name__ == "__main__":
    main()
