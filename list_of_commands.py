class Command(object):
    Commands = [
        # CELL metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricObjectName,metricValue where objecttype='CELL' and metricType !='cumulative' \" | awk '{print $1 \",\" $2 \",\" $3 \",\" $4}'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataCELLMetrics',
            "metricFamilyDesc" : 'Exadata CELL metrics',
            "metricObjName" : 'CELL'
        },
        #CELL Disk metrics
        {
            #"osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricValue where objecttype='CELLDISK' and metricType !='cumulative'\"  |  awk '{gsub(\",\",\".\",$4); a[$1\",\"$2]+=$4}END{for(i in a) print i \",\" a[i]}' | sed  's/://g'",
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricObjectName,metricValue where objecttype='CELLDISK' and metricType !='cumulative' \" | awk '{gsub(\",\",\"\",$4); print $1 \",\" $2 \",\" $3 \",\" $4}'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataCELLDISKMetrics',
            "metricFamilyDesc" : 'Exadata CELLDISK metrics',
            "metricObjName" : 'CELLDISK'
        },
        # GRIDDISK metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list griddisk attributes name,asmModeStatus \" | awk '{gsub(\",\",\"\",$3); $4= $3==\"ONLINE\" ? 0 : 1; print $1 \",\" $2 \",\" $4 }'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataGRIDDISKMetrics',
            "metricFamilyDesc" : 'Exadata Grid Disks Metrics',
            "metricObjName" : 'GRIDDISK'
        }, 
        #FLASHCACHE metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricObjectName,metricValue where objecttype='FLASHCACHE' and metricType !='cumulative' \" | awk '{gsub(\",\",\"\",$4); print $1 \",\" $2 \",\" $3 \",\" $4}'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataFLASHCACHEMetrics',
            "metricFamilyDesc" : 'Exadata FLASHCACHE metrics',
            "metricObjName" : 'FLASHCACHE'
        },
        # HOST_INTERCONNECT metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricValue where objecttype='HOST_INTERCONNECT' and metricType !='cumulative' \" |  awk '{gsub(\",\",\".\",$3); a[$1\",\"$2]+=$3}END{for(i in a) print i \",\" a[i]}' | sed  's/://g'",
            "metricFamilyName" : 'ExadataHOSTINTERCONNECTMetrics',
            "metricFamilyDesc" : 'Exadata HOSTINTERCONNECT metrics',
            "metricObjName" : 'HOSTINTERCONNECT'
        },
        # PLUGGABLE DATABASE I/O metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricObjectName,metricValue where objecttype='IORM_PLUGGABLE_DATABASE' and metricType !='cumulative' \" | awk '{gsub(\",\",\"\",$4);gsub(\"MOE.\",\"\",$3); print $1 \",\" $2 \",\" $3 \",\" $4}'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataPLUGGABLEDBEMetrics',
            "metricFamilyDesc" : 'Exadata PLUGGABLE DB metrics',
            "metricObjName" : 'PLUGGABLEDB'
        }, 
        # PLUGGABLE DATABASE I/O metrics
        {
            "osCommand" : "dcli -g /root/db_group -l root dbmcli -e \"list metriccurrent attributes name,metricObjectName,metricValue\" | awk '{print $1 \",\" $2 \",\" $3 \",\" $4}' | sed  's/://g'",
            "metricFamilyName" : 'ExadataDBNodeMetrics',
            "metricFamilyDesc" : 'Exadata DB Nodes metrics',
            "metricObjName" : 'DBMETRICS'
        },
        # SMARTIO metrics
        {
            "osCommand" : "dcli -g /root/cell_group -l root cellcli -e \"list metriccurrent attributes name,metricObjectName,metricValue where objecttype='SMARTIO' and metricType !='cumulative' \" | awk '{gsub(\",\",\"\",$4);gsub(\"MOE.\",\"\",$3); print $1 \",\" $2 \",\" $3 \",\" $4}'   | sed  's/://g'",
            "metricFamilyName" : 'ExadataDBNodeMetrics',
            "metricFamilyDesc" : 'Exadata DB Nodes metrics',
            "metricObjName" : 'DBMETRICS'
        }                       
        ];

