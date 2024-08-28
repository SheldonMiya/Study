def can_shout(A, B, C):
    if B < C:
        # 高橋君がB時からC時の間に寝る
        if A >= B and A < C:
            return "No"
        else:
            return "Yes"
    else:
        # 高橋君がC時からB時の間に寝る
        if A >= B or A < C:
            return "No"
        else:
            return "Yes"

# 入力
A = int(input("叫ぶ時間 A: "))
B = int(input("寝る時間 B: "))
C = int(input("起きる時間 C: "))

print(can_shout(A, B, C))

