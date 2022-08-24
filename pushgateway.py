from prometheus_client import push_to_gateway,CollectorRegistry,Gauge
import random
import time

registry=CollectorRegistry()

gauge=Gauge('number_of_records_processed','Number of records processed every run by the job',registry=registry)

while(True):
    random_count=random.random()*100000
    gauge.set(random_count)
    time.sleep(1)
    if(random_count==4020):
        break
    push_to_gateway('http://localhost:9091/',job="data_processor",registry=registry)