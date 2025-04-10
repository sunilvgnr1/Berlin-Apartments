from functools import partial
from mac_notifications import client

if __name__ == "__main__":
    client.create_notification('new listing is found')   
    