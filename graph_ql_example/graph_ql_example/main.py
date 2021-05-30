from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

app = FastAPI()


@app.get("/hello")
def hello():
    return {"Hello": "World"}


@app.get("/query")
async def hello_query(id: str = None):
    return {"text": f"hello world, {id}!"}


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))
