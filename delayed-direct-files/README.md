# Description
In this scenario encrypted files are sent periodically on the active nodes. The time periods between the files and the receivers of every file are randomly, but every time the same per node.

# prepare
Nothing to do here.

# initiate
Starts the DirectedRhizomeAdder.py script on every active node.

### Usage
```
t <sec> (f1 | f2 | f3)
```
With the `t` parameter, messages will be sent for `<sec>` seconds.
With `f1` files with a size 250kB will be added, with `f2` with 5MB and with `f3` with 50MB.

# watch-agent
Watches for a specific time.

### Usage
```
t <sec>
```
With the `t` parameter, finishes watching after `<sec>` seconds.

---


**NOTE:** The `t` parameters has to be set seperately per script.