# Description
In this scenario a number files is send from one end to all other nodes.

# prepare
Generates files which will be sent on initiate.
### Usage
```
<num> <path> <bytesize> <bytecount>
```
Generate `<num>` files in `<path>` with `<bytesize>` times `<bytecount>` size.

# initiate
Adds all files in the fiven path.

### Usage
```
<path>
```
The parameter `<path>` is the path, where the generated testfiles are.

# watch-agent
Watches for a number of files.

### Usage
```
<num>
```
Waits, until `<num>` files arrived.

---


**NOTE:** The `<path>` parameters has to be the same.
**NOTE:** The `<num>` parameters has to be the same.