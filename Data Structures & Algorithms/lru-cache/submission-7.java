class LRUCache {
    class Node{
        int key; 
        int val; 
        Node prev;
        Node next;

        public Node(int key, int val){
            this.key = key; 
            this.val = val;
        }
    }
    Map<Integer, Node> map;
    private Node head;
    private Node tail;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity; 
        map = new HashMap<>();
        head = new Node(0,0);
        tail = new Node(0,0);
        head.next = tail; 
        tail.prev = head;
    }
    
    public int get(int key) {
        if(map.containsKey(key)){
            Node curr = map.get(key);
            movetofront(curr);
            return curr.val;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node curr = map.get(key);
            curr.val = value;
            movetofront(curr);
            return;
        }
        if(map.size() == capacity){
            Node LRU = tail.prev;
            map.remove(LRU.key);
            remove(LRU);
        }
        Node node = new Node(key, value);
        map.put(key, node);
        addtofront(node);
    }

    private void remove(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    private void addtofront(Node node){
        Node temp = head.next; 
        head.next = node;
        node.prev = head;
        node.next = temp; 
        temp.prev = node;
    }

    private void movetofront(Node node){
        remove(node);
        addtofront(node);
    }
}
