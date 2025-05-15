from jinja2 import Environment, FileSystemLoader
import yaml
import os

# Define the path to your templates and data files
template_dir = '.'  # Assuming templates are in the current directory
data_file = 'network_data.yaml'

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('router_config.j2')

# Load network data from YAML file
with open(data_file, 'r') as f:
    network_data = yaml.safe_load(f)

# Generate configurations for each router
for router_name, router_details in network_data['routers'].items():
    config = template.render(router=router_details)
    output_filename = f"{router_name}_config.txt"
    with open(output_filename, 'w') as f:
        f.write(config)
    print(f"Generated configuration for {router_name} in {output_filename}")
