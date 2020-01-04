function init() {
  // get some data from flask
  d3.json('/data').then(data => {
    console.log(data);
    d3.select('#data')
      .selectAll('#number')
      .data(data)
      .enter()
      .append('li')
      
      .text((d, i) => d)
  })
}

init();