import pandas as pd
import os
import conf
import matplotlib.pyplot as plt
from cocapi import CocApi
from clan_data import read_file
from conf import configuration

class Clan_graph:
    def __init__(self):
        self.clan_tag = configuration.clan_tag
        self.token = read_file('info.txt')
        self.output_dir = "analysis"

        api = CocApi(self.token, config=configuration.config)

        os.makedirs(self.output_dir, exist_ok = True)

        data = api.clan_tag(self.clan_tag)
        info = data.get('memberList', [])
        self.df = pd.DataFrame(info)

    def config(self, arg):
        if (arg =="exp"):
            self.df.plot(x='tag', y='expLevel', kind='bar')
            filename = "exp_level.png"
        elif (arg =="level"):
         self.df.plot(x='tag', y='townHallLevel', kind='bar')
         filename = "townHall_level.png"
        plt.subplots_adjust(bottom=0.27)
        plt.savefig(
         os.path.join(self.output_dir, filename),
         dpi=300,
         bbox_inches="tight"
        )
   
    def show_exp(self):
        self.config("exp")

    def show_level(self):
        self.config("level")
            

