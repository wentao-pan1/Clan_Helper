from cocapi import CocApi, ApiConfig

token ="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjNiNDYwZTdmLTQwMzYtNGQ5MS1iZGNhLTYwNjE2NTEyMzdjMSIsImlhdCI6MTc2NTkyMjc2Niwic3ViIjoiZGV2ZWxvcGVyLzFjM2ExZDc2LWMwOTItNDJiMS1hMTc1LWM1ODMzZmQwYjc2MCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjczLjg5Ljk2LjM3Il0sInR5cGUiOiJjbGllbnQifV19.qag_ZAPn_vgb8k0MIg5I7PZMtWQNtvFcNkkXwiOsPUpcWK8C3hxpD5wzsu0xMeQFJ_ZdDjQbbwDRFCYvVQpCNA"

config = ApiConfig(enable_metrics = True)

api = CocApi(token, config=config)

metrics = api.get_metrics()
#print(metrics.keys())

#help(ApiConfig)

Ctags = api.clan_tag("#2J9RRRRRR")
Ptags = api.players("#2P0J2GYQ")

Ckeys = Ctags.keys()
Pkeys = Ptags.keys()

#print(Ckeys)
#print("- - - - -")
#print(Pkeys)

Cmember = Ctags["members"]
print(Cmember)
