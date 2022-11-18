from xml.etree import ElementTree


class CastVote:
    records = []
    batchSequence = None
    sheetNumber = None
    precinctSplit = None
    batchNumber = None
    CvrGuid = None

    def __init__(self, cvr_filepath):
        cast_vote_record = ElementTree.parse(cvr_filepath)
        cast_vote_tree = cast_vote_record.getroot()
        for child in cast_vote_tree:
            if "Contests" in child.tag:
                self.getContests(child)
            elif "BatchSequence" in child.tag:
                self.getBatchSequence(child)
            elif "SheetNumber" in child.tag:
                self.getSheetNumber(child)
            elif "PrecinctSplit" in child.tag:
                self.getPrecinctSplit(child)
            elif "BatchNumber" in child.tag:
                self.getBatchNumber(child)
            elif "CvrGuid" in child.tag:
                self.getCvrGuid(child)

    def getContests(self, tree):
        for contest in tree:
            self.records.append(self.getSingleContest(contest))

    def getSingleContest(self, tree):
        contest_data = {}
        contest_name = ""
        for child in tree:
            if "Name" in child.tag:
                contest_name = child.text
                if child.text not in contest_data.keys():
                    contest_data[contest_name] = []
                break

        for child in tree:
            if "Options" in child.tag:
                for option in child:
                    #print(option.tag)
                    name = ""
                    value = "0"
                    for data_point in option:
                        #print(data_point.tag)
                        if "Name" in data_point.tag:
                            name = data_point.text
                            #print(name)
                        elif "Value" in data_point.tag:
                            value = data_point.text
                    if value != "0":
                        contest_data[contest_name].append(name)

        return contest_data

    def getBatchSequence(self, tree):
        self.batchSequence = tree.text

    def getSheetNumber(self, tree):
        self.sheetNumber = tree.text

    def getPrecinctSplit(self, tree):
        for child in tree:
            if "Name" in child.tag:
                self.precinctSplit = child.text

    def getBatchNumber(self, tree):
        self.batchNumber = tree.text

    def getCvrGuid(self, tree):
        self.CvrGuid = tree.text

    def __str__(self):
        string = ""
        string += f"Batch Sequence: \t\t{self.batchSequence}\n"
        string += f"Sheet Number: \t\t{self.sheetNumber}\n"
        string += f"Precinct: \t\t{self.precinctSplit}\n"
        string += f"Batch Number: \t\t{self.batchNumber}\n"
        string += f"Selections:\n"
        for record in self.records:
            for contest_name in record.keys():
                sanitized_contest_name = contest_name.replace('\n', ' ')
                string += f"\t\t{sanitized_contest_name}\n\t\t\t{record[contest_name]}\n"

        return string

