import pulumi
from pulumi_azure_native import resources, web
from pulumi_azure import appservice, sql
from pulumi_postgresql import Database


# Create an Azure Resource Group
resource_group = resources.ResourceGroup('az-400-demo')

# Create an Azure PostgreSQL database
postgres_db = sql.SqlDatabase(
    "psqlDatabase",
    resource_group_name=resource_group.name,
    location=resource_group.location,
    server_name="testapi.postgres.database.azure.com",
    database_name="api_test1",
    requested_service_objective_name="S0")

# Configuring the Azure Web App
app_service_plan = appservice.Plan(
    "testapiplan",
    resource_group_name=resource_group.name,
    kind="App",
    sku=appservice.PlanSkuArgs(
        tier="Basic",
        size="B1",
    ))

github_repo_url = "git@github.com:Prince-K-Ado/test_api.git"

app = web.WebApp(
    "thestruggledjangoapp",
    resource_group_name=resource_group.name,
    server_farm_id=app_service_plan.id,
    site_config=web.SiteConfigArgs(
        app_settings=[
            web.NameValuePairArgs(name="WEBSITE_RUN_FROM_PACKAGE", value=github_repo_url),
            # Set other necessary environment variables like database connection string
        ]
    ))

pulumi.export('app_service_endpoint', app.default_host_name)

