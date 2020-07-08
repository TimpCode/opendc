from opendc.util.database import DB


def test_get_prefab_non_existing(client, mocker):
    mocker.patch.object(DB, 'fetch_one', return_value=None)
    assert '404' in client.get('/api/v2/prefabs/1').status


def test_get_prefab_no_authorizations(client, mocker):
    mocker.patch.object(DB, 'fetch_one', return_value={'authorizations': []})
    res = client.get('/api/v2/prefabs/1')
    assert '403' in res.status


def test_get_prefab_not_authorized(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'authorizations': [{
                                'prefabId': '2',
                                'authorizationLevel': 'OWN'
                            }]
                        })
    res = client.get('/api/v2/prefabs/1')
    assert '403' in res.status


def test_get_prefab(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'authorizations': [{
                                'prefabId': '1',
                                'authorizationLevel': 'EDIT'
                            }]
                        })
    res = client.get('/api/v2/prefabs/1')
    assert '200' in res.status


def test_update_prefab_missing_parameter(client):
    assert '400' in client.put('/api/v2/prefabs/1').status


def test_update_prefab_non_existing(client, mocker):
    mocker.patch.object(DB, 'fetch_one', return_value=None)
    assert '404' in client.put('/api/v2/prefabs/1', json={'prefab': {'name': 'S'}}).status


def test_update_prefab_not_authorized(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'authorizations': [{
                                'prefabId': '1',
                                'authorizationLevel': 'VIEW'
                            }]
                        })
    mocker.patch.object(DB, 'update', return_value={})
    assert '403' in client.put('/api/v2/prefabs/1', json={'prefab': {'name': 'S'}}).status


def test_update_prefab(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'authorizations': [{
                                'prefabId': '1',
                                'authorizationLevel': 'OWN'
                            }]
                        })
    mocker.patch.object(DB, 'update', return_value={})

    res = client.put('/api/v2/prefabs/1', json={'prefab': {'name': 'S'}})
    assert '200' in res.status


def test_delete_prefab_non_existing(client, mocker):
    mocker.patch.object(DB, 'fetch_one', return_value=None)
    assert '404' in client.delete('/api/v2/prefabs/1').status


def test_delete_prefab_different_user(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'googleId': 'other_test',
                            'authorizations': [{
                                'prefabId': '1',
                                'authorizationLevel': 'VIEW'
                            }],
                            'topologyIds': []
                        })
    mocker.patch.object(DB, 'delete_one', return_value=None)
    assert '403' in client.delete('/api/v2/prefabs/1').status


def test_delete_prefab(client, mocker):
    mocker.patch.object(DB,
                        'fetch_one',
                        return_value={
                            '_id': '1',
                            'googleId': 'test',
                            'authorizations': [{
                                'prefabId': '1',
                                'authorizationLevel': 'OWN'
                            }],
                            'topologyIds': [],
                            'experimentIds': [],
                        })
    mocker.patch.object(DB, 'update', return_value=None)
    mocker.patch.object(DB, 'delete_one', return_value={'googleId': 'test'})
    res = client.delete('/api/v2/prefabs/1')
    assert '200' in res.status
