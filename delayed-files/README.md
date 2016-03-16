# Description
In this scenario files are added periodically on the active nodes. The time periods between the files are randomly, but every time the same per node.

# prepare
Nothing to do here.

# initiate
Starts the SimpleRhizomeAdder.py script on every active node.

### Usage
```
(t <sec> | f <num>) (<f1 | f2 | f3>)
```
With the `t` parameter, files will be added for `<sec>` seconds. With `f` only `<num>` files will be added.

With `f1` files with a size 250kB will be added, with `f2` with 5MB and with `f3` with 50MB.

# watch-agent
Watches for a specific time or for a specific number of files.

### Usage
```
(t <sec> | f <num>)
```
With the `t` parameter, finishes watching `<sec>` seconds. With `f` after receiving `<num>` files.

---


**NOTE:** The `t` parameters has to be set seperately.