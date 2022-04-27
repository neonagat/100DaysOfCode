# Hurdle 1

# Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def running_jump(times):
#     for i in range(times):
#         move()
#         turn_left()
#         move()
#         turn_right()
#         move()
#         turn_right()
#         move()
#         # no need for a turn after the last hurdle
#         if i < times - 1:
#             turn_left()
#
# running_jump(6)

# Hurdle 2

# Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def running_jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     # no need for this turn once the finish is reached
#     if not at_goal():
#         turn_left()
#
# while not at_goal():
#     running_jump()

# Hurdle 3

# Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     # no need for this turn once the finish is reached
#     if not at_goal():
#         turn_left()
#
# while not at_goal():
#     while front_is_clear():
#         move()
#     jump()

# Hurdle 4

# Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
# Also valid for Hurdle 1, Hurdle 2 & Hurdle 3.

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def variable_jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     # "fall" until you hit the ground
#     while front_is_clear():
#         move()
#     # no need for this turn once the finish is reached
#     if not at_goal():
#         turn_left()
#
# while not at_goal():
#     while front_is_clear():
#         move()
#     variable_jump()

# Maze

# Copy-paste this to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()









