from mcp.server.fastmcp import FastMCP

# Initialize mcp at module level for proper exporting
mcp = FastMCP("mix_server")

# Export the mcp object
__all__ = ["mcp"]



