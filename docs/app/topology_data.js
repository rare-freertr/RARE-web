
//let url = 'http://10.233.108.88:8080/api/topology';
//const url = 'http://192.168.113.101:8080/api/topology';
//var url = 'http://127.0.0.1:8080/api/topology';
//let topologyData;
//topologyData = await (await fetch(url)).json();

//async function getTopology() {
//  const response = await fetch(url);
//  const data = await response.json();
  //console.log(data);
//  return(data); 
//}

//async function dosomething() {
//    var test = await getTopology();
//    return (test);
//}

//topologyData = dosomething();

//console.log(topologyData);


//console.log(topologyData);

/*
topologyData = fetch(url)
  .then((response) => {
    return response.json()
  })
  .then(function (data) {
    // Work with JSON data here
    //console.log(data);
    return(data);
  })
  .catch((err) => {
    // Do something for an error here
  });
*/

/*
topologyPromise = fetch(url)
  .then((response) => response.json())
  .then((result) => {
    topologyData=result;
    return (result);
  });

const printAddress = () => {
  topologyData.then((a) => {
    console.log(a);
  });
};

const getTopologyData = () => {
  topologyPromise.then((a) => {
    console.log(a);
    topologyData = a;
  });
};

getTopologyData();

//printAddress();
console.log(topologyData)
*/

