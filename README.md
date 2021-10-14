# pygraph


Developed by Harsh-singh586 2021

## Examples of How To Use

```python
import pygraph

g1 = pygraph.graph(name , x-xis)
g1.adddata(graph_type , lebel, y-axis, background_color)
g1.adddata(graph_type , lebel, y-axis, background_color)
graph1 = g1.getgraph()
pygraph.show([graph1])
```

Example Single Graph
```python
import pygraph

# Choose One

g1 = pygraph.graph('first', ['firstval', 'secval'])
g1.adddata('bar', 'test', [4, 3], ['yellow', 'green'])
graph1 = g1.getgraph()
pygraph.show([graph1])
```

Example Muptiple Graph
```python
import pygraph

# Choose One

g1 = pygraph.graph('first', ['firstval', 'secval'])
g1.adddata('bar', 'test', [4, 3], ['yellow', 'green'])
graph1 = g1.getgraph()
g2 = pygraph.graph('second', ['firstval', 'secval'])
g1.adddata('bar', 'test', [8, 7], ['yellow', 'green'])
graph2 = g2.getgraph()
pygraph.show([graph1, graph2])
```

Example Mixed Graph
```python
import pygraph

# Choose One

g1 = pygraph.graph('first', ['firstval', 'secval'])
g1.adddata('bar', 'test', [4, 3], ['yellow', 'green'])
g1.adddata('line', 'test', [8, 7], ['red', 'blue'])
graph1 = g1.getgraph()
pygraph.show([graph1])
```

You can see your graph on http://localhost:8000

NOTE:
   
   1. No two graph name can be same
   2. Number of values on y-axis must be same as x-axis
   3. Graphs Available
       1. 'bar'
       2. 'line'
       3. 'polar'
       4. 'doughnut'
       5. 'pie'


![Sampple](/sample.png)

Check out: https://github.com/Harsh-singh586/pygraph