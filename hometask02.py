from collections import deque

s = input('Enter string for palyndrome check >>> ')
s1 = s.lower().replace(' ','')

q = deque()
for i in range(len(s1)):
    q.append(s1[i])

answer = 'Yes, this is palyndrome'
for i in range(len(q.queue)//2):
    if q.pop() != q.popleft():
        answer = 'Not a palyndrome'

print(f'Texst "{s}": {answer}')