"""
Game AI -- this is for you to complete

TEAM ID IS ALREADY SET
"""



import requests
import time
import random
import sys

SERVER = "http://127.0.0.1:5000"  # this will not change
TEAM_ID = "withya1809"  # set it to your GitHub username


def reg():
    # register using a fixed team_id
    resp = requests.get(SERVER + "/reg/" + TEAM_ID).json()  # register 1st team


    if resp["response"] == "OK":
        # save which player we are
        print("Registered successfully as Player {}".format(resp["player"]))
        return resp["player"]
    else:
        # TODO handle the case where the response was ERROR
        if resp["response"] == "ERROR":

            if resp["error_code"] == 1:
                print("invalid team")
            elif resp["error_code"] == 2:
                print("team_id, already exists")
            elif resp["error_code"] == 3:
                print("Game has already started")
            
            return resp["error_code"]


def play(player):
    game_over = False

    #Calculation of bits - to know which sides are occupied, to compare with the board
    sum_border_dict = {
        3: "tr",
        5: "tb", 
        9: "tl",
        6: "rb",
        10: "rl",
        12: "bl",
        7: "trb",
        13: "ltb",
        11: "trl",
        14:"rbl"
    }
    border_dict = {
        1: "top",
        2: "right",
        4: "bottom", 
        8: "left"
    }
    while not game_over:
        time.sleep(0.5)  # wait a bit before making a new status request
        status = requests.get(SERVER + "/status").json()  # request the status of the game
        if status["status_code"] > 300:
            game_over = True
        
        elif status["status_code"] == 200 + player:  # it's our turn
            print("It's our turn ({}ms left)".format(status["time_left"]))
            # we make a random move => note that this might be an invalid move (segment may be occupied)
            # TODO: figure out a smart move
            find_move = True
            board = status["board"]

            x = random.randint(0,6)
            y = random.randint(0,6)
            border = ["top", "right", "bottom", "left"][random.randint(0,3)]
            while find_move:
                bit = '{0:06b}'.format(board[y][x])
                border_numb = int(bit[-4:], 2)
                if border_numb != 0 and border_numb != 15:
                    if bit[0] == '0' and bit[1] == '0':
                        if border_numb in border_dict:
                            if border[0] == border_dict[border_numb][0]:
                                border = ["top", "right", "bottom", "left"][random.randint(0,3)]
                            else:
                                find_move = False
                        elif border_numb in sum_border_dict:
                            if border[0] in sum_border_dict[border_numb]:
                                border = ["top", "right", "bottom", "left"][random.randint(0,3)]
                            else:
                                find_move = False
                    else:
                        x = random.randint(0,6)
                        y = random.randint(0,6)
                elif border_numb == 15:
                    x = random.randint(0,6)
                    y = random.randint(0,6)
                else:
                    find_move = False
           
            print("Making a move: ({},{}) {}".format(x, y, border))
            move = str(x) + "," + str(y) + "," + border
            status = requests.get(SERVER + "/move/" + TEAM_ID + "/" + move).json()


if __name__ == "__main__":
    player = reg()
    play(player)

    