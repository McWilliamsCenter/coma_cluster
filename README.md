# Coma Cluster

This is a wiki-page covering all you need to know about running and diagnosing jobs on Coma, the main computing workhorse shared by the cosmologists at the CMU [McWilliams Center](https://www.cmu.edu/cosmology/).


## System Description

Coma currently has in total 1144 cores, distributed among 61 different nodes. It has several large nodes for shared memory (OpenMP) applications, and allows for communication between nodes for applications using MPI


## Index

- [Getting Started](./getting_started.md)
- [Queues and Nodes](./queues_and_nodes.md)
- [Storage](./storage.md)
- [Scheduling Tips](./scheduling_tips.md)
- [Tips and Tricks](./tips_and_tricks.md)
- [FAQ](#faq)


## Logging In

You can use ssh to log-in to logon machine (a.k.a., the head node)

```console
user@local:~$ ssh -X yourusername@coma.hpc1.cs.cmu.edu
```

"The first rule of coma club is to never run jobs on the logon machine!" --- the Dictator
 
The head node should be used only to write and edit code, compile programs, and copy data between drives on coma or on external machines. It should **NOT** be used to perform computation-heavy jobs, since this could potentially crash the entire system. Even if it does not crash the machine, it slows down the head node for all users. 
 

## FAQ <a name="faq"></a>
 
- **How do I get started?**
	
	See [Getting Started](./getting_started.md) for information that you should know before you can use the cluster for the first time.
 
- **I want to use IDL (or python2.7) but it doesn't seem to be in my `PATH`, should I install them locally?**

	Coma does have both installed system-wide, and many more goodies: read the [Getting Started](./getting_started.md) page more carefully and look for the keyword "module".
 
- **What queues and nodes should I use?**

	See [Queues and Nodes](./queues_and_nodes.md) for a table of all the available computational resources on Coma.
 
- **What is Slurm?**

	See [Scheduling Tips](./scheduling_tips.md) for information about submitting jobs and some useful commands when using the [Slurm](https://slurm.schedmd.com/documentation.html) workload manager.
 
- **Where should I store my data?**

	See [Storage](./storage.md) for information about all the hard drives on Coma. 


## Help

Please direct help requests regarding this cluster to [help@cs.cmu.edu](help@cs.cmu.edu).




contact: duncanc@andrew.cmu.edu