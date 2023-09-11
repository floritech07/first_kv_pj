import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.2.1')

class GameView(BoxLayout):
    def __init__(self):
        super(GameView, self).__init__()
        self.new_game()

    def new_game(self):
        self.randomValue = random.randint(0, 1000)
        self.result_label.text = "Trouver le nombre"
        self.result_label.color = "#000000"
        self.answer_input.text = ""

    def checknumber(self):
        try:
            guessed_number = int(self.answer_input.text)
            if guessed_number == self.randomValue:
                self.result_label.text = "Félicitations ! Vous avez trouvé le nombre."
                self.result_label.color = "#00EF0B"
            elif guessed_number < self.randomValue:
                self.result_label.text = "Plus grand !"
                self.result_label.color = "#EF3E00"
            else:
                self.result_label.text = "Plus petit !"
                self.result_label.color = "#EF3E00"
        except ValueError:
            self.result_label.text = "Veuillez entrer un nombre valide."
            self.result_label.color = "#EF3E00"
    
class FloriApp(App):
    def build(self):
        return GameView()
    
floriApp = FloriApp()
floriApp.run()
