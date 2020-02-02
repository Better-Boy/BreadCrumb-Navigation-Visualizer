# BreadCrumb-Visualizer

This repository contains code for visualization of breadcrumbs as seen in the ecommerce websites.

### What are breadcrumbs navigation?
Breadcrumb Navigation is a form of site navigation that shows visitors where they are on a site's hierarchy of pages without having to examine a URL structure


### How to create the visualization?
Put all the breadcrumb navigation in a text file. Every breadcrumb navigation should be in a new line. 

1. Install `anytree` package from pip. Run the command 
   `pip install anytree`
2. Run the python program with the following command
  `python tree_generator.py --inputFilePath breadcrumbs.txt --sep "/" --nodetoexport "Home"` 
   
   Argument Explanation:
   1. --inputFilePath - Input file containing new line delimited breadcrumb navigations
   2. --sep - Separator between the nodes of a breadcrumb navigation
   3. --nodetoexport - which node and it's corresponding children to export to json format
3. After you run the python file, 2 json files are generated.
   1. data.json - Json representation of the tree
   2. error_records.json - breadcrumb navigations that encountered Error during it's adding/conversion to the tree
4. Run a python server from the current working directory where `index.html` and `data.json` is found. 
   Run the command - `python -m http.server`
5. Open `http://localhost:8000/` to view the visualization


### Functionalities supported:
1. Search Node - Searches a given node in whole tree
2. Highlight Navigation Path to the node from the root


The visualization for the sample data in the repository can be found at - https://better-boy.github.io/BreadCrumb-Navigation-Visualizer/
