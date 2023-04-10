def solution(sequence, k):
    length = len(sequence)
    startIndex, endIndex, resultLength, summation = 0, 0, float("inf"), sequence[0]

    if summation == k:
        return [0, 0]

    result = None

    while startIndex < length and endIndex < length and startIndex <= endIndex:
        if summation == k:
            if resultLength > (endIndex - startIndex + 1):
                result = [startIndex, endIndex]
                resultLength = endIndex - startIndex + 1

            endIndex += 1
            if endIndex < length:
                summation += sequence[endIndex]
        elif summation < k:
            endIndex += 1
            if endIndex < length:
                summation += sequence[endIndex]
        elif summation > k:
            summation -= sequence[startIndex]
            startIndex += 1

    return result


print(solution([1, 2, 3, 4, 5], 7))
