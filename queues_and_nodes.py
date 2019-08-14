"""
"""

from __future__ import print_function
from slurm_utils import get_nodes_dict, get_partitions_dict
import numpy as np
import datetime

def main():

    node_dict = get_nodes_dict()
    nodes = node_dict.keys()
    nodes.sort()

    partition_dict = get_partitions_dict()
    partitions = partition_dict.keys()
    partitions.sort()

    output_file  = open('queues_and_nodes.md', 'w')

    output_file.write("# Queues & Nodes \n")
    output_file.write("\n")
    output_file.write("\n")

    line = ("This page contains information on the current queues and nodes installed on the Coma cluster. \n")
    output_file.write(line)
    output_file.write("\n")

    now = datetime.datetime.now()
    date = str(now.month) + '/' + str(now.day) + '/' + str(now.year)

    line = ("This page was last populated on: " + date )
    output_file.write(line)
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("## Queues \n")
    output_file.write("\n")
    output_file.write("\n")

    line = ("Below is a list of the current queues Coma, including the number of nodes,\
             and the time limit for jobs. \n")
    output_file.write(line)
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("Queue | Number of Nodes | Time Limit [days-hours:minutes:seconds] \n")
    output_file.write("----- | --------------- | --------------------------------------- \n")
    for queue in partitions:
        n_nodes = partition_dict[queue]['NODES']
        time_limit = partition_dict[queue]['TIMELIMIT']
        line = " ".join([queue, "|", str(n_nodes), "|", time_limit, "\n"])
        output_file.write(line)
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("## Nodes \n")
    output_file.write("\n")
    output_file.write("\n")

    line = ("Below is a list of the current nodes installed on Coma, including the number of processors,\
             amount of memory, CPU architecture, and queue(s) to which they belong. \n")
    output_file.write(line)
    line = ("More information on a specific node can be retrieved with the following command: \n")
    output_file.write(line)
    output_file.write("\n")
    output_file.write("```console \n")
    output_file.write("user@local:~$ scontrol show node [NODE_NAME] \n")
    output_file.write("``` \n")
    output_file.write("\n")
    output_file.write("\n")

    output_file.write("Node | Number of Processors | Total Memory | CPU Architecture | Queues \n")
    output_file.write("---- | -------------------- | ------------ | ---------------- | ------ \n")
    for node in nodes:
        n = int(np.ceil(np.log10(int(node_dict[node]['RealMemory']))/np.log10(2)))
        mem = (2**n)/1024
        if 'amd' in node_dict[node]['AvailableFeatures']:
            cpu = 'AMD'
        elif 'intel' in node_dict[node]['AvailableFeatures'][0]:
            cpu = 'Intel'
        else:
            print(node_dict[node]['AvailableFeatures'])
            cpu = 'unknown'
        try:
            queues = ', '.join(node_dict[node]['Partitions'])
        except KeyError:
            queues = 'none'

        line = " ".join([node, "|", node_dict[node]['CPUTot'], "|", str(mem), "|", cpu, "|", queues, "\n"])
        output_file.write(line)

    output_file.write("\n")
    output_file.write("\n")
    line = ("This page was created by running the `queues_and_nodes.py` script on Coma. \n")
    output_file.write(line)


if __name__ == "__main__":
    main()
