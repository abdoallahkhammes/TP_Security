import re
import math


def calculate_entropy(password: str) -> float:

    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'\d', password):
        charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset_size += 33

    if charset_size == 0 or len(password) == 0:
        return 0.0

    return len(password) * math.log2(charset_size)


def check_strength(password: str) -> str:
    """ترجع 'قوية' أو 'ضعيفة'"""

    length = len(password)
    entropy_value = calculate_entropy(password)

    # التحقق من وجود أنواع مختلفة من الحروف
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[^a-zA-Z0-9]', password))

    diversity_count = sum([has_lower, has_upper, has_digit, has_special])

    # شروط القوة
    is_strong = (
            length >= 8 and  # الطول 8 على الأقل
            entropy_value >= 40 and  # الإنتروبي 40 بت على الأقل
            diversity_count >= 3  # 3 أنواع مختلفة من الحروف على الأقل
    )

    if is_strong:
        return "قوية"
    else:
        return " ضعيفة"



if __name__ == "__main__":
    print("=" * 40)
    print("  فحص قوة كلمة المرور")
    print("=" * 40)

    password = input("\nأدخل كلمة المرور: ")

    result = check_strength(password)

    print("\n" + "=" * 40)
    print(f"النتيجة: {result}")
    print("=" * 40)