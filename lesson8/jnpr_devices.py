from getpass import getpass

username = "pyclass"
password = getpass("Bitte Passwort eingeben : ")

# Dictionary to define each SRX device
srx2 = {"host": "srx2.lasthop.io", "user": username, "password": password}

# List of the SRX devices
junos_devices = [srx2]

