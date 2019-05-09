# Save the Factory

Title: Save The Factory
Category: OT
Difficulty: Intermediate
Author: m0eukh

*This challenge shares the same settings as challenge "Track The Hacker". It is probably easier to solve first "Save the Factory" then "Track The Hacker", though this is not mandatory and up to you!*

*FearFactory* is an industrial factory where most of the sensitive units are remotely supervised and controlled by one **main board**.
The communication between the **main board** and the rest of the physical equipment (OTs, machines, sensors, ...) is done using the **OPC-UA protocol**.
This is a client-server style protocol to tranfer data between all kinds of controls, monitoring devices and sensors that interact with real world data. An OPC-UA server is installed on the main board. 

Due to a misconfiguration of access rights, a **smart hacker managed to tamper with the server's data and send random requests to nodes**.
As each of those nodes are connected to real OT devices, **this represents a real safety hazard to the factory!!!**.

Can you save the factory (and its workers) in time and reset tampered nodes to normal operating values?


**Factory credentials:**

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



