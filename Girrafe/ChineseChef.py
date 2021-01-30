import chef
import newchef

# to use inheritance first import files then put it inside function in chinese chef

# on this one if you inherit from two classes with the same function name then the first one or the oldest child will get picked over the last child
# in this one if i put Chef first then the make_chicken function will get executed by the first chef
# if newChef first then the new chef will create the chicken
# so the inheritance order is based on the input first until last


class chineseChef(chef.Chef, newchef.newChef):
    def make_special_dish(self):
        print("The chef makes Orange Chicken")

    def make_fried_rice(self):
        print("The chef makes Fried Rice")
