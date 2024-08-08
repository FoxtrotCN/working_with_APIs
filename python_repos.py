import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
request = requests.get(url, headers=headers)
print(f"Status code: {request.status_code}")


# Store API response in a variable
response_dict = request.json()

# Process results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

# Explore info about the repos.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo
first_repo_dict = repo_dicts[0]


for repo_dict in repo_dicts:
    print("\nSelected information about first repository\n")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")




