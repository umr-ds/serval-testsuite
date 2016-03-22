# Description
Runs all scenarios at once.

# prepare
Nothing to do here.

# initiate
Initiates all scenarios. For more information see the README of the respective scenario.

### Usage
```
<timeout> (f1 | f2 | f3 | f4) (t <timeout> | f <file_count>) <salt>
```

# watch-agent
Waits, unitl all scenarios are finished. For the sake of convenience, this script wait's only for a timeout.

### Usage
```
<timeout>
```

---

**NOTE:** The first `<timeout>` parameter is for delayed messages and delayed directed files. The second `<timtout>`, that after the `t` is for delayed files.
**NOTE:** The `<timeout>` for the watch-agent should be a lot higher than the timeouts in initiate, since the delayed files and mass injects can be very long.