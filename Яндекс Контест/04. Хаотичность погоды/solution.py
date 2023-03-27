from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1
    result = []
    if temperatures[0] > temperatures[1]:
        result.append(temperatures[0])
    if temperatures[-1] > temperatures[-2]:
        result.append(temperatures[-1])
    for i in range(1, len(temperatures)-1):
        if (
            temperatures[i] > temperatures[i-1]
            and temperatures[i] > temperatures[i+1]
        ):
            result.append(temperatures[i])
    return len(result)


if __name__ == '__main__':
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    print(get_weather_randomness(temperatures))
