from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from game.minesweeper_grid import MinesweeperGrid
from game.restart_button import RestartButton
from game.xray_button import XRayButton
from kivy.core.window import Window


class MinesweeperApp(App):
    def build(self):
        grid = MinesweeperGrid()
        restart_button = RestartButton(grid)
        xray_button = XRayButton(grid)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(xray_button)
        layout.add_widget(restart_button)
        layout.add_widget(grid)
        return layout


if __name__ == '__main__':
    Window.size = (400, 500)
    MinesweeperApp().run()
