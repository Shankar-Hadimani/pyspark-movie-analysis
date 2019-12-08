import yaml

class LoadConfiguration():

    def __init__(self, filepath):
        self.filepath = filepath
    
    def yaml_loader(self):
        """ Loads the yaml file to set project parameters """
        with open(self.filepath,"r") as fd:
            data = yaml.full_load(fd)
        return data

    def yaml_dump(self, data):
        """ Dumps the data into yaml file """
        with open(self.filepath,"w") as fd:
            yaml.dump(data,fd)

