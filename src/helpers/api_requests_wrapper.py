import json
import requests


def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, json=payload, data=json.dumps(payload))
    if in_json:
        return post_response.json()
    else:
        return post_response


def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, json=payload, data=json.dumps(payload))
    if in_json:
        return put_response.json()
    else:
        return put_response


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, auth=auth, headers=headers, json=payload, data=json.dumps(payload))
    if in_json:
        return patch_response.json()
    else:
        return patch_response


def delete_request(url, auth, headers, in_json):
    delete_response = requests.delete(url=url, auth=auth, headers=headers)
    if in_json:
        return delete_response.json()
    else:
        return delete_response
