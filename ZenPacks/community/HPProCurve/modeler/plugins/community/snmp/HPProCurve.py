from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HPProCurve(SnmpPlugin):
    relname = 'sensors'
    modname = 'ZenPacks.community.HPProCurve.HPProCurveSensor'

    snmpGetTableMaps = (
        GetTableMap(
            'sensorTable', '1.3.6.1.4.1.11.2.14.11.1.2.6.1', {
                '.1': 'sensorIndex',
                '.4': 'sensorStatus',
                '.5': 'sensorWarnings',
                '.6': 'sensorFailures',
                '.7': 'sensorDescr',
                }
            ),
        )

    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)

        sensors = results[1].get('sensorTable', {})

        log.info("sensor_count is %d", len(sensors.keys()))

        rm = self.relMap()
        for snmpindex, row in sensors.items():
            sensorindex = row.get('sensorIndex')
            log.info("processing sensor %d", sensorindex)

            rawstatus = row.get('sensorStatus')
            if rawstatus == 5:
                log.info("sensor %d not present, skipping", sensorindex)
                continue
            elif rawstatus == 4:
                status = 'good'
            elif rawstatus == 2:
                status = 'bad'
            elif rawstatus == 3:
                status = 'warning'
            elif rawstatus == 1:
                status = 'unknown'
            else:
                status = ''

            rm.append(self.objectMap({
                'id': self.prepId(sensorindex),
                'title': row.get('sensorDescr'),
                'snmpindex': snmpindex.strip('.'),
                'status': status,
                'warnings': row.get('sensorWarnings'),
                'failures': row.get('sensorFailures'),
                'description': row.get('sensorDescr'),
                }))

        log.info("finished processing sensors")
        return rm
