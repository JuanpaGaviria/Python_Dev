from Simulator.simulator import Device
from Metering.random_id import rand_id
from Metering.random_voltage import rand_voltage
from Metering.random_timestamp import fun_timestamp


id = rand_id(7, "AEIOU12")  # Generates a random id
electronic_device = Device(id)  # Instanciates Device class

while 1:  # Infinite loop to generate randomly the meterings for the specified object
    voltage = rand_voltage()  # Calls voltage random generator function
    timestamp = fun_timestamp()  # Calls timestamp function
    electronic_device.random_metering(voltage, timestamp)  # Method that adds the atributes to the object
    
