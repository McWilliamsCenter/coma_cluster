"""
"""

import subprocess
import re

cluster_name = 'coma'

def get_nodes_dict():
    """
    return dictionary whose keys are the node names and whose entries are dictionaroes of properties
    """

    result = subprocess.check_output(['scontrol', 'show', 'node']).strip()
    node_entries = re.split(r'\n\n', result)

    node_dict = {}

    for node_entry in node_entries:

        # split by new lines or spaces
        node_entry = re.split(r'\n|\s+', node_entry)
        # remove empty lines
        node_entry = [x for x in node_entry if x != '']

        try:
            node_name = node_entry[0].split('=')[1]

            # skip head node
            if node_name == cluster_name:
                pass
            else:
                # check if node is in dict
                if node_name in node_dict.keys():
                    pass
                else:
                    node_dict[node_name] = {}

                # add node properties to node entry in dict
                for prop in node_entry[1:]:
                    try:
                        key, value = prop.split('=', 1)
                        try:
                            node_dict[node_name][key] = value
                        except KeyError:
                            pass
                            #print(node_name, key, value)
                    except ValueError:
                        pass
                        #print(node_name, prop)
        except IndexError:
            print(node_entry)

    # further process some property dictionaries
    nodes = node_dict.keys()
    for node in nodes:

        # partitions
        try:
            partition_list = node_dict[node]['Partitions']
            partition_list = partition_list.split(',')
            node_dict[node]['Partitions'] = partition_list
        except KeyError:
            pass

        try:
            # active features
            features_list = node_dict[node]['ActiveFeatures']
            features_list = features_list.split(',')
            node_dict[node]['ActiveFeatures'] = features_list

            # available features
            features_list = node_dict[node]['AvailableFeatures']
            features_list = features_list.split(',')
            node_dict[node]['AvailableFeatures'] = features_list
        except KeyError:
            pass

        # CfgTRES
        try:
            l = node_dict[node]['CfgTRES']
            l = l.split(',')
            d = {}
            for ll in l:
                key, value = ll.split('=', 1)
                d[key]=value
            node_dict[node]['CfgTRES'] = d
        except KeyError:
            pass

        # AllocTRES
        try:
            l = node_dict[node]['AllocTRES']
            l = l.split(',')
            d = {}
            for ll in l:
                try:
                    key, value = ll.split('=', 1)
                    d[key]=value
                except ValueError:
                    pass
            node_dict[node]['AllocTRES'] = d
        except KeyError:
            pass

    return node_dict


def get_partitions_dict():
    """
    return dictionary whose keys are the partitions with entries which are dictionaries of properties
    """

    # read in 'sinfo output'
    result = subprocess.check_output(['sinfo'])
    lines = result.split('\n')
    colnames = lines[0].split()

    partition_dict = {}

    for line in lines[1:-1]:

        # remove * from partition name
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

    # populate node list for each partition entry
    result = subprocess.check_output(['sinfo', '-N']).strip()
    lines = result.split('\n')

    for line in lines[1:-1]:
        node_name = line.split()[0]
        partition = line.split()[2].strip('*')
        state = line.split()[3].strip('*')
        partition_dict[partition]['NODELIST'].append(node_name)

    return partition_dict
