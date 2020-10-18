#URI - 1590
def find(num_list, bit, k, res):
    if not bit >= 0:
        return res
    else:
        new_num_list = []
        for num in num_list:
            if num & (1 << bit):
                new_num_list.append(num)
        if len(new_num_list) >= k:
            num_list = new_num_list
            res = res + (1 << bit)
        return find(num_list, bit - 1, k, res)


t = int(input())

for rep in range(t):
    [n, k] = map(int, input().split())
    numbers = list(map(int, input().split()))

    num_bits = 0
    for num in numbers:
        if num.bit_length() > num_bits:
            num_bits = num.bit_length()

    result = find(numbers, num_bits - 1, k, 0)
    
    print(result)