import boto3
import json

client = boto3.client('eks', region_name="us-west-1")
# saving the cluster name out of the list
clusters = client.list_clusters()['clusters']
# printing output in json format for better view
clusters_json = json.dumps(clusters, indent=4)
# print(clusters_json)
# to get the cluster name
for cluster in clusters:
    response = client.describe_cluster(
        name=cluster
    )
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    # to get the cluster endpoint
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']
    print(f"Cluster: {cluster} status is {cluster_status}")
    print(f"Endpoint: {cluster_endpoint}")
    print(f"Version: {cluster_version}")