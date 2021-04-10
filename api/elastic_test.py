from elasticsearch import Elasticsearch


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch(timeout=10)
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es


def create_index(es_object, index_name='user'):
    created = False
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "submitter": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "integer"
                    },
                }
            }
        }
    }
    try:
        if not es_object.indices.exists(index_name):
            es_object.indices.create(index=index_name, ignore=400, body=index_settings)
            print('Created new index: {}'.format(index_name))
        else:
            print('Index {} already exists'.format(index_name))
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


es = connect_elasticsearch()
create_index(es, 'user')
