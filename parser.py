import yaml
import pprint
from uml_builder import puml_builder as pb
from uml_builder import test as t

apps = []
components = {}
traits = []
workloads = []

app_component = {}
component_trait = {}
component_workload = {}


# This function returns oam-yaml file as dict type data
def read_yaml(yaml_path):
    yaml_list = []

    for path in yaml_path:
        with open(path) as file:
            yaml_list.append(yaml.load(file, Loader=yaml.FullLoader))

    return yaml_list


def parse_yaml(yaml_list):
    for yaml in yaml_list:

        # CASE: Application YAML
        if yaml["kind"] == "Application":
            app_name = yaml["metadata"]["name"].replace("-", "_").title()

            if app_name not in apps:
                apps.append(app_name)

                if app_name not in app_component:
                    app_component[app_name] = []

            for component in yaml["spec"]["components"]:
                component_name = component["name"].replace("-", "_")
                component_type = component["type"].replace("-", "_").title()

                if component_type not in components:
                    components[component_type] = []
                    component_trait[component_type] = []

                if component_name not in components[component_type]:
                    components[component_type].append(component_name)

                if component_type not in app_component[app_name]:
                    app_component[app_name].append(component_type)

                if "traits" in component:
                    for trait in component["traits"]:
                        trait_type = trait["type"].replace("-", "_").title()

                        if trait_type not in traits:
                            traits.append(trait_type)

                        if trait_type not in component_trait[component_type]:
                            component_trait[component_type].append(trait_type)

        # CASE: Component YAML
        elif yaml["kind"] == "ComponentDefinition":
            component_type = yaml["metadata"]["name"].replace("-", "_").title()

            if component_type not in component_workload:
                component_workload[component_type] = []

            if "workload" in yaml["spec"]:
                for workload in yaml["spec"]["workload"].values():
                    workload_name = workload["kind"].replace("-", "_").title()

                    if workload_name not in workloads:
                        workloads.append(workload_name)

                    if workload_name not in component_workload[component_type]:
                        component_workload[component_type].append(workload_name)

        # CASE: Exception
        else:
            print("================ Undefined Type: " + yaml["kind"] + " ================")


def print_data():
    pp = pprint.PrettyPrinter(width=20, indent=4)

    pp.pprint("Apps")
    pp.pprint(apps)
    print()
    pp.pprint("Components")
    pp.pprint(components)
    print()
    pp.pprint("Traits")
    pp.pprint(traits)
    print()
    pp.pprint("Workloads")
    pp.pprint(workloads)
    print()
    pp.pprint("App-Component")
    pp.pprint(app_component)
    print()
    pp.pprint("Component-Trait")
    pp.pprint(component_trait)
    print()
    pp.pprint("Component-Workload")
    pp.pprint(component_workload)


def build_uml(idx):
    f = open("./result/yaml_data.uml" + str(idx), "w")
    content = pb.header_builder()
    content += pb.package_builder("Applications", apps)
    content += pb.package_builder("Components", components)
    content += pb.package_builder("Traits", traits)
    content += pb.package_builder("Workloads", workloads)
    content += pb.relation_builder(app_component, True)
    content += pb.relation_builder(component_trait, False)
    content += pb.relation_builder(component_workload, False)
    content += pb.footer_builder()
    f.write(content)
    f.close()


if __name__ == "__main__":
    yaml_path = t.get_test_file_path(7)
    yaml_list = read_yaml(yaml_path)
    parse_yaml(yaml_list)
    print_data()
    build_uml("")
