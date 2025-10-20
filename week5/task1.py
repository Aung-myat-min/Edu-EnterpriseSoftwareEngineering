class Hello:
    greeting = ''

    def __init__(self, name):
        self.greeting = name

    def say_hello(self):
        print(f'Hello {self.greeting}')

sandar = Hello('Sandar')
sandar.say_hello()