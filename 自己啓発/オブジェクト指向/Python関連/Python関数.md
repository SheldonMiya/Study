# 関数

## input()

機能

- 標準入力からユーザーの入力を受け取るための関数

使い方

- `input()`を呼び出すと、プログラムはユーザーからの入力を待機する。ユーザーが何かを入力してEnterキーを押すと、その入力が文字列として返される
- 例：

   ``` python
   user_input = input()
   print(user_input)
   ```

## split()

機能

- 文字列を指定した区切り文字で分割し、リストを作成するためのメソッド

使い方

- `split()`メソッドは、文字列に対して呼び出す。引数を指定しない場合は、空白(スペース、タブ、改行)を区切りとして使用する
- 例：

    ```python
    text = "Hello World"
    words = text.split()
    ```

    ```python
    data = "1,2,3"
    numbers = data.split(",") #['1','2' '3']
    ```

## map()

機能

- 関数を指定したイテラブル(リストなど)の各要素に適用し、その結果を生成するための関数

使い方

- `map(function, iterable)`の形式で使用する、`function`は適用する関数、`iterable`は対象のリストやタプルなど
　結果は`map`オブジェクトとして返されるが、リストに変換して使用することが一般的

## enumerate()(イーナムレート)

機能

- `enumerate`関数は、リストやその他の反復可能なオブジェクトをループ処理する際に、要素とそのインデックスを同時に取得できる

使い方

入力

```python
a = [10, 20, 30, 40]
for i, a_i in enumerate(a):
    print(f"Index: {i}, Value: {a_i}")
```

出力

```yml
Index: 0, Value: 10
Index: 1, Value: 20
Index: 2, Value: 30
Index: 3, Value: 40
```
