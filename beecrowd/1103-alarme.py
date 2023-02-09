TOTAL_MINUTES_DAY = 1_440

def get_total_minutes_to_sleep(first_interval: int, second_interval:int) -> int:
    return second_interval - first_interval

def add_one_day(minutes: int) -> int:
    return minutes + TOTAL_MINUTES_DAY


def get_total_minutes(hours: int, minutes: int) -> int:
    return (hours * 60) + minutes


def main() -> None:
    
    while True:
        
        first_hour, first_minute, second_hour, second_minute = [int(x) for x in input().split()]
        
        if not (first_hour or first_minute or second_hour or second_minute):
            break
        
        first_interval: int = get_total_minutes(first_hour, first_minute)
        second_interval: int = get_total_minutes(second_hour, second_minute)

        if second_interval < first_interval:
            second_interval = add_one_day(second_interval)
        
        print(get_total_minutes_to_sleep(first_interval, second_interval))

if __name__ == '__main__':
    main()
