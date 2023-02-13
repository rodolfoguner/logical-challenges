SERVICE_TIME_START_IN_MINUTES = 420
CONSULTATION_TIME = 30


class Patient:

    def __init__(self, arrive: int, critical: int):
        self.__arrive = arrive
        self.__critical = arrive + critical

    def patient_limit_reached(self, service_time: int) -> bool:
        return service_time > self.__critical


def transform_arrive_to_minutes(hour: int, minutes: int) -> int:
    return (hour * 60) + minutes


def main() -> None:

    service_time: int
    patients_critical_reached: int

    while True:

        service_time = SERVICE_TIME_START_IN_MINUTES
        patients_critical_reached = 0

        try:
            patients: int = int(input())

            if patients <= 0 or patients > 25:
                break

            for _ in range(patients):

                arrived_hours, arrived_minutes, critical = [int(time) for time in input().split()]

                arrived_time_in_minutes = transform_arrive_to_minutes(arrived_hours, arrived_minutes)

                while service_time < arrived_time_in_minutes:
                    service_time += CONSULTATION_TIME

                patient = Patient(arrived_time_in_minutes, critical)

                if patient.patient_limit_reached(service_time):
                    patients_critical_reached += 1

                service_time += CONSULTATION_TIME

            print(patients_critical_reached)

        except EOFError:
            break


if __name__ == '__main__':
    main()
