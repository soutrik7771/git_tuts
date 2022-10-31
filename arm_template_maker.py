import json
import yaml

"""
    Reading the azure monitor json template file
    this file will be used to create new template
    with different default parameter
"""
json_template_path = "environment_setup/arm_templates/azure_monitor_template.json"

# alert object as reading from pipeline.yml file
yml_path = ".pipelines/alerts_iac_pipeline.yml"
with open(yml_path, "r") as f:
    content = yaml.safe_load(f)


def join_names(arr):
    # utility function to concatinate names from array
    rr = ''
    for ele in arr:
        rr += ele + " "
    return rr


for alert in content["parameters"][0]["default"]:
    with open(json_template_path, "r") as file2:
        arm = json.load(file2)
    arm["parameters"]["alertName"]["defaultValue"] = alert["alertName"]
    arm["parameters"]["alertDescription"]["defaultValue"] = alert["alertDescription"]
    arm["parameters"]['alertSeverity']["defaultValue"] = alert["alertSeverity"]
#         arm["parameters"]["resourceId"]["defaultValue"] = "resource_id" will be overriden
    arm["parameters"]['metricName']["defaultValue"] = join_names(alert["metricName"]).strip()
#         arm["parameters"]['actionGroupId']["defaultValue"] = "action group id" will be overriden
    arm["parameters"]['autoMitigate']["defaultValue"] = alert["autoMitigate"]
    arm["parameters"]['isEnabled']["defaultValue"] = alert["isEnabled"]
    if "dimension" in alert:
        arm["parameters"]['dimensions']["defaultValue"] = alert["dimension"]
#         print(arm)
    with open(alert["alertName"] + ".json", "w") as file:
        json.dump(arm, file)
