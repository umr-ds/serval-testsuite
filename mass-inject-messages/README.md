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

# Example
```
./scenario core mass-inject-messages/ "" "*" "*" 0
```
With this call, 5 messages will be sent from node 0, while the watch agent watches for 5 arriving messages.

```
./scenario core mass-inject-messages/ "" "18" "18" 1
```
With this call, 18 messages will be sent from node 1, while the watch agent watches for 18 arriving messages.