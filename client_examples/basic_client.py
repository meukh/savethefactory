from opcua import Client


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Objects node is: ", root)

        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())
        # List a node's children names. 
        for child in root.get_children():
            print(child.get_browse_name().Name)

        # Same thing could be done with values if it is supported by the children nodes' types.
        # (i.e some types do not have a value)
        #for var in node.get_children():
        #    print(var.get_value())

        # get a specific node knowing its node id
        var = client.get_node("ns=3;i=2002")
        print(var)

        var.get_value() # get value of node as a python builtin
        var.set_value(3.9) # set node value using implicit data type

        # Now getting a variable node using its browse path
        myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
        # The name space can be omitted if it is equal to 0. The line above is equivalent to:
        myvar = root.get_child("Objects").get_child("2:MyObject").get_child("2:MyVariable")

        obj = root.get_child(["0:Objects", "2:MyObject"])
        print("myvar is: ", myvar)
        print("myobj is: ", obj)


    finally:
        client.disconnect()
