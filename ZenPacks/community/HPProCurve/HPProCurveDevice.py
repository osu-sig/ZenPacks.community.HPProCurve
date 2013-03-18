from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class HPProCurveDevice(Device):
    sensor_count = None

    _properties = Device._properties + (
        {'id': 'sensor_count', 'type': 'int'},
        )

    _relations = Device._relations + (
    ('sensors', ToManyCont(ToOne,
        'ZenPacks.community.HPProCurve.Sensor',
        'sensor_device',
        )),
    )
