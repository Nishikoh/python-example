import gokart
import time


class Example(gokart.TaskOnKart):
    def run(self):
        time.sleep(10)
        self.dump("Hello, world!")


class StringToSplit(gokart.TaskOnKart):
    """Like the function to divide received data by spaces."""

    task = gokart.TaskInstanceParameter()

    def run(self):
        time.sleep(10)
        sample = self.load("task")
        self.dump(sample.split(" "))


# task = Example()
task = StringToSplit(task=Example())
output = gokart.build(task)
print(output)
