from opcua import Client
from IPython import embed

class SubHandler(object):

    """
    Subscription Handler. To receive events from server for a subscription
    data_change and event methods are called directly from receiving thread.
    Do not do expensive, slow or network operation there. Create another 
    thread if you need to do such a thing
    """
    def event_notification(self, event):
        print("New event notification", event)
        # To print only the notification message
        #print("Write whatever you want here", event.Message.Text)


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    try:
        client.connect()

        root = client.get_root_node()
        print("Objects node is: ", root)
        # Now getting a variable node using its browse path
        obj = root.get_child(["0:Objects", "2:MyObject"])
        print("MyObject is: ", obj)

        # Get the custom event type
        myevent = root.get_child(["0:Types", "0:EventTypes", "0:BaseEventType", "2:MyFirstEvent"])
        print("MyFirstEventType is: ", myevent)

        msclt = SubHandler()
        sub = client.create_subscription(100, msclt)
        handle = sub.subscribe_events(obj, myevent)

        #embed()
        #sub.unsubscribe(handle)
        #sub.delete()
    finally:
client.disconnect()
