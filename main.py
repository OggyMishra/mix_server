from server import mcp
import tools.csv_tools
import tools.parquet_tools

if __name__ == "__main__":
    print("Starting MCP Mix Server")
    mcp.run()
