
from botcity.core import Desktop
from config.login import login
from time import sleep

class Bot(Desktop):
    def action(self, execution):
        self.browse('https://dapic.webpic.com.br/')
        
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
