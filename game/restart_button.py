from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior


class RestartButton(ButtonBehavior, Label):
    def __init__(self, grid, **kwargs):
        super(RestartButton, self).__init__(**kwargs)
        self.grid = grid
        self.text = 'Restart'
        self.size_hint = (None, None)
        self.size = (100, 50)
        self.pos_hint = {'center_x': 0.5, 'y': 0.1}  # Размещаем кнопку по центру по горизонтали и ближе к нижней границе экрана
        self.bind(on_release=self.restart_game)

    def restart_game(self, *args):
        self.grid.restart_game()
