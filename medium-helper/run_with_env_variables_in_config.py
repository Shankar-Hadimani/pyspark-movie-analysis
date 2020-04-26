# To run this:
# export DB_PASS=very_secret_and_complex 
# python use_env_variables_in_config_example.py -c /path/to/yaml
# do stuff with conf, e.g. access the database password like this: conf['database']['DB_PASS']
import argparse
from yaml_environment_variable_reader import parse_config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='script to execute config with env')
    parser.add_argument( "-c", "--conf", action="store",dest="config_file", help="path to the configuration file")
    args = parser.parse_args()
    conf = parse_config(path=args.config_file)

    print("testing environment variable reader..............!!!")
    print("file name: " + args.config_file)
    print(conf['database']['password'])
