from getpass import getpass

ssh_password = getpass("Bitte Passwort eingeben : ")

cisco3 = {
    "device_type": "cisco_ios",
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": ssh_password,
}

arista1 = {
    "device_type": "arista_eos",
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": ssh_password,
    "global_delay_factor": 4,
}

arista2 = {
    "device_type": "arista_eos",
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": ssh_password,
    "global_delay_factor": 4,
}

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": ssh_password,
}

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": ssh_password,
}

device_list = [cisco3, arista1, arista2, nxos1]

