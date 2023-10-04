def game_broadcast(boradcast_message):
    broadcast_messages={
        "D&D":"You have selected D&D a fantasy adventure role playing game filled with magical beasts, villains, and heroes. The Dungeon master will be right with you. Have fun!",
        "Cyberpunk":"You have selected Cyberpunk a dark future dystopian role playing game full of cyber criminals, mega corporations and corrupt government. The game master will be right with you. Have fun!",
        "Scifi":"You have selected Scifi a futuristic role playing game full of aliens, robots, and space travel. The game master will be right with you. Have fun!"
    }
    try:
        broadcast = broadcast_messages[boradcast_message]
        print(broadcast)
    except KeyError:
        return False
    return True
    