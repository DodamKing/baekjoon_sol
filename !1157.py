# 단어공부
# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

word = input().upper()
word_list = list(set(word))
cnt_list = []

for i in word_list:
    count = word.count(i)
    cnt_list.append(count)
if cnt_list.count(max(cnt_list)) >= 2:
    print('?')
else:
    print(word_list[cnt_list.index(max(cnt_list))])
