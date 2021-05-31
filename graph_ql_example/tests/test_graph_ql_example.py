from graph_ql_example import __version__
from fastapi.testclient import TestClient
from graph_ql_example.main import Query, app
from graphene.test import Client
import graphene


client = TestClient(app)


def test_version():
    assert __version__ == "0.1.0"


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_query():
    response = client.get("/query")
    assert response.status_code == 200
    assert response.json() == {"text": "hello world, None!"}

    response = client.get("/query?id=1")
    assert response.status_code == 200
    assert response.json() == {"text": "hello world, 1!"}

    response = client.get("/query?id=hoge")
    assert response.status_code == 200
    assert response.json() == {"text": "hello world, hoge!"}


def test_graphql():
    client = Client(graphene.Schema(query=Query))
    executed = client.execute(
        """query{
            hello(name: "Fast API")
           }"""
    )
    assert executed == {"data": {"hello": "Hello Fast API"}}
