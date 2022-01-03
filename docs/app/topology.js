(function (nx) {
	nx.define('MyTopology', nx.graphic.Topology, {
		methods: {
			"init": function(){
				this.inherited({
					// width 100% if true
					'adaptive': true,
					// show icons' nodes, otherwise display dots
					'showIcon': true,
					// special configuration for nodes
					'nodeConfig': {
						'label': 'model.name',
						'iconType': 'router',
						'color': '#00ff00' //'#0how00'
					},
					// special configuration for links
					'linkConfig': {
						'linkType': 'curve',
						'color': '#00ff00', //'#0how00'
						'taillabel': 'model.taillabel',
						'midlabel': 'model.midlabel',
				        'headlabel': 'model.headlabel',
					},
					'theme': 'rare',
					// property name to identify unique nodes
					'identityKey': 'name', // helps to link source and target
					// canvas size
					//'width': 640,
					'height': '600',
					// "engine" that process topology prior to rendering
					'dataProcessor': 'force',
					// moves the labels in order to avoid overlay
					'enableSmartLabel': true,
					// smooth scaling. may slow down, if true
					'enableGradualScaling': true,
					// if true, two nodes can have more than one link
					'supportMultipleLink': true,
					// enable scaling
					"scalable": true,
					"linkInstanceClass": 'RARELinkClass',
					"showNavigation": false
				});
			}
		}
	});
})(nx);

