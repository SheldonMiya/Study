# スクリプト内で標準出力のエンコーディングを指定

import sys
sys.stdout.reconfigure(encoding="utf-8")

"""
# selfとは

- クラスに作成する通常のメソッドは、インスタンスメソッドとも呼ばれる
- インスタンスメソッドの第１引数は self (実際は任意だが、慣習的に self とする)
- self はそのクラスの現在のインスタンスを表す
- self を介して、そのインスタンスの変数やメソッドにアクセスできる
- self はメソッド実行時に自動的に渡される引数である
"""

"""
# selfがある / ないで何ができて、何ができない

"""

# self が「ある」とできること

## １．インスタンスごとの状態を持てる

class User:
    def __init__(self, name):
        self.name = name
        print(f"ユーザ {self.name}が作成された")

u1 = User("健太")

"""
u1 = User("健太") の内部処理

u1 = User("健太")
     ↓
メモリ上にUserオブジェクト作成
     ↓
__init__(u1, "健太")が自動実行
     ↓
u1.name = "健太" が設定される
     ↓
ユーザ 健太が作成された（出力）

"""

## ２．メソッド間で同じデータを共有できる

class User2:
    def set_name(self, name):
        self.name = name
    
    def show_name(self):
        print(self.name)

u2 = User2()
u2.set_name("花子")
u2.show_name()

# self が「ない」と何ができない

## １．インスタンス変数を使えない

class User3:
    def greet():
        print("hello")

u3 = User3()
# u3.greet()  # エラーになる
# TypeError: greet() takes 0 positional arguments but 1 was given
# 理由：Pythonはメソッド呼び出し時に自動的にインスタンスを第１引数として渡すため

# クラス同士の連携

class User4:
    def __init__(self, name):
        self.name = name
    
    def create_order(self, item):
        return Order(self, item)

class Order:
    def __init__(self, user, item):
        self.user = user
        self.item = item
    
    def show(self):
        print(f"{self.user.name} が {self.item} を注文しました。")

user = User4("裕二")
order = user.create_order("本")
order.show()