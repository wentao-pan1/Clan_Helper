import csv
import asyncio
import os
from cocapi import CocApi, ApiConfig    
from conf import configuration

#2J9RRRRRR

class Clan_data:
    def __init__(self):
        self.clan_tag = configuration.clan_tag
        self.output_dir = 'analysis'

        os.makedirs(self.output_dir, exist_ok = True)

        self.config = configuration.config
    
    async def export_table(self):
        token = read_file("info.txt")
        if not token: 
            print("token not found in info.txt")
            return
        
        async with CocApi(token, config=self.config) as api:
            try:
                clan_data = await api.clan_tag(self.clan_tag)
                members = clan_data.get('memberList', [])
                fieldnames = ['name', 
                          'tag', 
                          'role', 
                          'expLevel', 
                          'trophies',
                          'townHallLevel']
                csv_path = os.path.join(self.output_dir, "clan_members.csv")

                with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()

                    for member in members:
                        row = {key: member.get(key) for key in fieldnames}
                        writer.writerow(row)

            except Exception as e:
                print(f"API or File Error: {e}")


def read_file(filename):
        data = {}
        collection = []
        current_key = None

        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.endswith(":"):
                    current_key = line[:-1].strip().lower()
                    collection = []
                else:
                    collection.append(line)
                    if current_key:
                        data[current_key] = "".join(collection)

        return data.get("token", "")
        

if __name__ == "__main__":
    print(read_file('info.txt'))
   

