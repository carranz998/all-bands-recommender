from typing import Any, Callable

import networkx as nx

from api.algorithms.bidirectional_bfs import BidirectionalBFS


def generate_items_flowchart(source_item_id: Any, target_item_id: Any, similar_items_gather: Callable):
    bidirectional_bfs = BidirectionalBFS()

    bidirectional_bfs \
        .search(source_item_id, target_item_id, similar_items_gather)

    items_flowchart = nx \
        .dijkstra_path(bidirectional_bfs.G, source_item_id, target_item_id)

    return items_flowchart
