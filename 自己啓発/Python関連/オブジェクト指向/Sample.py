# スクリプト内で標準出力のエンコーディングを指定

import sys
sys.stdout.reconfigure(encoding='utf-8')

# 親クラス
class Person:
    def __init__(self, name, age):
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

    def say_hello(self):
        print(f"こんにちは、私は教師の{self.name}です。{self.age}歳で、担当科目は{self.subject}です。")

# 子クラス: HeadMaster

class HeadMaster(Person):
    def __init__(self, name, age, school_name):
        super().__init__(name, age)  # 親クラスの初期化(コンストラクタ)を呼び出す
        self.school_name = school_name

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