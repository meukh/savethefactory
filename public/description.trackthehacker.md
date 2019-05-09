# Track the Hacker

Title: Track the Hacker
Category: OT
Difficulty: Intermediate
Author: m0eukh

*This challenge shares the same settings as challenge Save The Factory. It is probably easier to solve first "Save the Factory" then this one, though this is not mandatory and up to you!*

*FearFactory* is an industrial factory where most of the sensitive units are remotely supervised and controlled by one **main board**.
The communication between the **main board** and the rest of the physical equipment (OTs, machines, sensors, ...) is done using the **OPC-UA protocol**.
This is a client-server style protocol to tranfer data between all kinds of controls, monitoring devices and sensors that interact with real world data. An OPC-UA server is installed on the main board.

Due to a misconfiguration of access rights, a **smart hacker managed to gain access to the server and mess it up**. He found a tricky way to store some data (probably a file, or something for later use?) in the tree graph of the OPC-UA server.

It seems he had to stop what he was doing abruptly and didn't have enough time to clean up his traces.

Can you retrieve what the data he has exfiltrated to see if it can lead us back to him?

- OPC-UA URL path: `opc.tcp://HOST:PORT/FearFactory/supervision_unit`
- Port: get `PORT` for your team at the organizer's desk.

Do not use another port on the factory. This won't help you. Teams intentionally causing havoc will be banished :=)

**Shell access:**

If you wish to get a shell on the Factory, **come and get one at the organizer's desk**:

- SSH Port: `6666`
- Username: *supplied at the organizer's desk*
- Password: *supplied at the organizer's desk*

OPC-UA:

- **Connect** an OPC UA client to the factory's server at address.
- **Subscribe** to notifications of the `MainBoard` to receive alerts
- We provide a **Python OPC-UA script** `client_example.py` to help your first steps for this challenge. This script uses [FreeOpcUa](https://github.com/FreeOpcUa/python-opcua). You can find more documentation on FreeOpcUa, such as [example subscribing to a node](https://github.com/FreeOpcUa/python-opcua/blob/master/examples/client-example.py), [minimal client example](https://github.com/FreeOpcUa/python-opcua/blob/master/examples/client-minimal.py), [node class](https://python-opcua.readthedocs.io/en/latest/node.html), [client class](https://python-opcua.readthedocs.io/en/latest/client.html)
- Don't forget to inspect the contents of the **black box** to see if there are any interesting logs :)
