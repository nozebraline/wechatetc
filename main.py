import werobot

robot = werobot.WeRoBot(token='etcwuganzhifuyingxiao')


@robot.handler
def hello(message):
    return 'Hello World!'


if __name__ == '__main__':
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 8081
    robot.run()
