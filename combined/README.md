# Description
Runs all scenarios at once.

# prepare
Generates files which will be sent on initiate.
### Usage
```
<num_files> <path> <bytesize> <bytecount>
```
Generate `<num_files>` files in `<path>` with `<bytesize>` times `<bytecount>` size.

# initiate
Initiates all scenarios. For more information see the README of the respective scenario.

### Usage
```
<timeout> (f1 | f2 | f3) (f <num_delayed_files> | t <timeout>) <path> <num_messages>
```

# watch-agent
Waits, unitl all scenarios are finished. For detailed finishing conditions, see the README of the resprective scenario.

### Usage
```
<timeout> (f <num_delayed_files> | t <timeout>) <num_files> <num_messages>
```

---

**NOTE:** `<num_files>` has to be the same.
**NOTE:** `<path>` has to be the same.
**NOTE:** Both `<timeout>` parameters in initate has to be the same.
**NOTE:** Both `<timeout>` parameters in watch-agent has to be the same.
**NOTE:** `<num_delayed_files>` has to be the same.
**NOTE:** `<num_messages>` hast to be the same.
**NOTE:** `<timeout>` in watch-agent has to be higher than in initiate.