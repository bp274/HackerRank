import java.io.*;
import java.util.*;

class AdjacencyListNode
{
    public int nodeIndex;
    public int weight;

    public AdjacencyListNode next;

    AdjacencyListNode(int nodeIndex, int weight)
    {
        this.nodeIndex = nodeIndex;
        this.weight = weight;
        this.next = null;
    }
}

class AdjacencyList
{
    public AdjacencyListNode head;
    public AdjacencyListNode tail;

    AdjacencyList()
    {
        head = null;
        tail = null;
    }

    public void storeEdge(int nodeIndex, int weight)
    {
        if (head == null)
        {
            head = new AdjacencyListNode(nodeIndex, weight);
            tail = head;
        }
        else
        {
            tail.next = new AdjacencyListNode(nodeIndex, weight);
            tail = tail.next;
        }
    }
}

class Graph
{
    private AdjacencyList adjacencyListArray[];
    public Vertex vertex[];
    public int numberOfNodes;
    private int numberOfEdges;

    Graph(int totalNodes, int totalEdges)
    {
        adjacencyListArray = new AdjacencyList[totalNodes];
        numberOfNodes = totalNodes;
        numberOfEdges = totalEdges;

        for (int i = 0; i < numberOfNodes; i++)
        {
            adjacencyListArray[i] = new AdjacencyList();
        }
    }

    public void addEdge(int startIndex, int endIndex, int weight)
    {
        adjacencyListArray[startIndex].storeEdge(endIndex, weight);
    }

    public void initializeSingleSource(Graph graph, int source)
    {
        vertex = new Vertex[graph.numberOfNodes];

        for (int i = 0; i < graph.numberOfNodes; i++)
        {
            vertex[i] = new Vertex();
            vertex[i].index = i;
            vertex[i].distance = Integer.MAX_VALUE;
            vertex[i].heapIndex = -1;
        }

        vertex[source].index = source;
        vertex[source].distance = 0;
    }

    public void dijkstra(Graph graph, int source)
    {
        int totalWeight = 0;

        initializeSingleSource(graph, source);

        int visited[] = new int[graph.numberOfNodes];

        MinHeap minHeap = new MinHeap(graph.numberOfNodes);
        for (int i = 0; i < graph.numberOfNodes; i++)
        {
            minHeap.insert(vertex[i]);
        }

        while (minHeap.isEmpty() != true)
        {
            Vertex u;
            u = minHeap.extractMin();

            visited[u.index] = 1;
            u.heapIndex = -1;

            totalWeight += u.distance;

            AdjacencyListNode temp;
            temp = graph.adjacencyListArray[u.index].head;

            while (temp != null)
            {
                Vertex v = vertex[temp.nodeIndex];
                int w = temp.weight;

                if (visited[v.index] != 1 && w < v.distance)
                {
                    v.distance = w;
                    minHeap.heapIncreaseKey(v.heapIndex);
                }

                temp = temp.next;
            }
        }
        System.out.print(totalWeight);
    }
}

class Vertex
{
    public int index;
    public int distance;
    public int heapIndex;
}

class MinHeap
{
    public Vertex heap[];
    private int capacity;
    public int heapSize;

    MinHeap(int size)
    {
        heap = new Vertex[size];
        capacity = size;
        heapSize = 0;
    }

    public int parent(int index) { return (index - 1) / 2; }
    public int leftChild(int index) { return (2 * index + 1); }
    public int rightChild(int index) { return (2 * index + 2); }

    public void swapValuesAt(int i, int j)
    {
        Vertex temp;

        temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;

        int tempIndex;

        tempIndex = heap[i].heapIndex;
        heap[i].heapIndex = heap[j].heapIndex;
        heap[j].heapIndex = tempIndex;
    }

    public void heapIncreaseKey(int i)
    {
        while (i > 0 && heap[parent(i)].distance > heap[i].distance)
        {
            swapValuesAt(i, parent(i));
            i = parent(i);
        }
    }

    public void insert(Vertex v)
    {
        heapSize += 1;
        v.heapIndex = heapSize - 1;
        heap[heapSize - 1] = v;

        heapIncreaseKey(heapSize - 1);
    }

    public void heapify(int i)
    {
        int l = leftChild(i);
        int r = rightChild(i);
        int smallest = i;

        if (l < heapSize && heap[l].distance < heap[smallest].distance)
        {
            smallest = l;
        }
        if (r < heapSize && heap[r].distance < heap[smallest].distance)
        {
            smallest = r;
        }
        if (smallest != i)
        {
            swapValuesAt(i, smallest);
            heapify(smallest);
        }
    }

    public Vertex extractMin()
    {
        Vertex min;
        min = heap[0];

        swapValuesAt(0, heapSize - 1);
        heapSize -= 1;

        heapify(0);

        return min;
    }

    public boolean isEmpty()
    {
        if (heapSize == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

class Solution
{
    static PrintWriter out = new PrintWriter(System.out);
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st = new StringTokenizer("");

    public static void main(String[] args) throws IOException
    {
        st = new StringTokenizer(br.readLine());

        int numberOfNodes = Integer.parseInt(st.nextToken());

        int numberOfEdges = Integer.parseInt(st.nextToken());

        Graph graph = new Graph(numberOfNodes, numberOfEdges);

        for (int i = 0; i < numberOfEdges; i++)
        {
            st=new StringTokenizer(br.readLine());

            int index1 = Integer.parseInt(st.nextToken());
            int index2 = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph.addEdge(index1 - 1, index2 - 1, weight);
            graph.addEdge(index2 - 1, index1 - 1, weight);
        }

        int source = Integer.parseInt(br.readLine());

        graph.dijkstra(graph, source - 1);
    }
}
