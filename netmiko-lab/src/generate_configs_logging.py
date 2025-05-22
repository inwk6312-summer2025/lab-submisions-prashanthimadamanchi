import yaml
import logging
from jinja2 import Environment, FileSystemLoader

# Setup logging
logging.basicConfig(filename='config_generation.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('config_template.j2')

    with open('devices.yaml') as file:
        data = yaml.safe_load(file)

    for router in data['routers']:
        config = template.render(**router)
        filename = f"{router['hostname']}_config.txt"
        with open(filename, "w") as f:
            f.write(config)
        logging.info(f"Generated config for {router['hostname']} saved to {filename}")

except Exception as e:
    logging.error(f"Error during config generation: {e}")
