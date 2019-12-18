#!/bin/bash

HADOOP_HOME=/work/opt/hadoop-2.9.1/
hadoop_home=/work/opt/hadoop-2.9.1//bin
streaming_home=/work/opt/hadoop-2.9.1/share/hadoop/tools/lib

input=".../sample_test_fenci_vec/"
root=".../xgboost_script"
spark_home=/work/opt/spark
export CURRENT=file:.../xgboost_script




$spark_home/bin/spark-submit  \
  --jars ${root}/xgboost4j-0.72.jar \
  --jars ${root}/xgboost4j-spark-0.72.jar \
  $CURRENT/xgboost_all.py ${input}
