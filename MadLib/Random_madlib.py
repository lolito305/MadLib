import random
from MadLib import A_Day_at_the_Silly_Circus_Madlib, The_Hilarious_Haunted_House

if __name__ =="__main__":
    m = random.choice([A_Day_at_the_Silly_Circus_Madlib, The_Hilarious_Haunted_House])
    m.madlib()