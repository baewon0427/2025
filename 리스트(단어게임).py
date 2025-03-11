que = ["teacher","student","milk","sakuya"]
ans1 = ["교사","학생","우유","사쿠야"]
ans2 = ["선생님","학생","우유","사쿠야"]

for i in range(4):
    print(que[i], "는 무슨 뜻인가용?")
    a = input()

    if ans1[i] == a:
        print("정답입니당! 사쿠야가 행운을 줄게욤!!")

    if ans2[i] == a:
        print("정답입니당! 사쿠야가 행운을 줄게욤!!")