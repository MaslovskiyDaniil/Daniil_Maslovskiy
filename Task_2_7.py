a = int(input())
b = int(input())
c = int(input())
cnt = 0
if a == b:
    cnt += 1
if b == c:
    cnt += 1
if c == a:
    cnt += 1
print(cnt)