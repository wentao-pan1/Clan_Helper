from cocapi import ApiConfig


class configuration:
    clan_tag = ""
    player_tag = ""

    config = ApiConfig(enable_metrics=True, 
                       metrics_window_size=1000,
                       enable_rate_limiting=True,
                       requests_per_second=10,
                       max_retries=3)
    
    




