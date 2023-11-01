# Подумать ещё
# Решение не укладывается по времени при длине строки в 100 000 символов

def get_max_length(seq1, seq2):
    seq1_points_and_their_indices = {}
    for index, value in enumerate(seq1):
        if value in seq1_points_and_their_indices:
            seq1_points_and_their_indices[value].append(index)
        else:
            seq1_points_and_their_indices[value] = [index]

    counter, max_len = 0, 0
    indices_of_prev = []
    for seq2_value in seq2:
        if seq2_value not in seq1_points_and_their_indices:
            counter = 0
            indices_of_prev = []
            continue
        if not indices_of_prev:
            counter = 1
            indices_of_prev = seq1_points_and_their_indices[seq2_value]
        else:
            indices_of_cur = seq1_points_and_their_indices[seq2_value]
            indices_of_prev = list(filter(lambda i: i-1 in indices_of_prev,
                                   indices_of_cur))
            if indices_of_prev:
                counter += 1
            else:
                counter = 1
                indices_of_prev = seq1_points_and_their_indices[seq2_value]

        if max_len < counter:
            max_len = counter
        if max_len > (len(seq2) - 1 - seq2_value) and counter == 0:
            break

    return max_len


if __name__ == '__main__':
    n = int(input())
    first_team_points = list(map(int, input().split()))
    m = int(input())
    second_team_points = list(map(int, input().split()))
    print(get_max_length(first_team_points, second_team_points))
