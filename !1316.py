# 그룹 단어 체커 실버5 
# 조건에 맞는 문자열을 찾는 문제
# 풀이 봄 ㅠㅠ

N = int(input())
group_word = 0
for i in range(N):
    word = input()
    count = 0
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                count = count + 1
    if count == 0:
        group_word = group_word + 1
print(group_word)
