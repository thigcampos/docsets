IGNORED_FILES_AND_FOLDERS = ['man']


def handle_response(name: str, response: json) -> json:
    """It loops through the response and get the necessary information"""
    docset = {}
    docset['name'] = name

    for doc in response:
        doc_type = doc['type']
        if doc_type == 'dir':
            docset['dir'] = doc['name']
        else:
            docset['doc'] = doc['name']
            docset['path'] = doc['path']
            docset['sha'] = doc['sha']
            docset['download_url'] = doc['download_url']

        doc_name = doc['name']
        doc_path = doc['path']
        doc_sha = doc['sha']
        doc_download_url = doc['download_url']
    return response
