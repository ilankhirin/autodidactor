
var graphData = {
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
// create an array with nodes

function getNodes(graphData) {
  var nodeSizes = calculateNodeSizes(graphData);
  var nodes = [];
  var nodesLables = Object.keys(graphData);
  for (var i = 0; i < nodesLables.length; i++) {
    nodes.push({
      id: i+1,
      label: nodesLables[i],
      font : {
        size: nodeSizes[nodesLables[i]]
      }
    });
  }
  return nodes;
}

function getEdges(graphData, nodesDictionary) {
  var edges = [];    
  for (var sourceNode in graphData) {
    for (var targetNode in graphData[sourceNode]) {
        var connectionsCount = graphData[sourceNode][targetNode];
        if (connectionsCount > 0) {
          edges.push({
            from: nodesDictionary[sourceNode],
            to: nodesDictionary[targetNode],
            arrows: 'to',
            width: connectionsCount
          })
        }
    }
  }

  return edges;
}

function buildNodesDictionary(node) {
  var nodesDictionary = {};
  nodes.forEach(function(node) {
    nodesDictionary[node.label] = node.id;
  })
  return nodesDictionary;
}

function normalizeCounts(graphData) {
  for (var sourceNode in graphData) {
    var maxCount = 0;
    for (var targetNode in graphData) {
      var connectionsCount = graphData[sourceNode][targetNode];
      if (connectionsCount > maxCount) {
        maxCount = connectionsCount;
      }
    }
    if (maxCount > 0) {
      for (var targetNode in graphData) {
        var connectionsCount = graphData[sourceNode][targetNode];
        if (connectionsCount > 0) {
          graphData[sourceNode][targetNode] = 1 + 2 * (0.0 + connectionsCount) / maxCount
        }
     }
    }
  }
}


function calculateNodeSizes(nodeData) {
  var nodesSize = {}
  for (var sourceNode in graphData) {
    for (var targetNode in graphData[sourceNode]) {
      var connectionsCount = graphData[sourceNode][targetNode];
      if (targetNode in nodesSize) {
        nodesSize[targetNode] += connectionsCount;
      } else {
        nodesSize[targetNode] = connectionsCount;
      }
    }
  }
  var minSize = _.min(_.values(nodesSize));
  var maxSize = _.max(_.values(nodesSize));

  var maxFont = 30;
  var minFont = 10;

  for (var node in nodesSize) {
    nodesSize[node] = nodesSize[node] * (0.0 + maxFont - minFont) / (maxSize - minSize) + (minFont - minSize);
  }

  return nodesSize;
}

var nodes = getNodes(graphData);
normalizeCounts(graphData);
var nodesDictionary = buildNodesDictionary(nodes);
var edges = getEdges(graphData, nodesDictionary);

var nodes2 = new vis.DataSet([
  {id: 1, label: 'X'},
  {id: 2, label: 'Y'},
  {id: 3, label: 'Z'}
]);

// create an array with edges
var edges2 = new vis.DataSet([
  {from: 1, to: 2, arrows:'to', width: 5},
  {from: 2, to: 3, arrows:'to'},
]);

// create a network
var container = document.getElementById('mynetwork');
var data = {
  nodes: nodes,
  edges: edges
};
var options = {
  physics:{
    enabled: true,
    barnesHut: {
      gravitationalConstant: -2000,
      centralGravity: 0.3,
      springLength: 95,
      springConstant: 0.04,
      damping: 0.09,
      avoidOverlap: 0
    },
    forceAtlas2Based: {
      gravitationalConstant: -50,
      centralGravity: 0.01,
      springConstant: 0.08,
      springLength: 100,
      damping: 0.4,
      avoidOverlap: 0
    },
    repulsion: {
      centralGravity: 0.2,
      springLength: 200,
      springConstant: 0.05,
      nodeDistance: 200,
      damping: 0.09
    },
    hierarchicalRepulsion: {
      centralGravity: 0.0,
      springLength: 100,
      springConstant: 0.01,
      nodeDistance: 120,
      damping: 0.09
    },
    maxVelocity: 50,
    minVelocity: 0.1,
    solver: 'repulsion',
    stabilization: {
      enabled: true,
      iterations: 1000,
      updateInterval: 100,
      onlyDynamicEdges: false,
      fit: true
    },
    timestep: 0.5,
    adaptiveTimestep: true
  }
}


var network = new vis.Network(container, data, options);