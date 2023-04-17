"""
@author: Preston Konkel

Simple Pokemon battler GUI game
User is prompted to select between two pokemon types.
Next they enter any name they want for their pokemon.
Then the user has a choice of two attacks that change based on their Pokemon
type.
Whenever the user attacks it's then the Computer's turn which is always the
opposite type of pokemon then what the player chose. The Computer chooses an
attack at random.
First to get the enemy pokemon to zero health wins.

"""
import tkinter as tk
import random

class Pokemon:

    def __init__(self, name:str, hitPower:int, lifePoints:int):
        self.name = name
        self.hitPower = hitPower
        self.lifePoints = lifePoints

    def life_points_remaining(self):
        str = f"{self.name} has {self.lifePoints} life points remaining"
        return str

    def attack(self, enemy):
        if enemy.lifePoints > 0:
            enemy.lifePoints = enemy.lifePoints - self.hitPower
            str = f"{self.name} attacks and deals {self.hitPower} damage!\n"
        return str

class FireType(Pokemon):

    def fireBall(self, enemy):
        if enemy.lifePoints > 0:
            enemy.lifePoints = enemy.lifePoints - (self.hitPower+5)
            str = f"{self.name} uses fire ball attack! It deals 5 extra fire damage!\n"
        return str

class WaterType(Pokemon):

    def waterJet(self, enemy):
        if enemy.lifePoints > 0:
            enemy.lifePoints = enemy.lifePoints - (self.hitPower+6)
            str = f"{self.name} uses water jet attack! It deals 6 extra water damage!\n"
        return str

