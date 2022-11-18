import os
from CastVote import CastVote

DATA_FOLDER = "C:/Users/daved/bin/election_audits/data"
EXAMPLE_FILE = os.path.join(DATA_FOLDER, "1_000f90b5-0bc7-4718-baf0-0ae9f33a70f5.xml")


def get_all_xml_files(folder=DATA_FOLDER):
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename[-4:].lower() == ".xml":
                yield os.path.join(root, filename)


def get_list_of_cast_votes(max=9999999):
    list_of_cast_votes = []
    count = 0
    for xml_file in get_all_xml_files(DATA_FOLDER):
        cast_vote = CastVote(xml_file)
        list_of_cast_votes.append(cast_vote)
        count += 1
        if count == max:
            break

    return list_of_cast_votes

if __name__ == "__main__":
    list_of_votes = get_list_of_cast_votes(max=100)
    for vote in list_of_votes:
        print(vote)