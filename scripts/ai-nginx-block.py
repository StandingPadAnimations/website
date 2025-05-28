import requests

# Fetch robots.txt content
url = "https://raw.githubusercontent.com/ai-robots-txt/ai.robots.txt/main/robots.txt"
response = requests.get(url)
txt = response.text

# Filter out lines for Applebot
txt = "\n".join([line for line in txt.split("\n") if line != "User-agent: Applebot"])

# Get the list of user-agents to block
bots = [
    line.split(": ")[1].strip()
    for line in txt.split("\n")
    if line.startswith("User-agent:") and line != "User-agent: Applebot"
]


lines = ["@blocked_user_agents {"]

for bot in bots:
    lines.append(f"header User-Agent \"{bot}\"")

lines.append("}")
lines.append("respond @blocked_user_agents 403")

# Output Caddyfile configuration with the bots
print("\n".join(lines))
