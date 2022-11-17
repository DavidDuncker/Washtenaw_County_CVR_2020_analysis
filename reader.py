import main
import xml
from xml.etree import ElementTree

DATA_FOLDER = main.DATA_FOLDER
EXAMPLE_FILE = main.EXAMPLE_FILE


def recursively_parse_cvr_data(element_tree):
    pass


def do(cast_vote_filepath):
    cast_vote_tree = ElementTree.parse(cast_vote_filepath)
    cast_vote_root = cast_vote_tree.getroot()

    file = open(EXAMPLE_FILE, 'r')

