var connectionsData = {
  "css": {
    "html": 547,
    "javascript": 339,
    "json": 20,
    "promise": 0
  },
  "html": {
    "css": 383,
    "javascript": 291,
    "json": 13,
    "promise": 0
  },
  "javascript": {
    "css": 282,
    "html": 260,
    "json": 17,
    "promise": 1
  },
  "json": {
    "css": 400,
    "html": 363,
    "javascript": 627,
    "promise": 0
  },
  "promise": {
    "css": 55,
    "html": 42,
    "javascript": 945,
    "json": 20
  }
};

var nodes = getNodes(connectionsData);
var edges = getEdges(connectionsData);

var cy = cytoscape({
  container: document.getElementById('cy'),
  elements: {
    nodes: nodes,
    edges: edges
  },
  style: cytoscape.stylesheet()
    .selector('node')
    .css({
      'content': 'data(id)',
      'width': 100,
      'height': 100
    }),
  layout: {
    name: 'breadthfirst',
    directed: true,
    roots: '#a',
    padding: 10
  }
});

function getNodes(data) {
  var nodes = [];
  for (pageContainer in data) {
    nodes.push({ data: { id: pageContainer } });
  }

  return nodes;
}

function getEdges(data) {
  var edges = [];

  for (source in data) {
    for (target in data[source]) {
      edges.push({
        data: {
          id: source + "_" + target,
          weight2: data[source][target],
          source: source,
          target: target
        }
      });
    }
  }

  return edges;
}

function styleNode(node) {

}

// var bfs = cy.elements().bfs('#a', function(){}, true);

// var i = 0;
// var highlightNextEle = function(){
//   if( i < bfs.path.length ){
//     bfs.path[i].addClass('highlighted');

//     i++;
//     setTimeout(highlightNextEle, 1000);
//   }
// };

// // kick off first highlight
// highlightNextEle();