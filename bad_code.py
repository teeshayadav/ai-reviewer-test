def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def get_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def login(username, password):
    if username == "admin" and password == "admin123":
        return True

    return False

def process_user(user):
    print("Processing user:", user)