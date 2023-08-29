import boto3

regions = ["us-east-1", "eu-west-1", "ap-east-1"]

for region in regions:
    cloudformation = boto3.client("cloudformation", region_name=region)

    template_url = f"https://s3.amazonaws.com/ec-global-ds/{region}-template.json"

    cloudformation.create_stack(
        StackName=f"Ekata-prod-{region}",  # Adding region to the stack name
        TemplateURL=template_url,
        Parameters=[
            {"ParameterKey": "Environment", "ParameterValue": "production"},
            {"ParameterKey": "subnet1az", "ParameterValue": region + "a"},
            {"ParameterKey": "subnet2az", "ParameterValue": region + "b"},
            {"ParameterKey": "subnet3az", "ParameterValue": region + "c"},
        ],
    )
