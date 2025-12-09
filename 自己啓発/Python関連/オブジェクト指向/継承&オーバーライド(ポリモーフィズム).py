# スクリプト内で標準出力のエンコーディングを指定

import sys
sys.stdout.reconfigure(encoding='utf-8')

# 親クラス: Person

class Person:
    def __init__(self, name, age): # コンストラクタ
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"こんにちは、私は{self.name}です。{self.age}歳です。")

# 子クラス: Student

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 親クラスの初期化(コンストラクタ)を呼び出す
        self.student_id = student_id

    # メソッドのオーバーライド(ポリモーフィズム)

    def say_hello(self):
        print(f"こんにちは、私は学生の{self.name}です。{self.age}歳で、学生番号は{self.student_id}です。")

# 子クラス: Teacher

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # 親クラスの初期化(コンストラクタ)を呼び出す
        self.subject = subject

    # メソッドのオーバーライド(ポリモーフィズム)

    def say_hello(self):
        print(f"こんにちは、私は教師の{self.name}です。{self.age}歳で、担当科目は{self.subject}です。")

# 子クラス: HeadMaster

class HeadMaster(Person):
    def __init__(self, name, age, school_name):
        super().__init__(name, age)  # 親クラスの初期化(コンストラクタ)を呼び出す
        self.school_name = school_name

    # メソッドのオーバーライド(ポリモーフィズム)

    def say_hello(self):
        print(f"こんにちは、私は校長の{self.name}です。{self.age}歳で、{self.school_name}の校長を務めています。")

# 実際に使ってみる

person1 = Person("太郎", 30)
student1 = Student("花子", 20, "S12345")
teacher1 = Teacher("佐藤", 40, "数学")
headmaster1 = HeadMaster("鈴木", 50, "東洋大学附属高校")

# 同じメソッド名でも、呼び出すオブジェクトによって振る舞いが変わる（ポリモーフィズム）

person1.say_hello()  # Personクラスのメソッドを呼び出す
student1.say_hello()  # Studentクラスのオーバーライドされたメソッドを呼び出す
teacher1.say_hello()  # Teacherクラスのオーバーライドされたメソッドを呼び出す
headmaster1.say_hello()  # HeadMasterクラスのオーバーライドされたメソッドを呼び出す

"""
# 知識ポイント

1. クラスとインスタンス
- class Person: でクラスを定義
- person1 = Person("太郎", 30) でインスタンスを生成
→ クラスは「設計図」、インスタンスは「実体」

2. コンストラクタ(__init__)
- __init__はインスタンス生成時に呼ばれる初期化メソッド
- self.name = name のように属性を設定
- 子クラスでは super().__init__(...) で親クラスのコンストラクタを呼び出す

3. 継承
- class Student(Person): のように Person を継承
- 親クラスの機能を再利用しつつ、子クラス独自の属性やメソッドを追加できる
    - 例：Student は student_id を追加、 Teacher は subject を追加

4. メソッドのオーバーライド(ポリモーフィズム)
- 子クラスで親クラスと同じ名前のメソッドを定義すると「オーバーライド」になる
    - 例：say_hello() を各クラスで書き換え
- 同じメソッド名でも、オブジェクトによって振る舞いが変わる
    - 例：student1.say_hello() → 学生用の挨拶, teacher1.say_hello() → 教師用の挨拶, headmaster1.say_hello() → 校長用の挨拶

# 用語整理

クラス：設計図。属性やメソッドを定義する
- 例：class Person:

インスタンス(実体、オブジェクト)：クラスから実際に生成されたもの
- 例：person1 = Person("太郎", 30) → この person1 がインスタンス

コンストラクタ：インスタンス生成時に呼ばれる初期化メソッド

継承：あるクラスが別のクラスの属性やメソッドを引き継ぐこと

オーバーライド：子クラスで親クラスと同じ名前のメソッドを再定義すること

ポリモーフィズム(多態性、多様性)：同じメソッド名でも、オブジェクトによって異なる振る舞いをすること
- 実現方法：主にオーバーライド(メソッドの上書き)とオーバーロード(メソッドの多重定義)の2つがある
- **注意点**
    PythonにはJavaやC++のような「メソッドのオーバーロード（同じ名前で引数の型や数が違うメソッドを複数定義）」はない
    Pythonでは「最後に定義したものが有効になる」ため、同じ名前で複数メソッドを書くと上書きされてしまう

# オブジェクト

オブジェクト指向のオブジェクト
→ クラスから生成されたインスタンスのこと

Pythonのオブジェクト
→ Pythonの世界では「すべてがオブジェクト」。数値・文字列・関数・クラスなども含む広い意味
"""