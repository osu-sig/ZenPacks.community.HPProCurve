from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class Sensor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'HPProCurveSensor'

    status = None
    description = None
    warnings = None
    failures = None

    _properties = ManagedEntity._properties + (
        {'id': 'status', 'type': 'int'},
        {'id': 'description', 'type': 'string'},
        {'id': 'warnings', 'type': 'int'},
        {'id': 'failures', 'type': 'int'},
        )

    _relations = ManagedEntity._relations + (
        ('sensor_device', ToOne(ToManyCont,
            'ZenPacks.community.HPProCurve.HPProCurveDevice',
            'sensors',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.sensor_device()

    def getRRDTemplateName(self):
        return 'Sensor'
