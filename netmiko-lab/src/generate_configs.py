import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('config_template.j2')

with open('devices.yaml') as file:
    data = yaml.safe_load(file)

for router in data['routers']:
    config = template.render(**router)
    with open(f"{router['hostname']}_config.txt", "w") as f:
        f.write(config)
