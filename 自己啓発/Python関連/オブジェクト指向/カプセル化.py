class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner # 公開属性(誰の口座かは公開してよい)
        self.__balance = balance  # プライベート属性(残高は外部から直接アクセスさせたくない)

    # 残高を取得する公開メソッド

    def get_balance(self):
        return self.__balance

    # 入金メソッド

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}円を入金しました。現在の残高は{self.__balance}円です。")
        else:
            print("入金額は正の数でなければなりません。")

    # 出金メソッド

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}円を出金しました。現在の残高は{self.__balance}円です。")
        else:
            print("残高不足または不正な出金額です。")

# 実際に使ってみる

account = BankAccount("健太", 1000)
print(f"口座所有者: {account.owner}")
print(f"現在の残高: {account.get_balance()}円")

account.deposit(500)
account.withdraw(300)

# 以下の行はエラーになる（プライベート属性に直接アクセスしようとするため）
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'


"""
# 知識ポイント

カプセル化：オブジェクトの変数には直接アクセスせず、メソッドだけを通してオブジェクトを操作する手法。隠蔽処理ともよばれる

マングリング：特定の識別子の名前を変更することで、意図しないアクセスや衝突を防ぐ仕組み
    - Python では、クラスの変数やメソッド名にダブルアンダースコア（__）を付けるとマングリングが適用される
"""