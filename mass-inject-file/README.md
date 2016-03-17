# Description
In this scenario a number files is send from one end to all other nodes.

# prepare
Generates files which will be sent on initiate.
### Usage
```
<fileset> [number]
```
Generate `<fileset>` `<number>` times.
There are 4 different filesets available:

* f1 - small - 64K, 256K, 512K - 3 files total
* f2 - medium - 1M, 5M, 10M - 3 files total
* f3 - large - 25M, 50M, 100M - 3 files total
* f4 - all of the above - 9 files total

# initiate
Nothing to be done here.

# watch-agent
Watches for a number of files.

### Usage
```
<num>
```
Waits, until `<num>` files arrived. Remember to calculate correctly, depending on the `fileset` and the multiplier!
