class LRUCache {

    class Node {
        int key;
        int val;
        Node next; 
        Node prev;

        public Node (int key, int val){
            this.key = key; 
            this.val = val; 
        }
    }

    private int capacity;
    Map<Integer, Node> cache = new HashMap<>();
    private Node head;
    private Node tail;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        cache = new HashMap<>();
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if(!cache.containsKey(key)){
            return -1;
        }
        Node curr = cache.get(key);
        movetofront(curr);
        return curr.val;
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){
            Node curr = cache.get(key);
            curr.val = value;
            movetofront(curr);
            return;
        }
        else if(cache.size() == capacity){
            Node trash = tail.prev;
            cache.remove(trash.key);
            dispose(trash);
        }
        Node fresh = new Node(key, value);
        cache.put(key, fresh);
        addtofront(fresh);
    }

    public void dispose(Node node){
        node.prev.next = node.next; 
        node.next.prev = node.prev;
    }

    public void movetofront(Node node){
        dispose(node);
        addtofront(node);
    }

    public void addtofront(Node node){
        Node temp = head.next; 
        head.next = node; 
        node.prev = head; 
        node.next = temp;
        temp.prev = node;
    }
}
