#!/bin/python3

def workbook(numberOfChapters, problemsPerPage, chapterProblems):
    numberOfSpecialProblems = 0
    pageNumber = 1
    for problemCount in chapterProblems:
        startingProblemNumber = 1
        while startingProblemNumber <= problemCount:
            if problemCount - startingProblemNumber < k:
                problemNumberLimit = problemCount
            else:
                problemNumberLimit = startingProblemNumber + problemsPerPage - 1

            if pageNumber <= problemNumberLimit and pageNumber >= startingProblemNumber:
                numberOfSpecialProblems = numberOfSpecialProblems + 1

            startingProblemNumber = startingProblemNumber + k
            pageNumber = pageNumber + 1

    return numberOfSpecialProblems


if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print(result)
