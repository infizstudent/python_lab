from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
import random


class MinesweeperGrid(GridLayout):
    def build(self):
        Builder.load_file('styles.kv')
    def __init__(self, **kwargs):
        super(MinesweeperGrid, self).__init__(**kwargs)
        self.cols = 10
        self.rows = 10
        self.mine_count = 10
        self.button_grid = []
        self.revealed_cells = set()
        self.flagged_cells = set()
        self.game_over = False

        self.generate_mines()
        self.create_grid_buttons()

        self.padding = [20, 100, 20, 20]  # Добавляем отступы

    def generate_mines(self):
        self.mine_positions = random.sample(range(self.cols * self.rows), self.mine_count)

    def create_grid_buttons(self):
        for i in range(self.cols * self.rows):
            button = Button(text=' ', font_size=24)
            button.bind(on_release=self.on_button_release)
            button.bind(on_touch_down=self.on_button_touch_down)
            self.button_grid.append(button)
            self.add_widget(button)

            

    def on_button_release(self, button):
        if self.game_over:
            return

        if button in self.flagged_cells:
            return

        button.disabled = True
        button_color = (0.3, 0.3, 0.3, 1)
        index = self.button_grid.index(button)

        if self.mine_positions.count(index) > 0:
            button.text = 'X'
            button_color = (1, 0, 0, 1)
            self.show_all_mines()
            self.game_over = True
        else:
            self.revealed_cells.add(index)
            adjacent_mine_count = self.get_adjacent_mine_count(index)
            if adjacent_mine_count > 0:
                button.text = str(adjacent_mine_count)
            else:
                button.text = ' '
                self.open_adjacent_cells(index)

        button.background_color = button_color
        self.check_victory()

    def on_button_touch_down(self, button, touch):
        if self.game_over:
            return

        if button.disabled:
            return

        if button.collide_point(*touch.pos):
            if touch.button == 'right':
                if button.text == ' ':
                    button.text = 'F'
                    self.flagged_cells.add(button)
                elif button.text == 'F':
                    button.text = ' '
                    self.flagged_cells.remove(button)

    def get_adjacent_mine_count(self, index):
        count = 0
        row = index // self.cols
        col = index % self.cols

        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                adjacent_index = i * self.cols + j
                if adjacent_index != index and self.mine_positions.count(adjacent_index) > 0:
                    count += 1

        return count

    def open_adjacent_cells(self, index):
        row = index // self.cols
        col = index % self.cols

        for i in range(max(0, row - 1), min(row + 2, self.rows)):
            for j in range(max(0, col - 1), min(col + 2, self.cols)):
                adjacent_index = i * self.cols + j
                if adjacent_index != index and adjacent_index not in self.revealed_cells and \
                        adjacent_index not in self.flagged_cells and self.mine_positions.count(adjacent_index) == 0:
                    adjacent_button = self.button_grid[adjacent_index]
                    adjacent_button.disabled = True
                    adjacent_button_color = (0.3, 0.3, 0.3, 1)
                    self.revealed_cells.add(adjacent_index)
                    adjacent_mine_count = self.get_adjacent_mine_count(adjacent_index)
                    if adjacent_mine_count > 0:
                        adjacent_button.text = str(adjacent_mine_count)
                    else:
                        adjacent_button.text = ' '
                        self.open_adjacent_cells(adjacent_index)

                    adjacent_button.background_color = adjacent_button_color

    def show_all_mines(self):
        for index, button in enumerate(self.button_grid):
            if self.mine_positions.count(index) > 0:
                button.text = 'X'
                button.background_color = (1, 0, 0, 1)
                button.disabled = True

    def check_victory(self):
        if len(self.revealed_cells) + len(self.flagged_cells) == self.cols * self.rows:
            self.show_victory_popup()

    def show_victory_popup(self):
        content = Label(text='You Win!', font_size=24)
        popup = Popup(title='Congratulations', content=content, size_hint=(0.8, 0.4), size=(300, 200))
        popup.open()

    def restart_game(self, *args):
        self.clear_widgets()
        self.button_grid = []
        self.revealed_cells = set()
        self.flagged_cells = set()
        self.game_over = False

        self.generate_mines()
        self.create_grid_buttons()
