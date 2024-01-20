<h1 align="center">Hello Python 🐍 </h1>

## Chess ♟️
> Usually the modulo is taken according to the primary key. In order to facilitate expansion, the modulo is taken here for even numbers.

  ⬛  ⬛  ⬛  ⬛
⬛  ⬛  ⬛  ⬛  
  ⬛  ⬛  ⬛  ⬛
⬛  ⬛  ⬛  ⬛  
  ⬛  ⬛  ⬛  ⬛
⬛  ⬛  ⬛  ⬛  
  ⬛  ⬛  ⬛  ⬛
⬛  ⬛  ⬛  ⬛  

```
def main():
  for box in range(8):
      line = ""
      for col in range(8):
          if(box + col) % 2 == 0:
              line += "  "
          else:
              line += "⬛"
      print(line)

if __name__ == "__main__":
  main()
```

## Sub-database and sub-table
```
➜  ~ mysql.server start
Starting MySQL
. SUCCESS!
➜  ~ mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 10.1.17-MariaDB Homebrew

Copyright (c) 2000, 2016, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> select 1%4, 2%4, 3%4, 4%4, 5%4, 6%4, 7%4, 8%4;
+------+------+------+------+------+------+------+------+
| 1%4  | 2%4  | 3%4  | 4%4  | 5%4  | 6%4  | 7%4  | 8%4  |
+------+------+------+------+------+------+------+------+
|    1 |    2 |    3 |    0 |    1 |    2 |    3 |    0 |
+------+------+------+------+------+------+------+------+
1 row in set (0.00 sec)

MariaDB [(none)]> select 1%8, 2%8, 3%8, 4%8, 5%8, 6%8, 7%8, 8%8;
+------+------+------+------+------+------+------+------+
| 1%8  | 2%8  | 3%8  | 4%8  | 5%8  | 6%8  | 7%8  | 8%8  |
+------+------+------+------+------+------+------+------+
|    1 |    2 |    3 |    4 |    5 |    6 |    7 |    0 |
+------+------+------+------+------+------+------+------+
1 row in set (0.00 sec)

MariaDB [(none)]>
```


## Strace

```
strace -p [pid] -tt -s 1024 -o /tmp/[pid].log
```


##  Tuple

Why do we need to add a comma when the tuple has only one item?

```
In [1]: (3+4)*5
Out[1]: 35

In [2]: (3+4,)*5
Out[2]: (7, 7, 7, 7, 7)
```

```
In [3]: type(('fuck'))
Out[3]: str

In [4]: type(('fuck',))
Out[4]: tuple
```