from Products.ZenModel.Device import Device

class HPProCurveDevice(Device):
    sensor_count = None

    _properties = Device._properties + (
        {'id': 'sensor_count', 'type': 'int'},
        )
