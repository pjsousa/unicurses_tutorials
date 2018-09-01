import curses

instances = []
colors = []

def place_meeting(the_object):
	global instances

	found = False

	for instance in instances:
		if instance is the_object:
			continue
		else:
			if the_object.x >= instance.x and the_object.y >= instance.y \
			and the_object.x < instance.w and the_object.y < instance.h:
				possible_instance = instance
				found = True

	if found:
		return (True, possible_instance.background)
	else:
		return False



global_color_number = 1
def make_color(foreground, background):
  global global_color_number, colors

  if (foreground, background) in colors:
  	return colors.index((foreground, background)) + 1

  color_number = global_color_number
  curses.init_pair(color_number, foreground, background)
  global_color_number += 1

  colors.append((foreground, background))

  return color_number

