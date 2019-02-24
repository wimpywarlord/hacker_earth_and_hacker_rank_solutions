VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
 
 
def main(string):
    array = []
    for i in string:
        if i in VOWELS:
            array.append(1)
        else:
            array.append(0)
    total_sum = 0
    l = len(string)
    for i in range(l):
        if array[i] == 1:
            total_sum += ((l - i) * (i + 1))
    return total_sum
    
 
for _ in range(int(input())):
    print(main(input()))
