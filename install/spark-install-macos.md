# Title: Spark Install in macOS

- [Title: Spark Install in macOS](#title-spark-install-in-macos)
  - [Spark Installation in macOS environment](#spark-installation-in-macos-environment)
    - [Check current java and javac version](#check-current-java-and-javac-version)
    - [Install Scala](#install-scala)
    - [Install Spark binary with Hadoop enabled](#install-spark-binary-with-hadoop-enabled)
    - [Setup path variable](#setup-path-variable)
    - [Configure Spark Config](#configure-spark-config)
    - [Check spark shell](#check-spark-shell)
    - [Check current python language version and install PySpark](#check-current-python-language-version-and-install-pyspark)
    - [Start spark in background/daemon mode](#start-spark-in-backgrounddaemon-mode)
    - [Stop spark process](#stop-spark-process)
  - [References](#references)
  - [Appendix](#appendix)

---

## Spark Installation in macOS environment
This installation work followed in macOS Big Sur with intel cpu evironment.  

### Check current java and javac version
Check java version in MacOS. Required java version is 8 / 11. If java is not available then install it by downloaing from oracle website. 
```bash
$ java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)
```

Java environment variable
```bash
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/
```    


### Install Scala

Download scala binary and install in desire location. Then scala in PATH variable. 

```bash
# get scala binary from scala website, scala depends on java 8/11
cd /usr/local/src
tar zxf scala-2.12.0-M1.tgz
ln -s scala-2.12.0-M1 scala
cd scala

$ scala -version
Scala code runner version 2.12.0-M1 -- Copyright 2002-2013, LAMP/EPFL
```
Setup environment variable for scala.
```bash
export SCALA_HOME="/usr/local/src/scala"
export PATH=$PATH:$SCALA_HOME/bin
```


### Install Spark binary with Hadoop enabled
Download latest spark binary with hadoop enabled. 
```bash
# pre build Spark 3.1.2 + hadoop 3.2 
wget https://www.apache.org/dyn/closer.lua/spark/spark-3.1.2/spark-3.1.2-bin-hadoop3.2.tgz
cd /usr/local/src
tar zxf spark-3.1.2-bin-hadoop3.2.tgz
ln -s spark-3.1.2-bin-hadoop3.2 spark
```

### Setup path variable
```bash
export SPARK_HOME=/usr/local/src/spark                              
export PATH=:$PATH:$SPARK_HOME/bin
# Configure Spark to use Hadoop classpath
export SPARK_DIST_CLASSPATH=$(hadoop classpath)
```

### Configure Spark Config
```bash
# copy spark config
cp $SPARK_HOME/conf/spark-defaults.conf.template $SPARK_HOME/conf/spark-defaults.conf

vi $SPARK_HOME/conf/spark-defaults.conf
spark.driver.host	localhost
# Enable the following one if you have Hive installed. 
# spark.sql.warehouse.dir /user/hive/warehouse
```

### Check spark shell
```bash
$ spark-shell
# :quit

# test program
run-example SparkPi 10
```

While spark program is running, gui can be seen at 
```bash
http://localhost:4040
```


### Check current python language version and install PySpark
```bash
% python --version
Python 2.7.16

% python3 --version
Python 3.9.1
```

Py Spark
```bash
pip3 install pyspark
# py4j-0.10.9 pyspark-3.1.2
```

### Start spark in background/daemon mode

Start spark master node.
```bash
#/usr/local/spark/sbin/start-master.sh
/usr/local/spark/sbin/start-all.sh
```
Check running java application
```bash
$ jps
```

Check spark gui interface -
```bash
http://localhost:8080
```

### Stop spark process
```bash
#/usr/local/spark/sbin/stop-master.sh
/usr/local/spark/sbin/stop-all.sh
```


## References
- https://spark.apache.org/docs/latest/
- https://kontext.tech/column/spark/596/apache-spark-301-installation-on-macos
- https://kontext.tech/column/hadoop/547/install-hadoop-330-on-mac



## Appendix

starup log for spark
```bash
Arif-MBP-2:conf arifhossen$ vim spark-defaults.conf
Arif-MBP-2:conf arifhossen$ spark-shell 
21/07/12 00:33:55 WARN Utils: Your hostname, Arif-MBP-2.local resolves to a loopback address: 127.0.0.1; using 192.168.31.61 instead (on interface en0)
21/07/12 00:33:55 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
21/07/12 00:33:56 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = local[*], app id = local-1626028444613).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.1.2
      /_/
         
Using Scala version 2.12.10 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_181)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
```


Check PySpark 
```bash
Arif-MBP-2:bin arifhossen$ pyspark
Python 3.9.1 (default, Jan  8 2021, 17:17:43) 
[Clang 12.0.0 (clang-1200.0.32.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
21/07/12 01:53:22 WARN Utils: Your hostname, Arif-MBP-2.local resolves to a loopback address: 127.0.0.1; using 192.168.31.61 instead (on interface en0)
21/07/12 01:53:22 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
21/07/12 01:53:23 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 3.1.2
      /_/

Using Python version 3.9.1 (default, Jan  8 2021 17:17:43)
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = local[*], app id = local-1626033205942).
SparkSession available as 'spark'.
>>> 
```

Check Pi program
```bash
Arif-MBP-2:bin arifhossen$ run-example SparkPi 10
21/07/12 00:40:29 WARN Utils: Your hostname, Arif-MBP-2.local resolves to a loopback address: 127.0.0.1; using 192.168.31.61 instead (on interface en0)
21/07/12 00:40:29 WARN Utils: Set SPARK_LOCAL_IP if you need to bind to another address
21/07/12 00:40:30 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
21/07/12 00:40:30 INFO SparkContext: Running Spark version 3.1.2
21/07/12 00:40:30 INFO ResourceUtils: ==============================================================
21/07/12 00:40:30 INFO ResourceUtils: No custom resources configured for spark.driver.
21/07/12 00:40:30 INFO ResourceUtils: ==============================================================
21/07/12 00:40:30 INFO SparkContext: Submitted application: Spark Pi
21/07/12 00:40:31 INFO ResourceProfile: Default ResourceProfile created, executor resources: Map(cores -> name: cores, amount: 1, script: , vendor: , memory -> name: memory, amount: 1024, script: , vendor: , offHeap -> name: offHeap, amount: 0, script: , vendor: ), task resources: Map(cpus -> name: cpus, amount: 1.0)
21/07/12 00:40:31 INFO ResourceProfile: Limiting resource is cpu
21/07/12 00:40:31 INFO ResourceProfileManager: Added ResourceProfile id: 0
21/07/12 00:40:31 INFO SecurityManager: Changing view acls to: arifhossen
21/07/12 00:40:31 INFO SecurityManager: Changing modify acls to: arifhossen
21/07/12 00:40:31 INFO SecurityManager: Changing view acls groups to: 
21/07/12 00:40:31 INFO SecurityManager: Changing modify acls groups to: 
21/07/12 00:40:31 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users  with view permissions: Set(arifhossen); groups with view permissions: Set(); users  with modify permissions: Set(arifhossen); groups with modify permissions: Set()
21/07/12 00:40:31 INFO Utils: Successfully started service 'sparkDriver' on port 62561.
21/07/12 00:40:31 INFO SparkEnv: Registering MapOutputTracker
21/07/12 00:40:31 INFO SparkEnv: Registering BlockManagerMaster
21/07/12 00:40:31 INFO BlockManagerMasterEndpoint: Using org.apache.spark.storage.DefaultTopologyMapper for getting topology information
21/07/12 00:40:31 INFO BlockManagerMasterEndpoint: BlockManagerMasterEndpoint up
21/07/12 00:40:31 INFO SparkEnv: Registering BlockManagerMasterHeartbeat
21/07/12 00:40:31 INFO DiskBlockManager: Created local directory at /private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/blockmgr-5a97d36b-7118-4b6d-a15b-f3205f8ae0ff
21/07/12 00:40:31 INFO MemoryStore: MemoryStore started with capacity 366.3 MiB
21/07/12 00:40:31 INFO SparkEnv: Registering OutputCommitCoordinator
21/07/12 00:40:31 INFO Utils: Successfully started service 'SparkUI' on port 4040.
21/07/12 00:40:31 INFO SparkUI: Bound SparkUI to 0.0.0.0, and started at http://localhost:4040
21/07/12 00:40:31 INFO SparkContext: Added JAR file:///usr/local/src/spark/examples/jars/scopt_2.12-3.7.1.jar at spark://localhost:62561/jars/scopt_2.12-3.7.1.jar with timestamp 1626028830919
21/07/12 00:40:31 INFO SparkContext: Added JAR file:///usr/local/src/spark/examples/jars/spark-examples_2.12-3.1.2.jar at spark://localhost:62561/jars/spark-examples_2.12-3.1.2.jar with timestamp 1626028830919
21/07/12 00:40:31 WARN SparkContext: The jar file:/usr/local/src/spark/examples/jars/spark-examples_2.12-3.1.2.jar has been added already. Overwriting of added jars is not supported in the current version.
21/07/12 00:40:32 INFO Executor: Starting executor ID driver on host 192.168.31.61
21/07/12 00:40:32 INFO Executor: Fetching spark://localhost:62561/jars/scopt_2.12-3.7.1.jar with timestamp 1626028830919
21/07/12 00:40:32 INFO TransportClientFactory: Successfully created connection to localhost/127.0.0.1:62561 after 48 ms (0 ms spent in bootstraps)
21/07/12 00:40:32 INFO Utils: Fetching spark://localhost:62561/jars/scopt_2.12-3.7.1.jar to /private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-4933cb28-3bd0-4213-9204-eec93dfccece/userFiles-c7751f55-7dc7-4d86-888f-938a23306631/fetchFileTemp4405551607929424415.tmp
21/07/12 00:40:32 INFO Executor: Adding file:/private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-4933cb28-3bd0-4213-9204-eec93dfccece/userFiles-c7751f55-7dc7-4d86-888f-938a23306631/scopt_2.12-3.7.1.jar to class loader
21/07/12 00:40:32 INFO Executor: Fetching spark://localhost:62561/jars/spark-examples_2.12-3.1.2.jar with timestamp 1626028830919
21/07/12 00:40:32 INFO Utils: Fetching spark://localhost:62561/jars/spark-examples_2.12-3.1.2.jar to /private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-4933cb28-3bd0-4213-9204-eec93dfccece/userFiles-c7751f55-7dc7-4d86-888f-938a23306631/fetchFileTemp6101439290454063857.tmp
21/07/12 00:40:32 INFO Executor: Adding file:/private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-4933cb28-3bd0-4213-9204-eec93dfccece/userFiles-c7751f55-7dc7-4d86-888f-938a23306631/spark-examples_2.12-3.1.2.jar to class loader
21/07/12 00:40:32 INFO Utils: Successfully started service 'org.apache.spark.network.netty.NettyBlockTransferService' on port 62563.
21/07/12 00:40:32 INFO NettyBlockTransferService: Server created on localhost:62563
21/07/12 00:40:32 INFO BlockManager: Using org.apache.spark.storage.RandomBlockReplicationPolicy for block replication policy
21/07/12 00:40:32 INFO BlockManagerMaster: Registering BlockManager BlockManagerId(driver, localhost, 62563, None)
21/07/12 00:40:32 INFO BlockManagerMasterEndpoint: Registering block manager localhost:62563 with 366.3 MiB RAM, BlockManagerId(driver, localhost, 62563, None)
21/07/12 00:40:32 INFO BlockManagerMaster: Registered BlockManager BlockManagerId(driver, localhost, 62563, None)
21/07/12 00:40:32 INFO BlockManager: Initialized BlockManager: BlockManagerId(driver, localhost, 62563, None)
21/07/12 00:40:33 INFO SparkContext: Starting job: reduce at SparkPi.scala:38
21/07/12 00:40:33 INFO DAGScheduler: Got job 0 (reduce at SparkPi.scala:38) with 10 output partitions
21/07/12 00:40:33 INFO DAGScheduler: Final stage: ResultStage 0 (reduce at SparkPi.scala:38)
21/07/12 00:40:33 INFO DAGScheduler: Parents of final stage: List()
21/07/12 00:40:33 INFO DAGScheduler: Missing parents: List()
21/07/12 00:40:33 INFO DAGScheduler: Submitting ResultStage 0 (MapPartitionsRDD[1] at map at SparkPi.scala:34), which has no missing parents
21/07/12 00:40:33 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 3.1 KiB, free 366.3 MiB)
21/07/12 00:40:33 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 1816.0 B, free 366.3 MiB)
21/07/12 00:40:33 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:62563 (size: 1816.0 B, free: 366.3 MiB)
21/07/12 00:40:33 INFO SparkContext: Created broadcast 0 from broadcast at DAGScheduler.scala:1388
21/07/12 00:40:33 INFO DAGScheduler: Submitting 10 missing tasks from ResultStage 0 (MapPartitionsRDD[1] at map at SparkPi.scala:34) (first 15 tasks are for partitions Vector(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
21/07/12 00:40:33 INFO TaskSchedulerImpl: Adding task set 0.0 with 10 tasks resource profile 0
21/07/12 00:40:33 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0) (192.168.31.61, executor driver, partition 0, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:33 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1) (192.168.31.61, executor driver, partition 1, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:33 INFO TaskSetManager: Starting task 2.0 in stage 0.0 (TID 2) (192.168.31.61, executor driver, partition 2, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:33 INFO TaskSetManager: Starting task 3.0 in stage 0.0 (TID 3) (192.168.31.61, executor driver, partition 3, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:33 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
21/07/12 00:40:33 INFO Executor: Running task 2.0 in stage 0.0 (TID 2)
21/07/12 00:40:33 INFO Executor: Running task 3.0 in stage 0.0 (TID 3)
21/07/12 00:40:33 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
21/07/12 00:40:34 INFO Executor: Finished task 3.0 in stage 0.0 (TID 3). 1000 bytes result sent to driver
21/07/12 00:40:34 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 1000 bytes result sent to driver
21/07/12 00:40:34 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 1000 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Starting task 4.0 in stage 0.0 (TID 4) (192.168.31.61, executor driver, partition 4, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO Executor: Running task 4.0 in stage 0.0 (TID 4)
21/07/12 00:40:34 INFO TaskSetManager: Starting task 5.0 in stage 0.0 (TID 5) (192.168.31.61, executor driver, partition 5, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO TaskSetManager: Starting task 6.0 in stage 0.0 (TID 6) (192.168.31.61, executor driver, partition 6, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO TaskSetManager: Finished task 3.0 in stage 0.0 (TID 3) in 791 ms on 192.168.31.61 (executor driver) (1/10)
21/07/12 00:40:34 INFO Executor: Running task 6.0 in stage 0.0 (TID 6)
21/07/12 00:40:34 INFO Executor: Running task 5.0 in stage 0.0 (TID 5)
21/07/12 00:40:34 INFO Executor: Finished task 2.0 in stage 0.0 (TID 2). 1000 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 857 ms on 192.168.31.61 (executor driver) (2/10)
21/07/12 00:40:34 INFO TaskSetManager: Starting task 7.0 in stage 0.0 (TID 7) (192.168.31.61, executor driver, partition 7, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 810 ms on 192.168.31.61 (executor driver) (3/10)
21/07/12 00:40:34 INFO TaskSetManager: Finished task 2.0 in stage 0.0 (TID 2) in 809 ms on 192.168.31.61 (executor driver) (4/10)
21/07/12 00:40:34 INFO Executor: Running task 7.0 in stage 0.0 (TID 7)
21/07/12 00:40:34 INFO Executor: Finished task 4.0 in stage 0.0 (TID 4). 957 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Starting task 8.0 in stage 0.0 (TID 8) (192.168.31.61, executor driver, partition 8, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO TaskSetManager: Finished task 4.0 in stage 0.0 (TID 4) in 77 ms on 192.168.31.61 (executor driver) (5/10)
21/07/12 00:40:34 INFO Executor: Finished task 7.0 in stage 0.0 (TID 7). 957 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Starting task 9.0 in stage 0.0 (TID 9) (192.168.31.61, executor driver, partition 9, PROCESS_LOCAL, 4578 bytes) taskResourceAssignments Map()
21/07/12 00:40:34 INFO TaskSetManager: Finished task 7.0 in stage 0.0 (TID 7) in 60 ms on 192.168.31.61 (executor driver) (6/10)
21/07/12 00:40:34 INFO Executor: Running task 9.0 in stage 0.0 (TID 9)
21/07/12 00:40:34 INFO Executor: Finished task 6.0 in stage 0.0 (TID 6). 957 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Finished task 6.0 in stage 0.0 (TID 6) in 86 ms on 192.168.31.61 (executor driver) (7/10)
21/07/12 00:40:34 INFO Executor: Running task 8.0 in stage 0.0 (TID 8)
21/07/12 00:40:34 INFO Executor: Finished task 5.0 in stage 0.0 (TID 5). 957 bytes result sent to driver
21/07/12 00:40:34 INFO Executor: Finished task 9.0 in stage 0.0 (TID 9). 957 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Finished task 5.0 in stage 0.0 (TID 5) in 136 ms on 192.168.31.61 (executor driver) (8/10)
21/07/12 00:40:34 INFO TaskSetManager: Finished task 9.0 in stage 0.0 (TID 9) in 58 ms on 192.168.31.61 (executor driver) (9/10)
21/07/12 00:40:34 INFO Executor: Finished task 8.0 in stage 0.0 (TID 8). 957 bytes result sent to driver
21/07/12 00:40:34 INFO TaskSetManager: Finished task 8.0 in stage 0.0 (TID 8) in 73 ms on 192.168.31.61 (executor driver) (10/10)
21/07/12 00:40:34 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
21/07/12 00:40:34 INFO DAGScheduler: ResultStage 0 (reduce at SparkPi.scala:38) finished in 1.433 s
21/07/12 00:40:34 INFO DAGScheduler: Job 0 is finished. Cancelling potential speculative or zombie tasks for this job
21/07/12 00:40:34 INFO TaskSchedulerImpl: Killing all running tasks in stage 0: Stage finished
21/07/12 00:40:34 INFO DAGScheduler: Job 0 finished: reduce at SparkPi.scala:38, took 1.526425 s
Pi is roughly 3.1404511404511406
21/07/12 00:40:34 INFO SparkUI: Stopped Spark web UI at http://localhost:4040
21/07/12 00:40:34 INFO MapOutputTrackerMasterEndpoint: MapOutputTrackerMasterEndpoint stopped!
21/07/12 00:40:34 INFO MemoryStore: MemoryStore cleared
21/07/12 00:40:34 INFO BlockManager: BlockManager stopped
21/07/12 00:40:34 INFO BlockManagerMaster: BlockManagerMaster stopped
21/07/12 00:40:34 INFO OutputCommitCoordinator$OutputCommitCoordinatorEndpoint: OutputCommitCoordinator stopped!
21/07/12 00:40:34 INFO SparkContext: Successfully stopped SparkContext
21/07/12 00:40:34 INFO ShutdownHookManager: Shutdown hook called
21/07/12 00:40:34 INFO ShutdownHookManager: Deleting directory /private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-0ae6e173-2ab7-40e5-b7be-f58aa5847cb6
21/07/12 00:40:34 INFO ShutdownHookManager: Deleting directory /private/var/folders/cm/j6yz6csj5mg2_qlc_9kbtsnh0000gp/T/spark-4933cb28-3bd0-4213-9204-eec93dfccece
Arif-MBP-2:bin arifhossen$ 
```