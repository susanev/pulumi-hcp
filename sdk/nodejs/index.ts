// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./awsNetworkPeering";
export * from "./awsTransitGatewayAttachment";
export * from "./consulCluster";
export * from "./consulClusterRootToken";
export * from "./consulSnapshot";
export * from "./getAwsNetworkPeering";
export * from "./getAwsTransitGatewayAttachment";
export * from "./getConsulAgentHelmConfig";
export * from "./getConsulAgentKubernetesSecret";
export * from "./getConsulCluster";
export * from "./getConsulVersions";
export * from "./getHvn";
export * from "./getHvnPeeringConnection";
export * from "./getHvnRoute";
export * from "./getPackerImage";
export * from "./getPackerImageIteration";
export * from "./getPackerIteration";
export * from "./getVaultCluster";
export * from "./hvn";
export * from "./hvnPeeringConnection";
export * from "./hvnRoute";
export * from "./provider";
export * from "./vaultCluster";
export * from "./vaultClusterAdminToken";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { AwsNetworkPeering } from "./awsNetworkPeering";
import { AwsTransitGatewayAttachment } from "./awsTransitGatewayAttachment";
import { ConsulCluster } from "./consulCluster";
import { ConsulClusterRootToken } from "./consulClusterRootToken";
import { ConsulSnapshot } from "./consulSnapshot";
import { Hvn } from "./hvn";
import { HvnPeeringConnection } from "./hvnPeeringConnection";
import { HvnRoute } from "./hvnRoute";
import { VaultCluster } from "./vaultCluster";
import { VaultClusterAdminToken } from "./vaultClusterAdminToken";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "hcp:index/awsNetworkPeering:AwsNetworkPeering":
                return new AwsNetworkPeering(name, <any>undefined, { urn })
            case "hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment":
                return new AwsTransitGatewayAttachment(name, <any>undefined, { urn })
            case "hcp:index/consulCluster:ConsulCluster":
                return new ConsulCluster(name, <any>undefined, { urn })
            case "hcp:index/consulClusterRootToken:ConsulClusterRootToken":
                return new ConsulClusterRootToken(name, <any>undefined, { urn })
            case "hcp:index/consulSnapshot:ConsulSnapshot":
                return new ConsulSnapshot(name, <any>undefined, { urn })
            case "hcp:index/hvn:Hvn":
                return new Hvn(name, <any>undefined, { urn })
            case "hcp:index/hvnPeeringConnection:HvnPeeringConnection":
                return new HvnPeeringConnection(name, <any>undefined, { urn })
            case "hcp:index/hvnRoute:HvnRoute":
                return new HvnRoute(name, <any>undefined, { urn })
            case "hcp:index/vaultCluster:VaultCluster":
                return new VaultCluster(name, <any>undefined, { urn })
            case "hcp:index/vaultClusterAdminToken:VaultClusterAdminToken":
                return new VaultClusterAdminToken(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("hcp", "index/awsNetworkPeering", _module)
pulumi.runtime.registerResourceModule("hcp", "index/awsTransitGatewayAttachment", _module)
pulumi.runtime.registerResourceModule("hcp", "index/consulCluster", _module)
pulumi.runtime.registerResourceModule("hcp", "index/consulClusterRootToken", _module)
pulumi.runtime.registerResourceModule("hcp", "index/consulSnapshot", _module)
pulumi.runtime.registerResourceModule("hcp", "index/hvn", _module)
pulumi.runtime.registerResourceModule("hcp", "index/hvnPeeringConnection", _module)
pulumi.runtime.registerResourceModule("hcp", "index/hvnRoute", _module)
pulumi.runtime.registerResourceModule("hcp", "index/vaultCluster", _module)
pulumi.runtime.registerResourceModule("hcp", "index/vaultClusterAdminToken", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("hcp", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:hcp") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
