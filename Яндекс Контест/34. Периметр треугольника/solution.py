def get_max_perimeter(segments_qty, lengths):
    lengths.sort(reverse=True)
    for segment in range(segments_qty):
        if lengths[segment] < lengths[segment+1] + lengths[segment+2]:
            return lengths[segment] + lengths[segment+1] + lengths[segment+2]
        else:
            segment += 1


if __name__ == '__main__':
    segments_qty = int(input())
    lengths = list(map(int, input().split()))
    print(get_max_perimeter(segments_qty, lengths))
