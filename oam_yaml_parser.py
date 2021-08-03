import yaml
import pprint

yaml_path = [
    "./tests/2.ServiceTracker_App/KubeVelaManifest/app.yaml",
    "./tests/2.ServiceTracker_App/KubeVelaManifest/enhanced-webservice.yaml",
]

# yaml_path = [
#     "./tests/3.BikeSharing360_MultiContainer_App/KubeVelaManifest/app.yaml",
#     "./tests/3.BikeSharing360_MultiContainer_App/KubeVelaManifest/enhanced-webservice.yaml",
# ]

apps = []
components = {}
traits = []
workloads = []

app_component = {}
component_trait = {}
component_workload = {}


# This function returns oam-yaml file as dict type data
def read_yaml():
    global yaml_path
    yaml_list = []

    for path in yaml_path:
        with open(path) as file:
            yaml_list.append(yaml.load(file, Loader=yaml.FullLoader))

    return yaml_list


def parse_yaml(yaml_list):
    global apps, components, traits, workloads, app_component, component_trait, component_workload

    for yaml in yaml_list:

        # CASE: Application YAML
        if yaml["kind"] == "Application":
            app_name = yaml["metadata"]["name"]

            if app_name not in apps:
                apps.append(app_name)

                if app_name not in app_component:
                    app_component[app_name] = []

            for component in yaml["spec"]["components"]:
                component_name = component["name"]
                component_type = component["type"]

                if component_type not in components:
                    components[component_type] = []
                    component_trait[component_type] = []

                if component_name not in components[component_type]:
                    components[component_type].append(component_name)

                if component_name not in app_component[app_name]:
                    app_component[app_name].append(component_name)

                if "traits" in component:
                    for trait in component["traits"]:
                        trait_type = trait["type"]

                        if trait_type not in traits:
                            traits.append(trait_type)

                        if trait_type not in component_trait[component_type]:
                            component_trait[component_type].append(trait_type)

        # CASE: Component YAML
        elif yaml["kind"] == "ComponentDefinition":
            component_type = yaml["metadata"]["name"]

            if component_type not in component_workload:
                component_workload[component_type] = []

            if "workload" in yaml["spec"]:
                for workload in yaml["spec"]["workload"].values():
                    workload_name = workload["kind"]

                    if workload_name not in workloads:
                        workloads.append(workload_name)

                    if workload_name not in component_workload[component_type]:
                        component_workload[component_type].append(workload_name)

        # CASE: Exception
        else:
            print("================== New Type: " + yaml["kind"] + " ==================")


def print_data():
    global apps, components, traits, workloads, app_component, component_trait, component_workload

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


if __name__ == "__main__":
    yaml_list = read_yaml()
    parse_yaml(yaml_list)
    print_data()
