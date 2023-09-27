activities = {}


def check_activity(activity):
    if activity not in activities:
        activities[activity] = True
        print(activity)


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        check_activity(input())
