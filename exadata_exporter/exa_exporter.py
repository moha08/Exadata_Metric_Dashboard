import time
import list_of_commands
import subprocess
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from flask import Flask

# import the prometheus modules which we need
from prometheus_client import start_http_server, REGISTRY
from prometheus_client.core import GaugeMetricFamily


class ExadataCollector():
    def __init__(self):
        pass

    def collect(self):
        # call database metrics
        yield GaugeMetricFamily('Exadata', 'Exadata metrics')

        # loop in all Exadata metric families
        for exa_command in list_of_commands.Command.Commands:
            yield self.getExaMetrics(exa_command['osCommand'], exa_command['metricFamilyName'], exa_command['metricFamilyDesc'],
                                     exa_command['metricObjName'])

    # method get exadata metrics for database nodes and storage nodes
    def getExaMetrics(self, osCommand, metricFamilyName, metricFamilyDesc, metricObjName):

        out = subprocess.Popen(osCommand, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        stdout, stderr = out.communicate()
        # read output command and make some data cleansing
        dt = stdout.decode()
        lst = list(item.split(",")
                   for item in dt.replace("b'", "").replace("'", "").split('\n'))
        # create  metrics family for metrics
        counterFamily = GaugeMetricFamily(metricFamilyName, metricFamilyDesc, labels=[
                                          'node', 'object_name', 'metric_name'])
        for items in lst[:-2]:
            server = items[0]
            metricName = items[1]

            if metricObjName in ["HOSTINTERCONNECT", "GRIDDISK"]:
                metricObjectName = server
                metricValue = items[2]
            else:
                metricObjectName = items[2]
                metricValue = items[3]

            counterFamily.add_metric(
                [server, metricObjectName, metricName], metricValue)

        return counterFamily


if __name__ == "__main__":
    REGISTRY.register(ExadataCollector())

    app = Flask(__name__)
    app_dispatch = DispatcherMiddleware(
        app, {'/metrics': make_wsgi_app(REGISTRY)})
    start_http_server(9132)

while True:
    time.sleep(10)
