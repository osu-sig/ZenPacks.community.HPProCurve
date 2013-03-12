from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HPProCurve(SnmpPlugin):
    snmpGetTableMaps = (
        GetTableMap(
            'sensorTable', '1.3.6.1.4.1.11.2.14.11.1.2.6.1', {
                '.1': 'sensorIndex',
                }
            ),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        sensors = results[1].get('sensorTable', {})

        log.info("sensor_count is %d", len(sensors.keys()))

        return self.objectMap({
            'sensor_count': len(sensors.keys()),
            })
