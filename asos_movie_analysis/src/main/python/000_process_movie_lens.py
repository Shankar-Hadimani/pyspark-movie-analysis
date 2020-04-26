from pyspark.sql import functions as F
import configparser as cp

import sys

# initialise configuration file
read_cfg = cp.RawConfigParser()
read_cfg.read(r"src\main\resource\config\config-dev.ini")

# assign arguments
env_name = sys.argv[1]

# read configuration properties
print(read_cfg.get(env_name,"execution.mode"))



