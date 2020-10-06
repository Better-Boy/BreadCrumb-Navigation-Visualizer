from anytree import Node, RenderTree, LoopError
from anytree.exporter import JsonExporter
import json
import argparse

EXPORTER = JsonExporter(indent=2, sort_keys=True)
NODE_DICT = {}
ERROR_RECORDS = []

def cmd_line_args():
    """
    Method for commond line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputFilePath", required=True, help="Input Text File that contains new line delimited breadcrumbs", dest="inputFile")
    parser.add_argument("--sep", required=True, help="Separator between the levels of the breadcrumbs. Example. '-','/'", dest="sep")
    parser.add_argument("--nodetoexport", required=True, help="Parent Node name and it's children to export to json", dest="node_name")
    parser.add_argument("--outputFilePath", help="Output file to export for visualization", dest="outputFile", default="data.json")
    return parser.parse_args()

def read_input_file(fpath):
    """
    Method to read input file
    """
    return open(fpath).readlines()

def build_tree(input_breadcrumbs, separator):
    """
    Method to build the tree given the breadcrumbs
    """
    for path in input_breadcrumbs:
        try:
            path_nodes = path.strip().split(separator)
            path_nodes_tuple = [(path_nodes[h].strip(), path_nodes[h+1].strip()) for h in range(0, len(path_nodes)-1)]
            for parent, child in path_nodes_tuple:
                if parent not in NODE_DICT.keys():
                    NODE_DICT[parent] = Node(parent)
                if child not in NODE_DICT.keys():
                    NODE_DICT[child] = Node(child)
                NODE_DICT[child].parent = NODE_DICT[parent]
        except Exception as exc:
            print("Error - " + exc)
            ERROR_RECORDS.append({"record":path, "error_message": exc})

def export_node(node_name, outputFileName):
    """
    Once the tree is built, this method exports the given node to a file
    """
    EXPORTER.write(NODE_DICT[node_name], open(outputFileName, "w"))

def save_error_records():
    """
    Saves error records to a file
    """
    json.dump(ERROR_RECORDS, open("error_records.json", "w"))

def start():
    conf = vars(cmd_line_args())
    breadcrumbs = read_input_file(conf["inputFile"])
    build_tree(breadcrumbs, conf["sep"].strip())
    export_node(conf["node_name"], conf["outputFile"])
    save_error_records()

if __name__ == "__main__":
    start()
