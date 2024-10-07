def read_releases(filename):
    """ Reads the releases(data) from the input file and returns a list of tuples.
    Each tuple contains (delivery_day, validation_duration)"""
    releases = []
    with open(filename, 'r') as file:
        for line in file:
            delivery_day, validation_duration = map(int, line.strip().split())
            releases.append((delivery_day, validation_duration))
    return releases


def write_solution(filename, max_releases, schedule):
    """ Writes the solution to the output file.First line contains the number of releases,
    followed by the schedule of the validated releases"""
    with open(filename, 'w') as file:
        file.write(f"{max_releases}\n")
        for start_day, end_day in schedule:
            file.write(f"{start_day} {end_day}\n")


def select_max_releases(releases):
    """Selects the maximum number of releases that can be validated within the sprint
    Returns the number of releases and their validation schedule"""
    # Sort the releases by delivery day, and then by validation duration for ties
    releases.sort(key=lambda x: (x[0], x[1]))

    schedule = []
    current_day = 0

    for release in releases:
        delivery_day, validation_duration = release

        # Check if we can start validating on delivery_day and complete within the sprint
        if delivery_day + validation_duration - 1 <= 10 and delivery_day >= current_day:
            # Bob starts the validation on delivery_day
            start_day = delivery_day
            end_day = start_day + validation_duration - 1

            # Add this release to the schedule
            schedule.append((start_day, end_day))
            current_day = end_day + 1  # Next validation can start after the current one finishes

    # Return the number of validated releases and the schedule
    return len(schedule), schedule


def main():
    # name of the Input and output file names
    input_file = 'releases.txt'
    output_file = 'solution.txt'

    # Read the releases from the input file
    releases = read_releases(input_file)

    # To Select the maximum number of releases that can be validated within the sprint
    max_releases, schedule = select_max_releases(releases)

    # solution to the output file
    write_solution(output_file, max_releases, schedule)


if __name__ == '__main__':
    main()
