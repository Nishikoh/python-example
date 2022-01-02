from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

app = FastAPI()


@app.get("/hello")
def hello():
    return {"Hello": "World"}


@app.get("/query")
async def hello_query(id: Optional[str] = None):
    return {"text": f"hello world, {id}!"}


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return "Hello " + name


# https://github.com/graphql-python/graphene#examples


app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))

# %%
import graphene


class Query(graphene.ObjectType):
    helloo = graphene.String(description="A typical hello world")

    def resolve_helloo(self, info):
        return "World"


schema = graphene.Schema(query=Query)
query = '''
    query SayHello {
      helloo
    }
'''
result = schema.execute(query)
print(result)
# %%
