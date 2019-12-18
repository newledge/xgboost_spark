import sys
import time
import pandas as pd
import numpy as np
#from start_pyspark import spark, sc, sqlContext
import pyspark.sql.types as typ
import pyspark.ml.feature as ft
from pyspark.sql.functions import isnan, isnull
from pyspark.sql.session import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars xgboost4j-spark-0.72.jar,xgboost4j-0.72.jar pyspark-shell'
#import findspark
#findspark.init()
input=sys.argv[1]
#output=sys.argv[2]

conf = SparkConf().setMaster("spark://master:7077").setAppName("xgb").set('spark.cores.max', 32).set("spark.executor.cores", '4')
sc = SparkContext(conf = conf)

spark = SparkSession\
        .builder\
        .master("spark://master:7077") \
        .config('spark.cores.max', 32) \
        .appName("PySpark XGBOOST Titanic")\
        .getOrCreate()
import pyspark
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
from pyspark.sql.functions import col

spark.sparkContext.addPyFile(".../xgboost_script/sparkxgb.zip")
from sparkxgb import XGBoostEstimator
from pyspark.ml.classification import LogisticRegression
