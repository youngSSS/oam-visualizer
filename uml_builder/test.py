def get_test_file_path(idx):
    if idx == 1:
        path = [
            "./tests/1.Helloworld/app.yaml",
            "./tests/1.Helloworld/app-upgrade.yaml",
        ]
    elif idx == 2:
        path = [
            "./tests/2.ServiceTracker_App/KubeVelaManifest/app.yaml",
            "./tests/2.ServiceTracker_App/KubeVelaManifest/enhanced-webservice.yaml",
        ]

    elif idx == 3:
        path = [
            "./tests/3.BikeSharing360_MultiContainer_App/KubeVelaManifest/app.yaml",
            "./tests/3.BikeSharing360_MultiContainer_App/KubeVelaManifest/enhanced-webservice.yaml",
        ]

    elif idx == 4:
        path = [
            "./tests/4.BikeSharing360_SingleContainer_App/app.yaml",
        ]

    elif idx == 5:
        path = [
            "./tests/5.KUBEVELA_KPT_Demo/repository/sampleapp/app.yaml",
        ]

    elif idx == 6:
        path = [
            "./tests/6.Knative_App/app.yaml",
            "./tests/6.Knative_App/componentdefinition-knative-serving.yaml",
        ]

    elif idx == 7:
        path = [
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/App/boutique.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/App/product-deployment.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/App/product-v1.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/App/product-v2.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-annotations.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-cmd-probe.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-http-probe.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-loadbalancer.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-resources-limits.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-tcp-probe.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/traits/patch-volume.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/workloads/enhanced-webservice.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/workloads/enhanced-worker.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/Definitions/workloads/microservice.yaml",
            "./tests/7.GoogleCloudPlatform_MicroServices_Demo/istio-canary/rollback.yaml",
            # "./tests/7.GoogleCloudPlatform_MicroServices_Demo/istio-canary/traffic.yaml",
            # "./tests/7.GoogleCloudPlatform_MicroServices_Demo/istio-manifests.yaml",
        ]

    elif idx == 8:
        path = [
            "./tests/8.Terraform_DEMO/8.1Website_on_ECS/application.yaml",
            "./tests/8.Terraform_DEMO/8.1Website_on_ECS/ComponentDefinition-alibaba-website.yaml",
        ]

    return path
