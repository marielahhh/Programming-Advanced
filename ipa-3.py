'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if from_member in social_graph and to_member in social_graph:
        from_to = to_member in social_graph[from_member]["following"]
        to_from = from_member in social_graph[to_member]["following"]

        if from_to and to_from:
            return "friends"
        elif from_to:
            return "follower"
        elif to_from:
            return "followed by"
        else:
            return "no relationship"

   


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    for row in board:
        if row.count("X") == len(board):
            return "X"
        elif row.count("O") == len(board):
            return "O"

    for col in range(len(board[0])):
        result = ""
        for row in range(len(board)):
            result += board[row][col]
        if result.count("X") == len(board):
            return "X"
        elif result.count("O") == len(board):
            return "O"

   
    result2 = ""
    for i in range(len(board)):
        result2 += board[i][i]
    if result2 == "X" * len(board):
        return "X"
    elif result2 == "O" * len(board):
        return "O"


    result3 = ""
    for i in range(len(board)):
        result3 += board[i][len(board) - 1 - i]
    if result3 == "X" * len(board):
        return "X"
    elif result3 == "O" * len(board):
        return "O"

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    travel_time = 0
    present_stop = first_stop
    for (from_stop, to_stop) in route_map:
        if present_stop == second_stop:
            travel_time += route_map[(from_stop, to_stop)]["travel_time_mins"]
    while present_stop != second_stop:
        for (from_stop, to_stop) in route_map:
            if from_stop == present_stop:
                travel_time += route_map[(from_stop, to_stop)]["travel_time_mins"]
                present_stop = to_stop
                break
    
    return travel_time
