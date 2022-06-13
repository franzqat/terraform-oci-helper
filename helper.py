import argparse


def parse_line(line):
    """
    Parse the text line

    Args:
        line (string): string to be parsed

    Returns:
        string: string without spaces, \0 characters and split by "|" character.
    """
    return line.strip().split('|')


def write_instance_config(file, count, new_list, public_ip=False):
    """
    This function writes the yml configuration file for instances based on input file
    
    The structure follows the index order below.
    NAME|IP| PublicIP|Shape|OCPU count| Memory | AD|  FD | DISK(GB) |Tag|
    1    2    3       4       5           6       7   8       9       10

    Args:
        file (file): output file
        count (integer): counter to start the instance number from. It's just a indicator in the yaml file. Not used in terraform. eg. #1
        new_list (list of strings): list of text lines with instances informations
        public_ip (bool, optional): Enable public ip. For VMs not belonging to K8s Cluster. Defaults to False.
    """
    
    file.write('#' + str(count) + '\n')
    file.write('- display_name: ' + new_list[1] + '\n')
    file.write('  availability_domain: jfxe:EU-FRANKFURT-1-AD-' +
               new_list[7].split('-')[1] + '\n')
    file.write('  fault_domain: FAULT-DOMAIN-' +
               new_list[8].split('-')[1] + '\n')
    file.write('  hostname_label: ' + new_list[1] + '\n')
    file.write('  private_ip: ' + new_list[2] + '\n')
    file.write('  shape: ' + new_list[4] + '\n')
    file.write('  memory_in_gbs: ' + new_list[6] + '\n')
    file.write('  ocpus: ' + new_list[5] + '\n')
    file.write('  boot_volume_size_in_gbs: ' + new_list[9] + '\n')
    if public_ip:
        file.write('  assign_public_ip: true\n')  # not for kubernetes
    else:
        file.write('  assign_public_ip: false\n')  # not for kubernetes
    file.write('  freeform_tag: ' + new_list[10] + '\n')


def write_volume_config(file, count, new_list):
    """
    This function writes the yml configuration file for volumes based on input file

    Args:
        file (file): output file
        count (integer): counter to start the instance number from. It's just a indicator in the yaml file. Not used in terraform. eg. #1
        new_list (list of strings): list of text lines with volumes informations
    """
    file.write('#' + str(count) + '\n')
    file.write('- display_name: ' + new_list[1] + '\n')
    file.write('  size_in_gbs: ' + str(new_list[2]) + '\n')
    file.write('  vpus_per_gb: ' + str(new_list[3]) + '\n')
    file.write('  attached_to: ' + new_list[5] + '\n')
    file.write('  application: ' + new_list[6] + '\n')

def write_sl_config(file, count, new_list):
    """
    This function writes the yml configuration file for security list based on input file

    Args:
        file (file): output file
        count (integer): counter to start the ID from.
        new_list (list of strings): list of text lines with volumes informations
    """
    file.write('- description: ' + new_list[1] + '\n')
    file.write('  id: '          + str(count) + '\n')
    file.write('  icmp_options: []\n')
    file.write('  protocol: 6\n')
    file.write('  source: ' + new_list[2] + '\n')
    file.write('  source_type: CIDR_BLOCK\n')
    file.write('  stateless: false\n')
    file.write('  tcp_options:\n')
    file.write('  - max: ' + new_list[4] + '\n')
    file.write('    min: ' + new_list[3] + '\n')
    file.write('  udp_options: []\n')


def main():
    parser = argparse.ArgumentParser(
        description='Create config yml file from resources in tab.md file.\
        Copy the resources from the tab that you want to generate from README file into tab.md, then\
        launch the script selecting the correct type and the counter that you wish to start from')

    parser.add_argument("-t", "--type", help="instance type: volume, instance, security-list")
    parser.add_argument(
        "-c", "--count", help="counter to start the instance number from. It's just a indicator in the yaml file. Not used in terraform. eg. #1")
    args = parser.parse_args()

    new_list = []
    count = int(args.count)

    with open('outfile.yml', 'w') as file, open('tab.md', 'r') as read_file:
        lines = read_file.readlines()
        for line in lines:
            ls = parse_line(line)
            for l in ls:
                l = l.strip()
                new_list.append(l)
            print(new_list)
            if args.type == "instance":
                write_instance_config(file, count, new_list)
            elif args.type == "volume":
                write_volume_config(file, count, new_list)
            elif args.type == "security-list":
                write_sl_config(file, count, new_list)
            else:
                print('Wrong type choice')
                break
            new_list = []
            count += 1


if __name__ == "__main__":
    main()
