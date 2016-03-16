# Description
In this scenario a number messages are send from one end to all other nodes.

# prepare
Nothing to do here.

# initiate
### Usage
```
(<num> | *)
```
Send `<num>` messages to all other nodes. With `*` the default value 5 is set.

# watch-agent
Watches for all messages arriving.

### Usage
```
(<num> | *)
```
Waits for `<num>` messages. Waits for 5 messages, if `*` is used.

---


**NOTE:** The parameters has to be same in initiate and watch-agent, since the watch-agent would wait infinitely.