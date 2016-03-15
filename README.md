# serval-testsuite

## Architecture
Each test consists of seven phases:

 1. **prepare** (active nodes)
 2. start system monitoring
 3. start servald
 4. start servald monitoring
 5. start **watch-agent**s
 6. **initiate** scenario (active nodes)
 7. waiting for watch-agents
 8. teardown: stop monitoring and servald
 9. data collection

The phases 1,5 and 6 *must* be configured per scenario. This is done via shell scripts with the given name in the scenario subfolder.

**prepare** and **initiate** is executed on active nodes.

The **watch-agent** is executed on *every* node and should exit using the following return codes:

- ```0``` exit condition reached
- ```1``` agent script crashed
- ```2``` servald crashed
- ```3``` timeout reached
- ```...``` your return code here

This way the operator is able to debug the scenario. It's also possible to write to stdout for all three scripts.

## Invoke Scenario

To run a scenario use the **core-gui** or **MiniWorld** to start it and then use **scenario** to start the scenario:

```bash
usage: $0 scenario (core | miniworld) p w i [0 ... | -a ]
starts a scenario with prepare/initiate at all given nodes
       params for scripts: p - preparations
       params for scripts: w - watch-agents
       params for scripts: i - initiate
```

Example: ```$ ./scenario core mass-inject-file 0```



### Helpers
* **core-daemonize-all** - executes and forks a command on every core node (silently)
* **core-execute-all** - excecutes a command on every core node and shows the output
* **core-get-sids** - writes SIDs from all core nodes to $SEVERAL_ALL_SIDS_FILE
* **core-parallel-all** - executes a command parallel on every core node
* **core-watch-serval** - watches servald on every core node, and tells if one crashed
* **show-log** - should be run from main host, opens log of given node name in less for viewing or if _-n_ is appended just outputs the absolute log file path (e.g. ```$ show-log n12 ```)
* **check-crash** - checks all running core nodes under /tmp for logs containing crash information. These can be displayed using _show-log_

### Requirements

The core nodes do need some files in place:

 - **/home/meshadmin/serval-tests/\***
 - **servald**

### Setup Scenario

New directory is the scenario name
Three files are needed:

* **prepare** - is done right after the start before anything else
* **watch-agent** - is used to monitor for results
* **initiate** - triggers the test itself

All scripts get these parameters when executed:

 * $1: Number of nodes in the scenario 
 * $2: Number of *active* nodes
 * $3...: User specified in **p, w or i** 
