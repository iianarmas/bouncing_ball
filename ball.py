from kivy.app import App
from kivy.graphics import Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget


class BallAnim(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.velocity_x = dp(3)
        self.velocity_y = dp(4)

        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 2/60)

    def on_size(self, *args):
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):
        x, y = self.ball.pos

        if x + self.ball_size > self.width:
            self.velocity_x = -self.velocity_x
        elif y + self.ball_size > self.height:
            self.velocity_y = -self.velocity_y
        elif x <= 0:
            self.velocity_x = -self.velocity_x
        elif y <= 0:
            self.velocity_y = -self.velocity_y

        x += self.velocity_x
        y += self.velocity_y
        self.ball.pos = (x, y)


class BallApp(App):
    def build(self):
        return BallAnim()


if __name__ == "__main__":
    BallApp().run()
