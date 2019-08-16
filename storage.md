# Storage 

There are three types of storage on the cluster: local storage on the head node, ZFS storage exported via NFS, and Lustre storage.  The local storage is a hardware-based RAID* which is backed up to external tapes once a day.  The ZFS storage is similar to a software-based RAID with additional data protection features such as copy-on-write, snapshots, and scrubbing.  The Lustre storage is a parallel distributed file system
that provides high-performance I/O throughput.


MOUNT POINT | SIZE | TYPE | PROTECTION | HIGH-PERFORMACE
----------- | ---- | ---- | ---------- | ---------------
/home | 5T | local | tape | no
/nfs/nas-0-1 | 164T | ZFS | snapshots | no
/nfs/nas-0-9 | 164T | ZFS | snapshots | no
/lustre | 42T | Lustre | none** | yes
/physics | 126T | Lustre | none | yes
/physics2 | 284T | Lustre | none | yes

Generally speaking, we'd encourage people to store very important files,
e.g. analysis code, on the head node, large datasets and results in ZFS,
and job output in Lustre, especially if your jobs are I/O intensive.

The most relevant storages are:

- scratch
	- `/home`
	- backed up
	- Quota: Max 300 GB per user (Please confirm).
- physics
	- 126 TB
	- not backed up
- physics2
	- 284 TB
	- not backed up
- lustre:
	- 42 TB
	- Not backed up
	- shared with the Warp cluster

 
## Useful Commands

Running `df -h` will show you the current usage for all the drives in human-readable terms, if you’ve got a large data set and you’re trying to figure out which of the data-type drives to use.

Running `du -h` shows the size of directory and sub-directories. `du -hs` gives the total size of current directory + sub-directories (summary only).  This can be slow on some drives depending on filesystem (should be fine on `/home`, may be slow on `/physics`).


## Lustre-specific Commands

The Lustre drives (`physics`, `physics2`, and `lustre`) have certain commands that allow for optimizing the storage of large data files. One particular set of commands is knows as the striping of files and directories. It essentially controls how many different disks the file is stored across. In general, you should shoot for a maximum of ~50 GB/stripe in order to facilitate reading and writing of large files. When creating new files, the filesystem defaults to a stripe number of 4. This means that for files smaller than ~200 GB, no action is necessary. You must stripe files before they are created, or you can stripe a whole directory before you write files to it. You can view the current striping information via the command:

```console
user@local:~$ lfs getstripe <filename>
```

This shows the current striping information for the file. If you would like to retrieve the striping information for a directory, you should add the `-d` option to the command:

```console
user@local:~$ lfs getstripe -d <directory>
``` 

In order to change the striping, you can use the setstripe command. For instance, to create a new file and set its stripe number to 16, you would execute:

 
```console
user@local:~$ touch newfile.dat
user@local:~$ lfs setstripe -c 16 newfile.dat
```

Alternatively, if you do not know a priori what the file names will be, or will produce many output files in the same directory, the striping can be done at the level of the directory:

 
```console
user@local:~$ mkdir output_directory
user@local:~$ lfs setstripe -c 16 output_directory
```

This ensures that all (newly created) files in `output_directory` will be appropriately striped.