class GameOperator():

    def __init__(self, player, cpu, selection):
        self.player = player
        self.cpu = cpu
        self.selection = selection

    def set_selection_water(self):
        self.selection = "water"
        btn_fire.destroy()
        btn_water.destroy()
        entry_name.pack(side=tk.LEFT, expand=True)
        btn_enter_name.pack(side=tk.LEFT, expand=True)
        lbl0["text"] = "Enter the name of your Pokemon"

    def set_selection_fire(self):
        self.selection = "fire"
        btn_fire.destroy()
        btn_water.destroy()
        entry_name.pack(side=tk.LEFT, expand=True)
        btn_enter_name.pack(side=tk.LEFT, expand=True)
        lbl0["text"] = "Enter the name of your Pokemon"

    def set_up_game(self):
        color_player = None
        color_cpu = None
        if self.selection == "water":
            self.player = WaterType(entry_name.get(), 9, 90)
            self.cpu = FireType("Computer", 10, 100)
            color_player = "blue"
            color_cpu = "red"
        elif self.selection == "fire":
            self.player = FireType(entry_name.get(), 10, 100)
            self.cpu = WaterType("Computer", 9, 90)
            color_player = "red"
            color_cpu = "blue"
        btn_enter_name.destroy()
        entry_name.destroy()
        lbl0["text"] = "Time to fight! Select which attack to use"
        lbl_lifepoints_player["text"] = self.player.life_points_remaining()
        lbl_lifepoints_player["bg"] = color_player
        lbl_lifepoints_player.pack(side=tk.LEFT, expand=True)
        lbl_lifepoints_cpu["text"] = self.cpu.life_points_remaining()
        lbl_lifepoints_cpu["bg"] = color_cpu
        lbl_lifepoints_cpu.pack(side=tk.RIGHT, expand=True)
        btn_norm_attk.pack(side=tk.TOP, expand=True)
        btn_spec_attk.pack(side=tk.TOP, expand=True)

    def terminate(self):
        lbl0["text"] = "Thanks for playing! Closing program in 5"
        self.tksleep(1)
        lbl0["text"] = "Thanks for playing! Closing program in 4"
        self.tksleep(1)
        lbl0["text"] = "Thanks for playing! Closing program in 3"
        self.tksleep(1)
        lbl0["text"] = "Thanks for playing! Closing program in 2"
        self.tksleep(1)
        lbl0["text"] = "Thanks for playing! Closing program in 1"
        self.tksleep(1)
        root.destroy()

    def check_win_condition(self):
        if self.player.lifePoints == 0:
            lbl0["text"] = f"{self.player.name} has fainted! You lose!"
            self.tksleep(3)
            self.terminate()
        elif self.cpu.lifePoints == 0:
            lbl0["text"] = f"{self.cpu.name} has fainted! You win!"
            self.tksleep(3)
            self.terminate()

    def tksleep(self, t):
        """ since time.sleep() doesn't work with tkinter this method is used to
        emulate time.sleep(). Not my original code.
        Source: StackOverFlow, User: TheLizzard 
        https://stackoverflow.com/questions/10393886/tkinter-and-time-sleep/74162322#74162322"""
        ms = int(t*1000)
        rt = tk._get_default_root('sleep')
        var = tk.IntVar(rt)
        rt.after(ms, var.set, 1)
        rt.wait_variable(var)

    def norm_attk(self):
        lbl0["text"] = self.player.attack(self.cpu)
        lbl_lifepoints_cpu["text"] = self.cpu.life_points_remaining()
        self.tksleep(2)
        self.check_win_condition()
        self.cpu_attk()

    def spec_attk(self):
        if type(self.player).__name__ == "WaterType":
            lbl0["text"] = self.player.waterJet(self.cpu)
            lbl_lifepoints_cpu["text"] = self.cpu.life_points_remaining()
        elif type(self.player).__name__ == "FireType":
            lbl0["text"] = self.player.fireBall(self.cpu)
            lbl_lifepoints_cpu["text"] = self.cpu.life_points_remaining()
        self.tksleep(2)
        self.check_win_condition()
        self.cpu_attk()

    def cpu_attk(self):
        """ method that is called after player attacks. Then the cpu will attack
            the player. The attacks are chosen randomly """
        lbl0["text"] = "Now it's the Computer's turn"
        self.tksleep(1)
        lbl0["text"] = "Now it's the Computer's turn."
        self.tksleep(1)
        lbl0["text"] = "Now it's the Computer's turn.."
        self.tksleep(1)
        lbl0["text"] = "Now it's the Computer's turn..."
        self.tksleep(1)
        num = random.randint(1, 2)
        if num == 1:
            lbl0["text"] = self.cpu.attack(self.player)
            lbl_lifepoints_player["text"] = self.player.life_points_remaining()
        elif num == 2:
            if type(self.cpu).__name__ == "WaterType":
                lbl0["text"] = self.cpu.waterJet(self.player)
                lbl_lifepoints_player["text"] = self.player.life_points_remaining()
            elif type(self.cpu).__name__ == "FireType":
                lbl0["text"] = self.cpu.fireBall(self.player)
                lbl_lifepoints_player["text"] = self.player.life_points_remaining()
        self.check_win_condition()
if __name__ == "__main__":
    game = GameOperator(None, None, None)

    """ set up window """
    root = tk.Tk()
    root.title("Pokemon Battler")
    root.geometry('800x300')

    """ label for prompting user to select pokemon type """
    lbl0 = tk.Label(
        root,text = "Select which Pokemon type you want to play as")
    lbl0.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    """ labels for displaying player pokemon info """
    lbl_lifepoints_player = tk.Label(root)

    """ label for displaying cpu pokemon info """
    lbl_lifepoints_cpu = tk.Label(root)

    """ button for the user to select water type pokemon """
    btn_water = tk.Button(
        root, text="Water Type", bg="blue", command=game.set_selection_water)
    btn_water.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    """ button for the user to select fire type pokemon """
    btn_fire = tk.Button(
        root, text="Fire Type", bg="red", command=game.set_selection_fire)
    btn_fire.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

    """ button for the user to enter their pokemon's name """
    btn_enter_name = tk.Button(root, text="Enter", command=game.set_up_game)

    """ button for the user to select normal attack """
    btn_norm_attk = tk.Button(root, text="Normal attack", command=game.norm_attk)

    """ button for the user to select special attack """
    btn_spec_attk = tk.Button(root, text="Special attack", command=game.spec_attk)

    """ entry box for player to name their pokemon """
    entry_name = tk.Entry(root)

    """ main loop """
    root.mainloop()
