import streamlit as st
import networkx as nx
import graphviz
def output_nodes_and_edges(graph:nx.Graph):
    st.write(graph.nodes)
    st.write(graph.edges)

def count_nodes(graph:nx.Graph):
    num_nodes = len(graph.nodes)
    st.write(f"the Graph has", num_nodes, "of nodes")
    #st.write(graph.number_of_nodes())

def count_edges(graph = nx.Graph):
    num_edges = len(graph.edges)
    st.write(f"the Graph has", num_edges, "of edges")
    #st.write(graph.number_of_edges())

def specific_edge(G = nx.Graph):

    node1_col, node2_col = st.columns(2)
    graph_dict = st.session_state["graph_dict"]
    node_list = graph_dict["nodes"]
    edge_list = graph_dict["edges"]

    node_list = st.session_state["node_list"]
    node_name_list = []
    for node in node_list:
        node_name_list.append(node["name"])
    with node1_col:
        node1_select = st.selectbox(
            "select the first node",
            options=node_name_list,
            key="node1_select"  # can be added
        )
    with node2_col:
        node2_select = st.selectbox(
            "select the second node",
            options=node_name_list,
            key="node2_select"  # can be added
        )
    for edge in edge_list:
        # if node1_select in edge_list:
        for node1_select in edge_list:
            source = edge["source"]
        for node2_select in edge_list:
            target = edge["target"]
        if G.has_edge(source, target) in edge_list:
            relation = edge["type"]

            st.write(f"{node1_select} is {relation} {node2_select}")

def density_graph(graph:nx.Graph):

    n = graph.number_of_nodes()
    m = graph.number_of_edges()
    if m == 0 or n <= 1:
        return 0
    d = m / (n * (n - 1))
    if not graph.is_directed():
        d *= 2
    return d
    st.write(d)


def show_shortest_paths(graph: nx.DiGraph):
    # Retrieve graph data from session state
    graph_dict_tree = st.session_state["graph_dict"]

    # Extract node and edge lists from the graph data
    node_list_tree = graph_dict_tree["nodes"]
    edge_list_tree = graph_dict_tree["edges"]

    # Initialize lists to store found nodes and edges related to the shortest paths
    node_list_tree_found = []
    edge_list_tree_found = []

    # Extract the names of nodes from the node list
    node_name_list_tree = [node["name"] for node in node_list_tree]

    # Present a selection box to choose the start node for calculating the shortest paths
    start_node_select_tree = st.selectbox(
        "Select the start node of the shortest paths",
        options=node_name_list_tree
    )

    end_node_select_tree = st.selectbox(
        "Select the end node of the shortest paths",
        options=node_name_list_tree
    )

    # Present a button to trigger the calculation of shortest paths when clicked
    is_tree_button = st.button("Calculate trees", use_container_width=True, type="primary")

    # If the button is clicked
    if is_tree_button:
        # Calculate the shortest paths using NetworkX's shortest_path function
        tree_list = nx.shortest_path(graph, source=start_node_select_tree, target=end_node_select_tree, weight="dist")

        # Check if any shortest paths exist from the selected start node
        if not tree_list:
            st.write(f"There is no tree starting from {start_node_select_tree}.")
        else:
            # Iterate through each tree in the list of shortest paths
            for tree in tree_list:
                st.write(f"The node {tree} is a member of the tree")
                # For each node in the tree, identify the corresponding node data from the original node list
                for tree_element in tree:
                    for node_element in node_list_tree:
                        if node_element["name"] == tree_element:
                            to_be_assigned_element = node_element
                            # Add the node to the list of found nodes if it's not already there
                            if to_be_assigned_element not in node_list_tree_found:
                                node_list_tree_found.append(node_element)

            # Iterate through each edge in the original edge list
            for edge_element in edge_list_tree:
                for source in node_list_tree_found:
                    for target in node_list_tree_found:
                        # Check if both source and sink nodes of the edge are in the list of found nodes
                        if edge_element["source"] == source["name"] and edge_element["target"] == \
                                target["name"]:
                            # Add the edge to the list of found edges
                            edge_list_tree_found.append(edge_element)

            # Display the graph without considering the weights of the edges
            show_graph_without_weights(node_list_tree_found, edge_list_tree_found)


# Function to display the graph without considering edge weights
def show_graph_without_weights(nodes, edges):
    # Implement visualization logic here (not included for brevity)
        pass
