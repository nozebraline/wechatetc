import werobot

robot = werobot.WeRoBot(token='etcwuganzhifuyingxiao')


@robot.handler
def hello(message):
    return 'Hello World!'


if __name__ == '__main__':
    # 让服务器监听在 0.0.0.0:80
    robot.config['HOST'] = '0.0.0.0'
    robot.config['PORT'] = 80
    robot.run()
