# Stop old instance
docker stop mcp-proxy && docker rm mcp-proxy

# Rebuild and run
docker build -t lightrag-mcp-proxy:latest .
docker run -d --name mcp-proxy --restart always -p 8001:8001 lightrag-mcp-proxy:latest