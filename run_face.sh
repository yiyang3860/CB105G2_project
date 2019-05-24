#!/bin/bash
docker exec -i proj_g2_kafka_1 kafka-topics --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test9

docker exec -d proj_g2_facerecog_1 python image_comsumer_kafka.py
docker exec -d proj_g2_facerecog_1 python find_face_in_Dir.py
