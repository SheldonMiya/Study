# 全体像

`*`  
役割：引数の区切り・展開  
一言で：ここから先は特別

`*args`  
役割：可変長位置引数   
一言で：何個でも受け取る

`**kwargs`  
役割：可変長キーワード引数  
一言で：名前付きで何でも


# 具体的

## `*args`

`*args`：個数が決まらない引数を受ける  

### `*args` ないとできないこと

```python
def add(a, b, c):
    return a + b + c
```
- 引数の数が固定
- 呼び出し側が不自由

### `*args` があると

```python
def add(*args):
    return sum(args)

add(1, 2)
add(1, 2, 3, 4)
```

### 何が起きている？

- `args`は tuple
- 位置引数が全部まとめて入る
- → 「個数を気にしなくていい関数」

## `*kwargs`

`**kwargs`：名前付き引数をまとめて受ける

```python
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

show_profile(name="健太", age=25, job="engineer")
```
- `kwargs`はdict
- キー = 引数名
- → 拡張に強いAPI

## `*`

`*`（単体）：引数の意味を変える  

以降はキーワード専用
```python
def create_user(name, *, age, job):
    pass

create_user("健太", age=25, job="engineer")
```

