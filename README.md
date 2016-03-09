# serval-testsuite

## Architecture
Each test consists of seven phases:
 
 1. **prepare** (active nodes)
 2. start system monitoring (**TODO**)
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
- ```1``` servald crashed
- ```2``` timeout reached
- ```...``` your return code here

This way the operator is able to debug the scenario. It's also possible to write to stdout for all three scripts.

## CORE Related:
### Invoke Scenario

To run a scenario use the **core-gui** to start it and then use **core-scenario** to start the scenario:

```bash
usage: $0 scenario [n1 ... | -a ]
starts a scenario with prepare/initiate at all given nodes
```

Example: ```$ ./core-scenario mass-inject-file n1```



### Helpers
* **core-daemonize-all** - executes and forks a command on every core node (silently)
* **core-execute-all** - excecutes a command on every core node and shows the output
* **core-get-sids** - writes SIDs from all core nodes to $SEVERAL_ALL_SIDS_FILE
* **core-parallel-all** - executes a command parallel on every core node
* **core-watch-serval** - watches servald on every core node, and tells if one crashed
* **show-log** - should be run from main host, opens log of given node name in less for viewing or if -n is appended just outputs the absolute log file path (e.g. $ show-log n12 )

### Requirements

The core nodes do need some files in place:

 - **/home/meshadmin/serval-tests/\***
 - **servald**
