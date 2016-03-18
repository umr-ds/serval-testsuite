# Description
In this scenario messages are sent periodically on the active nodes. The time periods between the messages and the receivers of every message are randomly, but every time the same per node.

# prepare
Nothing to do here.

# initiate
Starts the SimpleMeshUser.py script on every active node.

### Usage
```
<timeout>
```
Messages will be sent for `<timeout>` seconds.

# watch-agent
Watches for a specific time.

### Usage
```
<timeout>
```
Finishes watching after `<timeout>` seconds.

---


**NOTE:** The `<timeout>` parameters has to be set seperately per script and a bit longer on watch-agent, to ensure waiting long enough to get all files.