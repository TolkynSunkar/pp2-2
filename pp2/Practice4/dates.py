from datetime import datetime, date, timedelta

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None


def main():
    print("=== 1) Current date/time ===")
    now = datetime.now()
    today = date.today()
    print("Now:", now)
    print("Today:", today)
    print()

    print("=== 2) Create specific datetime ===")
    custom = datetime(2026, 2, 26, 8, 0, 0)
    print("Custom datetime:", custom)
    print()

    print("=== 3) Formatting ===")
    print("ISO format:", now.isoformat(timespec="seconds"))
    print("Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))
    print()

    print("=== 4) Parse from string ===")
    date_string = "26-02-2026 08:15:30"
    parsed = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
    print("Original string:", date_string)
    print("Parsed datetime:", parsed)
    print()

    print("=== 5) Date arithmetic ===")
    future = now + timedelta(days=7, hours=3)
    difference = future - now
    print("Future time:", future)
    print("Difference:", difference)
    print("Days:", difference.days)
    print("Seconds:", difference.seconds)
    print()

    print("=== 6) Timezones (optional) ===")
    if ZoneInfo is not None:
        try:
            almaty = datetime.now(ZoneInfo("Asia/Almaty"))
            utc = datetime.now(ZoneInfo("UTC"))
            print("Almaty time:", almaty.strftime("%Y-%m-%d %H:%M:%S %Z"))
            print("UTC time:", utc.strftime("%Y-%m-%d %H:%M:%S %Z"))
        except Exception as e:
            print("Timezone data not available:", e)
    else:
        print("zoneinfo module not available.")
    print()


if __name__ == "__main__":
    main()