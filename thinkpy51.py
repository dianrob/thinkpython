import time

epoch = time.time()

seconds_a_day = 24 * 60 * 60

seconds_an_hour = 60 * 60

seconds_a_minute = 60

days_past = epoch // seconds_a_day

hour_today = int((epoch % seconds_a_day) // seconds_an_hour + 2)

minute_today = int((epoch % seconds_a_day) % seconds_an_hour // seconds_a_minute)

seconds_today = int((epoch % seconds_a_day) % seconds_an_hour % seconds_a_minute)

print(f"{hour_today}:{minute_today}:{seconds_today}")


