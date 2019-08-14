# Queues & Nodes 


This page contains information on the current queues and nodes installed on the Coma cluster. 

This page was last populated on: 8/14/2019

## Queues 


Below is a list of the current queues Coma, including the number of nodes,             and the time limit for jobs. 


Queue | Number of Nodes | Time Limit [days-hours:minutes:seconds] 
----- | --------------- | --------------------------------------- 
DEBUG | 0 | infinite 
bigmem | 2 | 7-00:00:00 
long | 13 | 7-00:00:00 
short | 16 | 8:00:00 


## Nodes 


Below is a list of the current nodes installed on Coma, including the number of processors,             amount of memory, CPU architecture, and queue(s) to which they belong. 
More information on a specific node can be retrieved with the following command: 

```console 
user@local:~$ scontrol show node [NODE_NAME] 
``` 


Node | Number of Processors | Total Memory | CPU Architecture | Queues 
---- | -------------------- | ------------ | ---------------- | ------ 
compute-1-1 | 64 | 512 | AMD | long, bigmem 
compute-1-11-1 | 20 | 128 | Intel | short, long 
compute-1-11-2 | 20 | 128 | Intel | short, long 
compute-1-11-3 | 20 | 128 | Intel | short, long 
compute-1-11-4 | 20 | 128 | Intel | short, long 
compute-1-13-1 | 20 | 128 | Intel | short, long 
compute-1-13-2 | 20 | 128 | Intel | short, long 
compute-1-13-3 | 20 | 128 | Intel | short, long 
compute-1-13-4 | 20 | 128 | Intel | short, long 
compute-1-15-1 | 20 | 128 | Intel | short, long 
compute-1-15-2 | 20 | 128 | Intel | short, long 
compute-1-15-3 | 20 | 128 | Intel | short, long 
compute-1-15-4 | 20 | 128 | Intel | short, long 
compute-1-17 | 16 | 128 | Intel | short 
compute-1-18 | 16 | 128 | Intel | short 
compute-1-19 | 16 | 128 | Intel | short, long 
compute-1-20 | 16 | 128 | Intel | short, long 
compute-1-21 | 16 | 128 | Intel | short, long 
compute-1-22 | 16 | 128 | Intel | short, long 
compute-1-23 | 16 | 128 | Intel | short, long 
compute-1-24 | 20 | 128 | Intel | short, long 
compute-1-25 | 20 | 128 | Intel | short, long 
compute-1-26 | 20 | 128 | Intel | short, long 
compute-1-27 | 20 | 128 | Intel | short, long 
compute-1-28 | 20 | 128 | Intel | short, long 
compute-1-29 | 20 | 128 | Intel | short, long 
compute-1-30 | 20 | 128 | Intel | short, long 
compute-1-31 | 20 | 128 | Intel | short, long 
compute-1-32 | 20 | 128 | Intel | short 
compute-1-33 | 20 | 0 | Intel | none 
compute-1-5-1 | 16 | 128 | Intel | short, long 
compute-1-5-2 | 16 | 128 | Intel | short, long 
compute-1-5-3 | 16 | 128 | Intel | short, long 
compute-1-5-4 | 16 | 128 | Intel | short, long 
compute-1-7-1 | 16 | 128 | Intel | short, long 
compute-1-7-2 | 16 | 128 | Intel | short, long 
compute-1-7-3 | 16 | 128 | Intel | short, long 
compute-1-7-4 | 16 | 128 | Intel | short, long 
compute-1-9-1 | 20 | 128 | Intel | short, long 
compute-1-9-2 | 20 | 128 | Intel | short, long 
compute-1-9-3 | 20 | 128 | Intel | short, long 
compute-1-9-4 | 20 | 128 | Intel | short, long 
compute-2-1 | 32 | 1024 | Intel | long, bigmem 
compute-2-10 | 16 | 32 | AMD | short, long 
compute-2-12 | 16 | 32 | AMD | short, long 
compute-2-14 | 16 | 32 | AMD | short, long 
compute-2-16 | 16 | 32 | AMD | short, long 
compute-2-18 | 16 | 32 | AMD | short, long 
compute-2-20 | 16 | 32 | AMD | short, long 
compute-2-22 | 16 | 32 | AMD | short, long 
compute-2-24 | 16 | 32 | AMD | short, long 
compute-2-26 | 16 | 32 | AMD | short, long 
compute-2-28 | 16 | 32 | AMD | short, long 
compute-2-30 | 16 | 32 | AMD | short, long 
compute-2-32 | 16 | 32 | AMD | short, long 
compute-2-34 | 16 | 32 | AMD | short, long 
compute-2-36 | 16 | 32 | AMD | short, long 
compute-2-38 | 16 | 32 | AMD | short, long 
compute-2-40 | 16 | 32 | AMD | short, long 
compute-2-6 | 16 | 32 | AMD | short, long 
compute-2-8 | 16 | 32 | AMD | short, long 


This page was created by running the `queues_and_nodes.py` script on Coma. 
