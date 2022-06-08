class Secret:
    TOKEN = "ODkwMTM5NzEwODg0ODE4OTg0.Gh3IEP.PZDYMqkeMu36WMf-YP9UTSFfbadxanP6kNqizQ"
    
    def __init__(self):
        self.TOKEN = Secret.TOKEN
        
    def get_token(self):
        return self.TOKEN