def find_second_oldest(S_AB, S_AC, S_BC):
    # 各兄弟の年齢を格納する辞書
    ages = {'A': 0, 'B': 0, 'C': 0}
    
    # S_ABの処理
    if S_AB == '<':
        ages['A'] = 1
        ages['B'] = 2
    else:
        ages['A'] = 2
        ages['B'] = 1
        
    # S_ACの処理
    if S_AC == '<':
        ages['C'] = ages['A'] + 1
    else:
        ages['A'] = ages['C'] + 1
        
    # S_BCの処理
    if S_BC == '<':
        ages['C'] = ages['B'] + 1
    else:
        ages['B'] = ages['C'] + 1
    
    # 年齢をソートして次男を見つける → 例：[('A', 2), ('B', 1), ('C', 3)]
    # lambda式
    sorted_brothers = sorted(ages.items(), key=lambda x: x[1])
    
    return sorted_brothers[1][0]  # 次男の名前を返す 

# 入力を1行で受け取る
input_line = input()
S_AB, S_AC, S_BC = input_line.split()

# 次男を求める
second_oldest = find_second_oldest(S_AB, S_AC, S_BC)

print(second_oldest)