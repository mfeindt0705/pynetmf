from netmiko import ConnectHandler
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

def show_version(device):
    net_connect = ConnectHandler(**device)
    # send show version and wait for prompt
    output = net_connect.send_command_expect("show version")
    net_connect.disconnect()
    return output


def show_version2(device):
    """Execute show version command using Netmiko."""
    print()
    print("#" * 80)
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command_expect("show version")
    net_connect.disconnect()
    print(output)
    print("#" * 80)
    print()


def ssh_command(device, show_command):
    net_connect = ConnectHandler(**device)
    # send show command and wait for prompt
    output = net_connect.send_command_expect(show_command)
    net_connect.disconnect()
    return output

def ssh_command2(device, show_command):
    """Establish an SSH connection. Execute show command, return results."""
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command(command)
    net_connect.disconnect()
    print("\n")
    print("-" * 20)
    print(output)
    print("-" * 20)
    print("\n")
    return

