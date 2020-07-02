"""This module parses a HTTP log file"""

#!/usr/bin python3
# -*- coding: utf-8 -*-

import sys
import time

def http_log_parser():
    """Loads the file into RAM, splits the data
    into primary parts, checks the status code
    parameter and time bounds, then does simple
    arithmetic to find the % of errors for 5xx
    level.

    Args:
        None

    Returns:
        None

    Raises:
        OSError: If file cannot be opened.
    """

    files = []
    line_count = 0
    counter_vimeo_dot_com = 0
    counter_player_dot_vimeo = 0
    counter_api_dot_vimeo = 0

    # User input parameters for data analysis.
    start_time = input("\nStart time (HH:MM:SS):")
    end_time = input("\nEnd time (HH:MM:SS):")
    new_file = input("\nWant to add file for analysis? (y/n):")

    # Checks if the user wants to load file
    # into RAM.
    if new_file in ['y', 'Y']:
        file_name = input("\nFile name: ")

        if file_name not in files:
            files.append(file_name)

        elif file_name in files:
            print("File already exists!")

        else:
            print("Could not upload file!")

    # If user defaults to not load file into
    # memory the program will exit.
    elif new_file in ['n', 'N']:
        print("No file loaded into memory. Exiting...")
        sys.exit()

    # If user does not enter a valid character it will
    # close the program.
    else:
        print("\nInvalid input. Please enter 'y/Y or n/N'")
        sys.exit()

    try:
        for log_file in files:

            # Using 'with' automatically closes the file.
            # Use readlines() as we are not restricted by RAM.
            with open(log_file, 'r', encoding='utf-8') as file_handle:
                file_all_line = file_handle.readlines()

                for line in file_all_line:
                    line_count += 1

                    all_data = line.split('|')
                    epoch_time = float(all_data[0])
                    endpoint = str(all_data[2])
                    status_code = int(all_data[4])
                    epoch_converted = time.strftime('%H:%M:%S', time.gmtime(epoch_time))

                    # Check if 5xx error AND that the time parameter falls into our parameters.
                    if status_code in range(500, 599) and start_time <= epoch_converted < end_time:
                        if endpoint == ' player.vimeo.com ':
                            counter_player_dot_vimeo += 1
                        elif endpoint == ' vimeo.com ':
                            counter_vimeo_dot_com += 1
                        elif endpoint == ' api.vimeo.com ':
                            counter_api_dot_vimeo += 1
                        else:
                            print('Unknown endpoint!')
                            sys.exit()

            # Compute the error percentages.
            errors_endpoint_1 = format(counter_player_dot_vimeo * 100 / float(line_count), '.2f')
            errors_endpoint_2 = format(counter_vimeo_dot_com * 100 / float(line_count), '.2f')
            errors_endpoint_3 = format(counter_api_dot_vimeo * 100 / float(line_count), '.2f')

        print('\nBetween time {} and time {}:'.format(start_time, end_time))
        print('vimeo.com returned {}% 5xx errors'.format(errors_endpoint_2))
        print('player.vimeo.com returned {}% 5xx errors'.format(errors_endpoint_1))
        print('api.vimeo.com returned {}% 5xx errors'.format(errors_endpoint_3))

    # Raise an OSError if the file DNE or cannot be opened
    # for some odd reason.
    except OSError:
        print("File does not exist!")
        sys.exit()

if __name__ == '__main__':
    http_log_parser()
