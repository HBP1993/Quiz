import weaponClass as w
import csv



#Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.


#Create an instance of the weapon object for each record.


#Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value.d = {}


# - Print out details of each weapon using the object's methods only (as per comments below). 
# - Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
# - Print out the name of the weapon and the number of bullets from the dictionary.

# HINT: Follow the comments for each line to help with the logic of the problem.



# create a file object to open the file in read mode
weapon_file = open('Weapons.csv', "r")


# create a csv object from the file object
weapon_file_reader = csv.reader(weapon_file, delimiter = ',')


#skip the header row
next(weapon_file_reader)


#create an empty dictionary named 'weapons_dict'
d = {}


#use a for loop to iterate through every row of the csv file
for line in weapon_file_reader:
    #use variables for name,speed and range (optional)
    name = line[0]
    speed = line[1]
    range_ = line[2]

    # create an instance of the weapon object using the 
    # specs from the csv file (name,speed and range) 
    my_weapon = w.weapon(name, speed, range_)

    # append the name and bullet count to 'weapons_dict'
    d[my_weapon.get_name()] = my_weapon.get_bullets


    # print out the name of the weapon using the appropriate method of the object 
    print('The Weapon name is ', my_weapon.get_name())
    
    # print out the speed of the weapon using the appropriate method of the object
    print('The Weapon speed is ', my_weapon.get_speed())
    
    # print out the range of the weapon using the appropriate method of the object
    print('The Weapon range is ', my_weapon.get_range())
    
    # print out the number of bullets of the weapon using the appropriate method of the object
    print('The number of bullets are ', my_weapon.get_bullets())

    #use an input statement to halt the program and wait for the user - 
    fire_weapon = input("Press any key to fire the weapon")
    print(fire_weapon)
    
    
    
    

    # use an appropriate loop to keep firing the weapon until all bullets run out
    for bullets_ in range(my_weapon.get_bullets()):
        # call the appropriate method to fire a bullet
        my_weapon.fire_bullet()

        # print out the bullet count every time the weapon is fired
        print(my_weapon.get_bullets(), end='\r')
        

    


#using a loop print out the name and number of bullets from the dictionary
for i, value in d.items():
    print(f"name: " + i + "bullets: " + str(value))
    



    


    



