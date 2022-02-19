import gokart
import time


class Example(gokart.TaskOnKart):
    def run(self):
        time.sleep(5)
        self.dump("Hello, world!")


task = Example()
output = gokart.build(task)
print(output)
