def header_builder():
    return "@startuml OAM\n\n"


def footer_builder():
    return "hide methods\nhide circle\n\n@enduml"


def package_builder(name, items):
    ret_val = "package " + name + " <<Rectangle>> {\n\n"

    if name == "Components":
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


def relation_builder(relation, arrow_flag):
    ret_val = ""

    if arrow_flag:
        line = "-up[dashed]-> "
    else:
        line = " -up[dashed]- "

    for key, value in relation.items():
        for v in value:
            ret_val += v + line + key + "\n"
    ret_val += "\n"

    return ret_val
