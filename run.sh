#!/bin/bash

docker exec -i proj_g2_kafka_1 kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test10

#docker exec proj_g2_yolov3_1 bash -c "python image_comsumer_kafkaV1.py"
#docker exec proj_g2_yolov3_1 bash -c "python detectfileV4.py"
docker-compose exec -d yolov3 python image_comsumer_kafkaV1.py
docker-compose exec -d yolov3 python detectfileV4.py
#docker exec -it proj_g2_yolov3_1 sh -c "sh yolov3start.sh"
#docker exec proj_g2_yolov3_1 bash -c "bash yolov3start.sh"
