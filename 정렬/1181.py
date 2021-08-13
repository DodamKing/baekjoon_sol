# 단어 정렬 실버5
# 단어의 순서를 정의하여 정렬하는 문제

n = int(input())
word_list = []
for _ in range(n):
    word_list.append(input())
word_list = list(set(word_list))
word_list.sort(key=lambda x:(len(x), str(x)))
print("\n".join(word_list))