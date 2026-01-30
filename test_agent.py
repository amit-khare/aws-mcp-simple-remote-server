# Using Strands Agents SDK for this example
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp_proxy_for_aws.client import aws_iam_streamablehttp_client

# Set your MCP server details from Step 4
RUNTIME_ID = "my_mcp_server-1Do2GZ9bZf"
ACCOUNT_ID = "951734276939"
REGION = "us-east-1"

def main():
    # Build the MCP server URL
    url = f"https://bedrock-agentcore.{REGION}.amazonaws.com/runtimes/{RUNTIME_ID}/invocations?qualifier=DEFAULT&accountId={ACCOUNT_ID}"

    print(f"\nInitializing MCP client with IAM-based auth for:\n{url}")

    mcp_client_factory = lambda: aws_iam_streamablehttp_client(
        aws_service="bedrock-agentcore",
        aws_region=REGION,
        endpoint=url,
        terminate_on_close=False
    )

    with MCPClient(mcp_client_factory) as mcp_client:
        mcp_tools = mcp_client.list_tools_sync()
        agent = Agent(tools=mcp_tools)

        query_1 = "What tools do you have available?"
        print(f"\nQ: {query_1}")
        agent(query_1)

        query_2 = "Roll three dice"
        print(f"\nQ: {query_2}")
        agent(query_2)

if __name__ == "__main__":
    main()