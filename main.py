from datetime import date, timedelta

def generate_next_7_dates():
    today = date.today()
    return [today + timedelta(days=i) for i in range(7)]

def same_day_and_month(date1, date2):
    return date1.day == date2.day and date1.month == date2.month

def get_birthdays_per_week(users):
    birthdays_next_week = {}
    dates_list = generate_next_7_dates()

    for user in users:
        for d in dates_list:
            if same_day_and_month(user['birthday'], d):
                weekday_name = d.strftime('%A')
                
                if weekday_name in ['Saturday', 'Sunday']:
                    weekday_name = 'Monday'

                if weekday_name not in birthdays_next_week:
                    birthdays_next_week[weekday_name] = []
                
                birthdays_next_week[weekday_name].append(user['name'])

    return birthdays_next_week


if __name__ == "__main__":
    users = [
            {
                "name": "John",
                "birthday": (date.today() + timedelta(days=1)),
            },
            {
                "name": "Doe",
                "birthday": (date.today() + timedelta(days=3)),
            },
            {"name": "Alice", "birthday": (date.today() + timedelta(days=-3))},
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")