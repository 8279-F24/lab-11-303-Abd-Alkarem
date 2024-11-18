numbers = list(map(int, input().split()))

negative_numbers = sorted([num for num in numbers if num < 0], reverse=True)

for num in negative_numbers:
    print(num, end=' ')
