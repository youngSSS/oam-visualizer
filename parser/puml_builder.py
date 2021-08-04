def header_builder():
    return "@startuml OAM Visualization\n\n"


def footer_builder():
    return "hide methods\nhide circle\n\n@enduml"


def package_builder(name, items):
    ret_val = "package " + name + " <<Rectangle>> {\n\n"

    if name == "Applications":
        for item in items:
            ret_val += "\tclass " + item + "\n"
        ret_val += "\n"

    elif name == "Components":
        for key, value in items.items():
            ret_val += "\tclass " + key + " {\n"
            for component_name in value:
                ret_val += "\t\t" + component_name + "\n"
                if component_name != value[-1]:
                    ret_val += "\t\t--\n"
            ret_val += "\t}\n\n"

    else:
        for item in items:
            ret_val += "\tclass " + item + "\n"
        ret_val += "\n"

    ret_val += "}\n\n"

    return ret_val


def relation_builder(app_comp, comp_trait, comp_workload):
    ret_val = ""
    line = " -up[dashed]- "
    arrow_line = " -up[dashed]-> "

    # Relation between application and component
    for key, value in app_comp.items():
        for comp in value:
            ret_val += comp + arrow_line + key + "\n"
    ret_val += "\n"

    # Relation between component and trait
    for key, value in comp_trait.items():
        for trait in value:
            ret_val += trait + line + key + "\n"
    ret_val += "\n"

    # Relation between component and workload
    for key, value in comp_workload.items():
        for workload in value:
            ret_val += workload + line + key + "\n"
    ret_val += "\n"

    print(ret_val)

    return ret_val
