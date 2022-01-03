(function(nx){

	// instantiate NeXt app
	var app = new nx.ui.Application();

	// instantiate Topology class
	var topology = new MyTopology();
    
    var topologyData;

    var referrer = document.referrer.replace(/\/$/, '');;

    const tstcase = referrer.split("/").pop();
    
    const api_url =`../json/${tstcase}.json`;

	// load topology data from REST API
    async function getTopology() {
        const response = await fetch(api_url);
        topologyData = await response.json();
        console.log(topologyData);
        topology.data(topologyData);
    }

       getTopology();


	// bind the topology object to the app
	topology.attach(app);

	// app must run inside a specific container. In our case this is the one with id="topology-container"
	app.container(document.getElementById("topology-container"));

})(nx);
