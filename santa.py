n = int(input())
a = list(map(int, input().split()))
error = 0
self_list = []
no_gift = []
for i, d in enumerate(a):
    if (i+1) == a[i]:
        error += 1
        self_list.append(i)
    if i+1 not in a:
        no_gift.append(i)
        error += 1

if error == 2 and len(self_list) == len(no_gift):
    print(self_list[0]+1, no_gift[0]+1)
else:
    print("-1 -1")
