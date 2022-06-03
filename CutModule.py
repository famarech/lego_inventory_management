import json as _json
# import pathlib as _pathlib
from os.path import abspath

def cut_after(mot, str):
    index = str.find(mot)
    if index >= 0:
        index = index + (len(mot))
    else:
        index = 0
    return str[index:]

def cut_before(mot, str):
    index = str.find(mot)
    if index >= 0:
        index = index
    else:
        index = len(str)
    return str[:index]

def get(cls):
    # if cls._value is None:
        # mydir = _pathlib.Path(__file__).parent
    mdp_json = abspath('mdp.json')
    if mdp_json.is_file():
        with mdp_json.open() as f:
            mdp_params = _json.load(f)
        cls.set(pseudo = mdp_params["Pseudo"],
                mdp = mdp_params["MDP"])
    print(cls._value)
    return cls._value

get("")


  # def get(cls):
  #   if cls._value is None:
  #     mydir = _pathlib.Path(__file__).parent
  #     auth_json = mydir / "auth.json"
  #     if auth_json.is_file():
  #       with auth_json.open() as f:
  #         auth_params = _json.load(f)
  #     cls.set(
  #         consumer_key = auth_params["ConsumerKey"],
  #         consumer_secret = auth_params["ConsumerSecret"],
  #         token_value = auth_params["TokenValue"],
  #         token_secret = auth_params["TokenSecret"],
  #     )
  #   return cls._value