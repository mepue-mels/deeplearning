##preprocessors.py

##usage: formats the output of the outline generation model
##returns: string

def format_outline(output):
    # Split the output into different sections
    lines = output.split(". ")

    # Extract the week and topic
    header = lines[0].split(" - ")
    week = header[0].strip()
    title = header[1].strip()

    # Prepare formatted output
    formatted_output = f"{week} {title}\n\n"

    # Extract objectives
    objectives_start = output.find("The objectives are:") + len("The objectives are:")
    objectives_end = output.find("The subtopics include:")
    objectives = output[objectives_start:objectives_end].strip()

    # Remove the numbers and add a dash for each objective
    formatted_output += "Objectives:\n"
    objective_lines = objectives.split(". ")
    for obj in objective_lines:
        # Strip out numbers like '1.', '2.' from objectives
        obj = obj.lstrip('1234567890. ').strip()
        if obj:
            formatted_output += f"- {obj}.\n"

    # Extract subtopics
    subtopics_start = output.find("The subtopics include:") + len("The subtopics include:")
    subtopics_end = output.find("The activities involve:")
    subtopics = output[subtopics_start:subtopics_end].strip()
    subtopics_list = subtopics.split(";")

    formatted_output += "\nSubtopics:\n"
    for subtopic in subtopics_list:
        if subtopic.strip():
            formatted_output += f"- {subtopic.strip()}\n"

    # Extract activities
    activities_start = output.find("The activities involve:") + len("The activities involve:")
    activities_end = output.find("Technologies utilized:")
    activities = output[activities_start:activities_end].strip()

    formatted_output += "\nActivities:\n"
    formatted_output += f"{activities}\n"

    # Extract technologies
    technologies_start = output.find("Technologies utilized:") + len("Technologies utilized:")
    technologies = output[technologies_start:].strip()

    formatted_output += "\nTechnologies Utilized:\n"
    formatted_output += f"{technologies}\n"

    return formatted_output
