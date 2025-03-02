import requests

url = "https://raw.githubusercontent.com/ai-robots-txt/ai.robots.txt/main/robots.txt"
response = requests.get(url)
txt = response.text

txt = "\n".join([line for line in txt.split("\n") if line != "User-agent: Applebot"])

bots = [
    line.split(": ")[1].strip().replace(' ', '\\ ')
    for line in txt.split("\n")
    if line.startswith("User-agent:") and line != "User-agent: Applebot"
]

CONF = r"""if ($http_user_agent ~* "({0})"){{
    return 403;
}}"""

print(CONF.format("|".join(bots)))
