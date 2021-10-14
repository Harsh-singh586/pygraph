from bottle import route, run, view, static_file

graphs = []

class graph:

    def __init__(self,name, xaxis):
        self.xaxis = xaxis
        self.name = name
        self.data = {'base' : {'name' : name, 'xaxis' : xaxis}, 'data' : [] } 
    
    def adddata(self,ctype, label, value, backcol = ['grey']):
        dic = {'type' : ctype,'label' : label, 'data' : value, 'backgroundColor' : backcol}
        self.data['data'].append(dic)

    def getgraph(self):
        return self.data
 
@route('/<filename:path>')
def js(filename):
    return static_file('chart.js', root="")

def show(graphs):
    @route('/')
    @view('base')
    def hello():
        return dict(graph = graphs)
    graphs = graphs
    run(host='localhost', port=8080, debug=True)

