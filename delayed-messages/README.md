# Description
In this scenario messages are sent periodically on the active nodes. The time periods between the messages and the receivers of every message are randomly, but every time the same per node.

# prepare
Nothing to do here.

# initiate
Starts the SimpleMeshUser.py script on every active node.

### Usage
```
t <sec>
```
With the `t` parameter, messages will be sent for `<sec>` seconds.

# watch-agent
Watches for a specific time.

### Usage
```
t <sec>
```
With the `t` parameter, finishes watching after `<sec>` seconds.

---


**NOTE:** The `t` parameters has to be set seperately per script.