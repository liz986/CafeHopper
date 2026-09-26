# Project Title - CaféHopper

#### Description:

     About this project:

     CaféHopper is a tool that makes planning itineraries for a day out easier!
     Based on user input, a tailored itinerary is formed and printed out that displays all essential details about each of the mentioned
     cafes.

     The user is asked to choose options from among different criteria:
     The travel time taken may be a dealbreaker for some cafes which is why the users can choose to be provided with cafes that are less
     than a certain time interval away.
     They can also choose to stick with a certain theme for all the cafes.
     If they are interested in exploring cafes with a certain specialty, this can be filtered out too.
     Also, an option is provided for when they don't have a particular preference!


     What each file included in this project does:

     project.py -
     Contains the main code for the project.
     Uses imported tabulate library
     Contains a main method:

     main() - Displays a table prompting users to make a choice based on the duration of travel they are interested in, accepts
              the choice and passes it to its respective function.
              Does the same for users to input choices for desired theme and specialty.

              Accepts lists from the three functions and converts them to sets so that the intersection of the three sets provides
              us with the set of cafes that meet all the requirements. This set is later converted to a list.

              If this final list is empty, a statement is printed out saying that an itinerary based on the earlier requirements chosen
              could not be made. Else, the final itinerary is printed out displaying the name of each of the cafes, how many minutes
              away each is from the user, what theme this cafe incorporates, and what the specialty of the cafe is.

     and three additional methods which are:

     filter_time(ch) - Accepts as input a choice from the user which is passed through the main method.
                       Contains a for loop and match case to check for and filter out options that meet the criteria for the choice
                       passed in.
                       Returns list of cafes that meet the requirements for the time constraint chosen.

     filter_theme(ch) - Accepts as input a choice from the user which is passed through the main method.
                        Contains a for loop and match case to check for and filter out options that meet the criteria for the choice
                        passed in.
                        Returns list of cafes that belong to a specific theme the user decides.

     filter_specialty(ch) - Accepts as input a choice from the user which is passed through the main method.
                            Contains a for loop and match case to check for and filter out options that meet the criteria for the
                            choice passed in.
                            Returns list of cafes that have the same specialty the user wants.


     test_project.py -
     Uses imported pytest library
     Also imports filter_time, filter_theme and filter_specialty from project.py for testing.


     requirements.txt -
     Lists the pip installable packages used

#### Date Completed:  5 September 2025

TODO
