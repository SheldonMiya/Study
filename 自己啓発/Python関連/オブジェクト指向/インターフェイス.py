from abc import ABC, abstractmethod

# インターフェイス的な役割を持つ抽象基底クラス

class PersonInterface(ABC):
    @abstractmethod
    def say_hello(self):
        pass

# 子クラス: Student

class Student(PersonInterface):
    def __init__(self, name):
        self.name = name

    # def say_hello(self):
    #     print(f"こんにちは、私は学生の{self.name}です。")

# 子クラス: Teacher

class Teacher(PersonInterface):
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"こんにちは、私は教師の{self.name}です。")

# 実際に使ってみる

Teacher1 = Teacher("佐藤")
Teacher1.say_hello()  # Teacherクラスのメソッドを呼び出

Student1 = Student("花子")
# 以下の行はエラーになる（抽象メソッドが実装されていないため）
# Student1.say_hello()  # TypeError: Can't instantiate abstract class Student with abstract

"""
# 知識ポイント

Python には interface キーワードはない
- 代わりに、abc モジュールの抽象基底クラス(ABC)を使って「インターフェイス的な役割」を持つクラスを定義する
- @abstractmethod デコレータを使うと、「必ず子クラスで実装しなければならない」メソッドになる

具象クラス
- そのままインスタンス化できる
- 共通の処理を持ち、子クラスに継承させて再利用できる

抽象クラス = インターフェイス的な役割
- 直接インスタンス化できない
- say_helloを必ず子クラスで実装させる「契約」を定義する
"""