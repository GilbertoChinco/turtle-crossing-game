setup = {
    "width": 400,
    "height": 400,
    "min_lim": -150,
    "max_lim": 150,
    "difficult": {
        "easy": {
            "number": 5,
            "min_speed": 1,
            "max_speed": 5
        },
        "medium": {
            "number": 10,
            "min_speed": 5,
            "max_speed": 10
        },
        "hard": {
            "number": 15,
            "min_speed": 8,
            "max_speed": 15
        }
    }
}
#
def generate_positions(min_lim, max_lim, n):
    step = int((max_lim - min_lim) / n)
    obstacle_positions = [(300, i) for i in range(min_lim, max_lim, step)]
    return obstacle_positions