#!/bin/python3

import sys

def designerPdfViewer(h, word):
    maxHeight = 0
    for x in word :
        height = h[ord(x) - 97]
        if height > maxHeight :
            maxHeight = height
    return maxHeight * len(word)

if __name__ == "__main__" :
    h = list(map(int, input().strip().split()))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)
