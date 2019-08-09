"""
"""

from __future__ import print_function
import subprocess
import re

def main():

    # read in 'sinfo output'
    result = subprocess.check_output(['sinfo'])
    lines = result.split('\n')
    colnames = lines[0].split()

    partition_dict = {}
    for line in lines[1:-1]:
        partition = line.split()[0].strip('*')
        avail = line.split()[1]
        time_limit = line.split()[2]
        num_nodes = int(line.split()[3])
        state = line.split()[4].strip('*')
        partition_dict[partition] = {'AVAIL': avail,
                                     'TIMELIMIT': time_limit,
                                     'NODES': num_nodes,
                                     'STATE': state,
                                     'NODELIST': []}

    result = subprocess.check_output(['sinfo', '-N']).strip()
    lines = result.split('\n')

    node_dict = {}
    for line in lines[1:-1]:
        node_name = line.split()[0]
        partition = line.split()[2].strip('*')
        state = line.split()[3].strip('*')
        node_dict[node_name] = {'PARTITION': partition, 'STATE': state}
        partition_dict[partition]['NODELIST'].append(node_name)

    result = subprocess.check_output(['scontrol', 'show', 'node']).strip()
    # node_entries = result.split('\n\n')
    node_entries = re.split(r'\n|,', result)

    for node_entry in node_entries:
        node_entry = re.split(r'\n|\s+', node_entry)
        node_entry = [x for x in node_entry if x != '']
        try:
            node_name = node_entry[0].split('=')[0]
            for prop in node_entry[1:]:
                try:
                    key, value = prop.split('=')
                    print(node_name, key, value)
                    node_dict[node_name][key] = value
                except ValueError:
                    print('     ', prop)
        except IndexError:
            print(node_entry)

if __name__ == "__main__":
    main()
