# Make a function that computes the minimum of a list
# in O(n^2) time
# 
# Exercise link:
# https://runestone.academy/runestone/books/published/pythonds/AlgorithmAnalysis/BigONotation.html


def find_min1(list):
    counter = 1
    min_nim = None
    for item in list:
        for second_item in list:
            if counter == 1:
                if item < second_item:
                    min_nim = item
                    counter += 1
                else:
                    min_nim = second_item
                    counter += 1
            else:
                if item < second_item and item < min_nim:
                    min_nim = item
                    counter += 1
                elif item > second_item and second_item < min_nim:
                    min_nim = second_item
                    counter += 1
                else:
                    counter += 1
                    continue

    return min_nim,counter

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(find_min1(l))
