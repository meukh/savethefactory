# CTF challenge: Save the Factory!

**Save the Factory** is an OT(Operational Technology)/IoT oriented challenge focusing on the industrial communication protocol *OPC Unified Architecture* that is becoming widely adopted in the industry. 

This challenge was originally made for the [*Ph0wn CTF*](https://ph0wn.org/) for its 2018's edition.

The challenge is divided to two parts with a timer where teams/players have to connect to an opcua server, explore its information model (data in the tree graph), subscribe ro certain nodes, receive notifications from the server and interpret some hints to solve the challenge and retrieve the flags. The main difficulty lies in learning how to write an OPC-UA client that talks with to the server and modifies its data.

# How to use this?

## Deploying the challenge on a CTF server
This only requires [*Docker*](https://www.docker.com/) to be installed on your server machine. Clone or download the files in this repository to your machine, then you can follow the instructions below to set it up.

Once the container is up and running, you can log in as root to add new players and start a new challenge instance for each one of them. The ssh port number and password and the number of exposed ports, among other things, are random and meant as guidelines only. The helper scripts, the Dockerfile as well as the description of the challenge should be easy to read, understand and modify to fit your needs. 

### Set up:
#### Building and running the docker:
```
~$ docker build -t opcua-challenge "/directory/to/Dockerfile"
~$ docker run -d -p 6666:22 -p 6100-6300:6100-6300 --name savethefactory opcua-challenge 
```
`6666`: port number chosen to ssh to the container.

`6100-6300`: range of container's ports to be published and mapped to the range `6100-6300` of the host's ports.

If the host ports are not the same as the container ports then use `docker port` to check the actual ports' mapping.

To use a different range of ports, modify the challenge's server port in the `add_player.sh` script. 

Alternatively, it's possible to only modify the Makefile then run:
```
~$ make build
~$ make run
``` 
And to stop it and remove the image:
```
~$ make stop
``` 

#### Adding a team:
Log in to the container as root:
```
~$ ssh root@"HOST_IP_ADDRESS" -p "SSH_PORT"
~$ cd /challenger/
~$ ./add_player.sh
```

The script will print out the username and the port at which the challenge's server will be listening.

The `.shadow` and `.used_ports` files will be automatically updated.

* `.shadow` contains a list of usernames, user number and their passwords in plain text.

```
USER_NUMBER 	USERNAME:PASSWORD
```

* `.used_ports` is there to track the teams' usernames and the assigned port number for the challenge.

Its lines follow a similar format.
```
USER_NUMBER 	USERNAME:PORT_NUMBER
```

### Description of the challenge:
All the necessary information needed to solve the challenge can be found [here](https://github.com/meukh/savethefactory/tree/master/public). It contains a description of the challenge's scenario that teams/players must be provided with. It describe what they are expected to do in both parts ([part1](https://github.com/meukh/savethefactory/tree/master/public/description.savethefactory.md), [part2](https://github.com/meukh/savethefactory/tree/master/public/description.trackthehacker.md)) and how they should go about it.


## Playing on your local machine
This challenge hasn't been made for this purpose, but for the sake of trying it out you can follow the set up instructions to build/run the container and adding a team, then you can ssh to the container again using the newly-added user credentials.

```
~$ ssh "USERNAME"@"HOST_IP_ADDRESS" -p "SSH_PORT"

```

Or, if you don not wish to get a shell acess you can directly connect to the challenge's OPC-UA server at: `opc.tcp://HOST:PORT_NUMBER/FearFactory/supervision_unit`

* `HOST_IP_ADDRESS`: `localhost` or `127.0.0.1`

* `PORT_NUMBER`: Should be in `.used_ports` after running the script `add_player.sh`
