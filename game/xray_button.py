from kivy.uix.button import Button


class XRayButton(Button):

    def __init__(self, grid, **kwargs):
        super(XRayButton, self).__init__(**kwargs)
        self.grid = grid
        self.text = 'X-Ray'
        self.size_hint = (None, None)
        self.size = (100, 50)
        self.pos_hint = {'x': 0.9, 'y': 0.95}
        self.bind(on_release=self.show_mines)

    def show_mines(self, *args):
        self.grid.show_all_mines()
