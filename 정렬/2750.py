# 백준 2750번 수 정렬하기
# 시간 복잡도가 O(n**2)인 정렬 알고리즘으로 풀 수 있습니다. 예를 들면 삽입 정렬, 거품 정렬 등이 있습니다.

N = int(input())

number_list = []
for i in range(N):
    number_list.append(int(input()))

for i in sorted(number_list):
    print(i)

## bubble sort
bubble_list = []
for i in range(N):
    bubble_list.append(int(input()))
for i in range(len(bubble_list)-1):
    for j in range(len(bubble_list) -1 -i):
        if bubble_list[j] > bubble_list[j+1]:
            bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]
for x in bubble_list:
    print(x)

## insertion sort
insert_list = []
for i in range(1, len(insert_list)):
    j = i - 1
    key = insert_list[i]
    while insert_list[j] > key and j >= 0:
        insert_list[j+1] = insert_list[j]
        j = j - 1
    insert_list[j+1] = key
print(insert_list)
