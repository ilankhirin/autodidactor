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

var cy = cytoscape({
  container: document.getElementById('cy'),

  boxSelectionEnabled: false,
  autounselectify: true,

  style: cytoscape.stylesheet()
    .selector('node')
    .css({
      'content': 'data(id)'
    })
    .selector('edge')
    .css({
      'curve-style': 'bezier',
      'target-arrow-shape': 'triangle',
      'width': 4,
      'line-color': '#ddd',
      'target-arrow-color': '#ddd'
    })
    .selector('.highlighted')
    .css({
      'background-color': '#61bffc',
      'line-color': '#61bffc',
      'target-arrow-color': '#61bffc',
      'transition-property': 'background-color, line-color, target-arrow-color',
      'transition-duration': '0.5s'
    }),

  elements: {
    nodes: getNodes(connectionsData),
    edges: getEdges(connectionsData)
    // nodes: [
    //   { data: { id: 'a' } },
    //   { data: { id: 'b' } },
    //   { data: { id: 'c' } },
    //   { data: { id: 'd' } },
    //   { data: { id: 'e' } }
    // ],

    // edges: [
    //   { data: { id: 'a"e', weight: 1, source: 'a', target: 'e' } },
    //   { data: { id: 'ab', weight: 3, source: 'a', target: 'b' } },
    //   { data: { id: 'be', weight: 4, source: 'b', target: 'e' } },
    //   { data: { id: 'bc', weight: 5, source: 'b', target: 'c' } },
    //   { data: { id: 'ce', weight: 6, source: 'c', target: 'e' } },
    //   { data: { id: 'cd', weight: 2, source: 'c', target: 'd' } },
    //   { data: { id: 'de', weight: 7, source: 'd', target: 'e' } }
    // ]
  },

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
  debugger
  for (source in data) {
    for (target in data[source]) {
      edges.push({
        data: {
          id: source + "_" + target,
          weight: data[source][target],
          source: source,
          target: target
        }
      });
    }
  }

  debugger
  return edges;
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