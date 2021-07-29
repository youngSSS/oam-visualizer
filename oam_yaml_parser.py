import yaml


oam_yaml_path = "./yaml_samples/1.Helloworld/app.yaml"

# This function returns oam-yaml file as dict type data
def read_oam_yaml():
    global oam_yaml_path

    with open(oam_yaml_path) as file:
        oam_yaml = yaml.load(file, Loader=yaml.FullLoader)

    return oam_yaml


def parse_oam_yaml(oam_yaml):
    print(type(oam_yaml))


if __name__ == "__main__":
    oam_yaml = read_oam_yaml()
    parse_oam_yaml(oam_yaml)
