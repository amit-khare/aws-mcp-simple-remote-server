import random
from fastmcp import FastMCP

# Initialize FastMCP with local configuration
mcp  = FastMCP()

@mcp.tool
def add_numbers(a : float, b : float) -> float:
    """Add two numbers together."""
    return a + b
    
@mcp.tool
def roll_dice(n_dice : int=1) -> list[int]:
    """Roll n_dice 6-sided dice  and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

def main():
    mcp.run(transport="streamable-http", stateless_http=True, port=8000)

if __name__ == "__main__":
    main()
