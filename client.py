import pickle
import requests

proxy_url = "https://o9iq3cn4tc.execute-api.eu-west-1.amazonaws.com/dev"

proxy_response = requests.post(
    f"{proxy_url}",
    data={'url': 'https://ianwhitestone.work'}
)
if not proxy_response.ok:
    raise Exception(
        "Proxy request not successful. Status code: "
        f"{proxy_response.status_code}\n{proxy_response.text}"
    )
response = pickle.loads(proxy_response.content)
