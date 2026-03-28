def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine



book_title = input()
days_overdue = int(input())


try:
    daily_rate = float(input())
    try:
        max_fine = float(input())
        fine = calculate_fine(book_title, days_overdue, daily_rate, max_fine)
    except:
        fine = calculate_fine(book_title, days_overdue, daily_rate)
except:
    fine = calculate_fine(book_title, days_overdue)



print(f"Book: {book_title}")
print(f"Days overdue: {days_overdue}")
print(f"Fine: Rs. {fine}")


if fine == 150.0 or ('max_fine' in locals() and fine == max_fine):
    print(f"You have accumulated the maximum fine of INR: {fine}")
