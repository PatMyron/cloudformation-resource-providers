import os
import re
import requests
url = 'https://api.github.com/orgs/aws-cloudformation/repos?type=public&per_page=100&sort=full_name'
while url:
  for repo in requests.get(url).json():
      if 'aws-cloudformation-resource-provider' in repo['html_url']:
          os.system('git submodule add ' + repo['html_url'] + ' ' + re.sub('.*resource-providers?-', '', repo['html_url']))
  url = requests.get(url).links.get('next', {}).get('url')
