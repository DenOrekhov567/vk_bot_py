import yaml

def get_token():
    with open('resources/config.yml', 'r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)['token']
