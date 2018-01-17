import itertools

#canvas keys
#0 1 2
#3 4 5
#6 7 8

#canvas example
#x o x
#x o o
#x x o

#setting the rules to match the canvas keys, to avoid row and column pair
#where 'x' for example is : row , column
#[ 0 , 0 ] = 0 + 0                   = 0 row + column
#[ 0 , 2 ] = 0 + 2                   = 2
#[ 1 , 0 ] = if row == 1 row = 3 + 0 = 3 row and step = 3 because canvas lenght in this case is 3
#[ 2 , 0 ] = if row == 2 row = 6 + 0 = 6
#[ 2 , 1 ] = if row == 2 row = 6 + 1 = 7

def build_rules(canvas):
  step = -len(canvas)
  rules = []
  for index in range(len(canvas)):
    step+=len(canvas)
    rules.append(step)
  #output rules example if canvas 3x3 = [0,3,6]

  return rules

def build_winners(canvas):
  #horizontal wins
  wins = []
  for row, items in enumerate(canvas):
    win = []
    for column, item in enumerate(items):
      win.append(rules[row] + column)
    wins.append(win)

  #vertical wins
  for column, item in enumerate(canvas):
    win = []
    for row, items in enumerate(item):
      win.append(rules[row] + column)
    wins.append(win)

  #diagonal wins
  canvas_lenght = len(canvas)
  first_diagonal = []
  second_diagonal = []
  j_index = canvas_lenght - 1
  for index in range(canvas_lenght):
    first_diagonal.append(rules[index] + index)
    second_diagonal.append(rules[index] + j_index)
    j_index-=1
  wins.append(first_diagonal)
  wins.append(second_diagonal)
  #output [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
  return wins


def get_position(canvas, x_or_o):
  position = []
  for row, items in enumerate(canvas):
    for column, item in enumerate(items):
      if x_or_o in item:
        position.append(rules[row] + column)
  #output example if 'x' [0,2,3,6,7]
  #output example if 'o' [1,4,5,8]
  return position
def check_winner(position,canvas):
  """check all possible combinations with the lenght = 3 in this case
     for example we have [0,2,3,6,7]
     so the combinations would be
    [[0, 2, 3], [0, 2, 6], [0, 2, 7], [0, 3, 6], [0, 3, 7], [0, 6, 7], [2, 3, 6], [2, 3, 7], [2, 6, 7], [3, 6, 7]]
  """
  winner = []
  for L in range(0, len(position)+1):
    for subset in itertools.combinations(position, L):
      if len(subset) == len(canvas):
        """the subset looks like (0, 2, 3) so we need
            to break it by element and create a list of the elements
            to have a list like [0, 2, 3]
        """
        fix_subset=[]
        for subset_element in subset:
          fix_subset.append(subset_element)
        winner.append(fix_subset)
  return winner

def show_result():
  winners = build_winners(canvas)

  x_position = get_position(canvas, 'x')
  o_position = get_position(canvas, 'o')

  x_winner = check_winner(x_position, canvas)
  o_winner = check_winner(o_position, canvas)
  is_winner = False
  for item in x_winner:
    if item in winners:
      print('x won at ', item)
      is_winner = True
  if not is_winner:
    for item in o_winner:
      if item in winners:
        print('o won at ', item)
        is_winner = True
  if not is_winner:
    print('draw')

canvas = [['x','o','x'],
          ['x','o','o'],
          ['x','x','o']]
#canvas = [['x','o','x','o'], ['o','x','o','x'], ['x','o','x','o'], ['x','o','x','x']] #if you want to try with a 4x4
rules = build_rules(canvas)
show_result()
#output x won at  [0, 3, 6]

