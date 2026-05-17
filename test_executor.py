from executor import Executor

executor = Executor()

action = {
    "type": "WRITE_FILE",
    "target": "example.txt",
    "content": "hello world"
}

result = executor.run(action)

print(result)
