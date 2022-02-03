'''
  * ***************************************************************
  *      Program: MATSim Data Generator
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ***************************************************************
'''

# Libraries
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import argparse
import datetime
from halo import Halo
import math
import pandas as pd
import platform


class MATSimDataGenerator:

    # Function: Constructor
    def __init__(self):

        # Build Halo spinner
        self.systemResponse = Halo(spinner='dots')

        # Build parser element
        parser = argparse.ArgumentParser()
        parser.add_argument("--output", "-o", default="./database_fix.csv", help="Database fixed output file.")
        parser.add_argument("--database", "-d", default="./resources/database.csv",
                            help="Input database file to adapt with coordinates system reference.")

        # Parse arguments
        args = parser.parse_args()
        self.output = args.output
        self.database = args.database

    # Function: getSystemPlatform
    def getSystemPlatform(self):

        # Get system configuration
        print("\nDetecting system and release version ...\n")
        systemPlatform = platform.system()
        systemRelease = platform.release()

        print("**************************************************************************")
        print("Configuration detected:")
        print("**************************************************************************")
        print("\nPlatform:")
        print(systemPlatform)
        print("Release:")
        print(systemRelease)

        return systemPlatform, systemRelease

    # Function: getDatabase
    def getDatabase(self):

        # Read from file
        database = pd.read_csv(str(self.database), sep=";")

        return database

    # Function: getDatabaseParams
    def getDatabaseParams(self, database):

        # Get database columns
        x_init = []
        y_init = []

        # Fix x, y coordinate init to zero
        for i in range(int(len(database.DISTANCIA_VIAJE))):

            coordinate = 0
            x_init.append(coordinate)
            y_init.append(coordinate)

        # Get x, y coordinate distance module
        x_end = []
        y_end = []

        # Fix x, y coordinate end to module component
        for (element, i) in zip(database.DISTANCIA_VIAJE, range(int(len(database.DISTANCIA_VIAJE)))):

            element = element.replace(",", ".")
            coordinate = float(element) * (math.sqrt(0.5))
            coordinate = str(coordinate)
            coordinate = coordinate[:4]
            coordinate = float(coordinate)
            x_end.append(coordinate)
            y_end.append(coordinate)

        # Get time init and end
        time_init = []
        time_end = []

        # Get travel time init
        for (element, i) in zip(database.VORIHORAINI, range(int(len(database.VORIHORAINI)))):

            element = str(element)
            time_value = element[:-2] + ":" + element[int(len(element))-2:]
            time_init.append(time_value)

        # Get travel time end
        for (element, i) in zip(database.VDESHORAFIN, range(int(len(database.VDESHORAFIN)))):

            element = str(element)
            time_value = element[:-2] + ":" + element[int(len(element))-2:]
            time_end.append(time_value)

        # Get time duration
        duration = []

        # Get time travel duration
        for (i, times_start, times_finish) in zip(range(int(len(database.VDESHORAFIN))), database.VORIHORAINI, database.VDESHORAFIN):

            times_start = int(times_start)
            times_finish = int(times_finish)
            time_duration = times_finish - times_start
            duration.append(time_duration)

        return x_init, x_end, y_init, y_end, time_init, time_end, duration

    # Function: generateDatabase
    def generateDatabase(self, x_init, x_end, y_init, y_end, time_init, time_end, duration):

        # Generate database
        database = pd.DataFrame({'X_INIT': x_init, 'X_DEST': x_end, 'Y_INIT': y_init, 'Y_DEST': y_end, 'TIME_INIT': time_init, 'TIME_DEST': time_end, 'DURATION': duration})

        print("Generated database:\n")
        print(database)

        return database

    # Function: saveDatabase
    def saveDatabase(self, database):

        # Save database adapted
        database.to_csv(str(self.output), sep=";", index_label=False)

    # Function: processRequests
    def processRequests(self, x_init, x_end, y_init, y_end, time_init, time_end, duration):

        print("\n**************************************************************************")
        print("Processing request:")
        print("**************************************************************************\n")

        try:
            # Get initial time
            initialTime = datetime.datetime.now()

            # Generate database
            database = self.generateDatabase(x_init, x_end, y_init, y_end, time_init, time_end, duration)

            # Save into file
            self.saveDatabase(database)

            systemResponseMessage = "\n[INFO] Request done correctly.\n"
            self.systemResponse.text_color = "green"
            self.systemResponse.succeed(systemResponseMessage)

            # Get end time
            endTime = datetime.datetime.now()

            # Compute elapsed time
            elapsedTime = endTime - initialTime

            systemResponseMessage = "\n[INFO] Elapsed time: " + str(elapsedTime) + ".\n"
            self.systemResponse.text_color = "blue"
            self.systemResponse.info(systemResponseMessage)

        except:
            systemResponseMessage = "\n[ERROR] Error, processing request.\n"
            self.systemResponse.text_color = "red"
            self.systemResponse.fail(systemResponseMessage)


# Function: main
def main():

    print("**************************************************************************")
    print("**************************************************************************")
    print("                    Program: MATSim Data Generator                        ")
    print("                     Author: David Velasco Garcia                         ")
    print("                             @davidvelascogarcia                          ")
    print("**************************************************************************")
    print("**************************************************************************")

    print("\nLoading MATSim Data Generator engine ...\n")

    # Build matsimDataGenerator object
    matsimDataGenerator = MATSimDataGenerator()

    # Get system platform
    systemPlatform, systemRelease = matsimDataGenerator.getSystemPlatform()

    # Read database
    database = matsimDataGenerator.getDatabase()

    # Get database params
    x_init, x_end, y_init, y_end, time_init, time_end, duration = matsimDataGenerator.getDatabaseParams(database)

    # Process input requests
    matsimDataGenerator.processRequests(x_init, x_end, y_init, y_end, time_init, time_end, duration)

    print("**************************************************************************")
    print("Program finished")
    print("**************************************************************************")
    print("\nmatsimDataGenerator program finished correctly.\n")

    #userExit = input()


if __name__ == "__main__":

    # Call main function
    main()