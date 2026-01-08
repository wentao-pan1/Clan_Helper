import sys
import asyncio
from clan_data import Clan_data
from clan_graph import Clan_graph
from conf import configuration

async def main():
    configuration.clan_tag = sys.argv[1]
    data = Clan_data()
    graph = Clan_graph()

    await data.export_table()
    graph.show_exp()
    graph.show_level()


if __name__ == "__main__":
    asyncio.run(main())




    

    
    


