(function (nx) {
nx.define('RARELinkClass', nx.graphic.Topology.Link, {
    properties: {
        taillabel: null,
         midlabel: null,
        headlabel: null,
    },
    view: function(view) {
        view.content.push({
            name: 'source',
            type: 'nx.graphic.Text',
            props: {
                'class': 'taillabel',
                'alignment-baseline': 'text-after-edge',
                'text-anchor': 'start',
            }
        },{
            name: 'midlabel',
            type: 'nx.graphic.Text',
            props: {
                'class': 'midlabel',
                'alignment-baseline': 'text-after-edge',
                'text-anchor': 'center'
            }
        }, {
            name: 'target',
            type: 'nx.graphic.Text',
            props: {
                'class': 'headlabel',
                'alignment-baseline': 'text-after-edge',
                'text-anchor': 'end'
            }
        });
        return view;
    },
    methods: {
        update: function() {
            this.inherited();
            var el, point;
            var line = this.line();
            var angle = line.angle();
            var stageScale = this.stageScale();
	        //var lenMidLabel = 0;
            line = line.pad(18 * stageScale, 18 * stageScale);
            if (this.taillabel()) {
                el = this.view('source');
                point = line.start;
                el.set('x', point.x);
                el.set('y', point.y);
                el.set('text', this.taillabel());
                el.set('transform', 'rotate(' + angle + ' ' + point.x + ',' + point.y + ')');
                el.setStyle('font-size', 12 * stageScale);
                el.setStyle('font-family', 'Cisco Sans Reg');
                el.setStyle('fill', '#00ff00');
            }
            if (this.headlabel()) {
                el = this.view('target');
                point = line.end;
                el.set('x', point.x);
                el.set('y', point.y);
                el.set('text', this.headlabel());
                el.set('transform', 'rotate(' + angle + ' ' + point.x + ',' + point.y + ')');
                el.setStyle('font-size', 12 * stageScale);
                el.setStyle('font-family', 'Cisco Sans Reg');
                el.setStyle('fill', '#00ff00');
            }
            if (this.midlabel()) {
                el = this.view('midlabel');
                point = line.center();
                //console.log(point.x ,point.y);
                //console.log(`length ${lenMidLabel}`);
                el.set('x', point.x - 30 );
                el.set('y', point.y + 10 );
                el.set('text', this.midlabel());
                //console.log(`WIDTH: ${el.getBound().width}`);
                el.set('transform', 'rotate(' + angle + ' ' + point.x + ',' + point.y + ')');
                el.setStyle('font-size', 12 * stageScale);
                el.setStyle('font-family', 'Cisco Sans Reg');
                el.setStyle('fill', '#00ff00');
            }
        }
    }
});
})(nx);
