(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HPProCurveSensor',
    _t('Sensor'),
    _t('Sensors'));

ZC.HPProCurveSensorPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HPProCurveSensor',
            autoExpandColumn: 'description',
            sortInfo: {
                field: 'description',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'description'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'warnings'},
                {name: 'failures'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'description',
                dataIndex: 'description',
                header: _t('Name'),
                sortable: true
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                sortable: true,
                width: 60
            },{
                id: 'warnings',
                dataIndex: 'warnings',
                header: _t('Warnings'),
                sortable: true,
                width: 60 
            },{
                id: 'failures',
                dataIndex: 'failures',
                header: _t('Failures'),
                sortable: true,
                width: 60
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.HPProCurveSensorPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HPProCurveSensorPanel', ZC.HPProCurveSensorPanel);

})();
