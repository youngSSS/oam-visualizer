import os
from time import sleep


def build_header():
    return "@startuml visualized_application\n\n"


def build_footer():
    return "hide methods\nhide circle\n\n@enduml"


def build_component(app_name, data):
    ret_val = "package " + app_name.title() + " <<Rectangle>> {\n\n"

    for item in data:
        ret_val += "\tclass " + item["component"].upper() + " {\n"

        for key in item:
            if key == "component":
                continue
            ret_val += "\t\t" + key.title() + " - " + item[key] + "\n"
            ret_val += "\t\t--\n"

        ret_val = ret_val[: len(ret_val) - 5]
        ret_val += "\t}\n\n"

    ret_val += "}\n\n"

    return ret_val


def visualize_uml():
    os.popen("plantuml ./result/uml_data.uml")
    os.popen("open ./result/visualized_application.png")
    return


def build_uml(app_name, data):
    uml_data = ""

    uml_data += build_header()
    uml_data += build_component(app_name, data)
    uml_data += build_footer()

    f = open("./result/uml_data.uml", "w")
    f.write(uml_data)
    f.close()

    visualize_uml()

    return uml_data
