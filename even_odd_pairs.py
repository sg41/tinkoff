n = int(input())
pairs = list(map(int, input().split()))
error = 0
err_list = []
even = 0
odd = 0
for i, d in enumerate(pairs):
    if (i+1) % 2 != d % 2:
        if (i+1) % 2 == 0:
            even += 1
        else:
            odd += 1
        error += 1
        err_list.append(i)
if error == 2 and odd == even:
    print(err_list[0]+1, err_list[1]+1)
else:
    print("-1 -1")
