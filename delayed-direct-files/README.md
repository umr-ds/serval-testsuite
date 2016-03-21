# Description
In this scenario encrypted files are sent periodically on the active nodes. The time periods between the files and the receivers of every file are randomly, but every time the same per node.

# prepare
Nothing to do here.

# initiate
Starts the DirectedRhizomeAdder.py script on every active node.

### Usage
```
<timeout> (f1 | f2 | f3)
```
Files will be sent for `<timeout>` seconds.
With `f1` files with a size between 64k and 512k will be added, with `f2` between 1M and 10 M and with `f3` with 25M and 100M.

# watch-agent
Watches for a specific time.

### Usage
```
<timeout>
```
Finishes watching after `<timeout>` seconds.

---

**NOTE:** The `<timeout>` parameters has to be set seperately per script and a bit longer on watch-agent, to ensure waiting long enough to get all files.

# Example
```
./scenario core delayed-direct-files/ "" "10" "5 f2" 0
```

With this call, the watch-agent will wait 10 seconds, while the initiate script will send files for 5 seconds on node 0 from the test-set 2.