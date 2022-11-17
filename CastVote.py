from xml.etree import ElementTree


class CastVote:
    contests = []
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
            self.contests.append(self.getSingleContest(contest))

    def getSingleContest(self, tree):
        contest_data = {}
        contest_data["options"] = []

        for child in tree:
            if "Name" in child.tag:
                contest_data["name"] = child.text
            elif "Options" in child.tag:
                for option in child:
                    name = ""
                    value = "0"
                    for data_point in option:
                        if "Name" in data_point:
                            name = data_point.text
                        elif "Value" in data_point:
                            value = data_point.text
                    if value != "0":
                        contest_data["options"].append(name)

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