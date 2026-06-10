import os
import sys
import subprocess

def launch_mcp_proxy():
    """
    Launches the LightRAG MCP server over HTTP.
    Verifies the custom API key passed by the Azure AI Foundry Agent header.
    """
    
    # Network Configuration
    mcp_listen_host = "0.0.0.0"  
    mcp_listen_port = "8001"
    mcp_path = "/mcp"
    
    lightrag_host = "localhost"
    lightrag_port = "9621"
    
    # The exact value entered into the right-hand box of the Azure Portal
    # For production, load this via os.environ.get("MCP_SECRET_KEY")
    secure_token = "your_secure_mcp_token_here" 

    cmd = [
        sys.executable, "-m", "lightrag_mcp.main",
        "--mcp-transport", "streamable-http",
        "--mcp-host", mcp_listen_host,
        "--mcp-port", mcp_listen_port,
        "--mcp-streamable-http-path", mcp_path,
        "--host", lightrag_host,
        "--port", lightrag_port,
        
        # Enforces the token checking protocol down to the API client
        "--api-key", secure_token
    ]
    
    # Map the expected authentication environment variables for the package
    env_config = os.environ.copy()
    env_config["LIGHTRAG_API_KEY"] = secure_token
    
    print("Starting Secured LightRAG MCP Proxy Server...")
    print(f"Awaiting Key-based validation on port {mcp_listen_port}...")
    
    try:
        subprocess.run(cmd, check=True, env=env_config)
    except KeyboardInterrupt:
        print("\nShutting down the MCP Proxy gracefully.")
    except Exception as e:
        print(f"\nFailed to start the proxy: {e}")

if __name__ == "__main__":
    launch_mcp_proxy()