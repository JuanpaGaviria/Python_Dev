
class Device:

    def __init__(self, id):
        self.id = id
        self.voltage = None
        self.timestamp = None
        
    def random_metering(self, voltage, timestamp):
        self.voltage = voltage
        self.timestamp = timestamp
        
