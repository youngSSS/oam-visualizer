import yaml
import pprint

COMPONENT_KEYWORDS = ["type", "properties", "traits"]

yaml_path = [
    "./tests/2.ServiceTracker_App/KubeVelaManifest/app.yaml",
    "./tests/2.ServiceTracker_App/KubeVelaManifest/enhanced-webservice.yaml",
]
application = {"name": {}, "components": {}}
yaml_data = {}


# This function returns oam-yaml file as dict type data
def read_yaml():
    global yaml_path
    yaml_list = []

    for path in yaml_path:
        with open(path) as file:
            yaml_list.append(yaml.load(file, Loader=yaml.FullLoader))

    return yaml_list


def parse_yaml(yaml_list):
    global application, yaml_data, COMPONENT_KEYWORDS

    for yaml in yaml_list:
        # CASE: 주진입점이 되는 YAML
        if yaml["kind"] == "Application":
            application["name"] = yaml["metadata"]["name"]
            for component in yaml["spec"]["components"]:
                application["components"][component["name"]] = {}
                for keyword in COMPONENT_KEYWORDS:
                    if keyword in component:
                        application["components"][component["name"]][keyword] = component[keyword]

        # CASE: Application에서 사용하는 YAML
        else:
            yaml_data[yaml["metadata"]["name"]] = {"kind": yaml["kind"]}


def print_data():
    pp = pprint.PrettyPrinter(width=20, indent=4)
    pp.pprint(application)
    print()
    pp.pprint(yaml_data)


if __name__ == "__main__":
    yaml_list = read_yaml()
    parse_yaml(yaml_list)
    print_data()
