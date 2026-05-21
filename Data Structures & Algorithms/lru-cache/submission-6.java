class LRUCache {
    class Node{
        int key;
        int val;
        Node next; 
        Node prev;

        public Node(int key, int val){
            this.key = key;
            this.val = val;
        }
    }

    Map<Integer, Node> cache;
    private Node head; 
    private Node tail;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity; 
        cache = new HashMap<>();
        head = new Node(0,0);
        tail = new Node(0,0);
        head.next = tail; 
        tail.prev = head;
    }
    
    public int get(int key) {
       if(cache.containsKey(key)){
        Node curr = cache.get(key);
        movetofront(curr);
        return curr.val;
       }
       return -1; 
    }
    
    public void put(int key, int value) {
        if(cache.containsKey(key)){
            Node curr = cache.get(key);
            curr.val = value;
            movetofront(curr);
            return;
        }
        if(cache.size() == capacity){
            Node lru = tail.prev;
            cache.remove(lru.key);
            remove(lru);
        }
        Node fresh = new Node(key, value);
        cache.put(key, fresh);
        addtofront(fresh);
    }

    public void remove(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    public void addtofront(Node node){
        Node temp = head.next;
        head.next = node; 
        node.next = temp; 
        node.prev = head;
        temp.prev = node;
    }

    public void movetofront(Node node){
        remove(node);
        addtofront(node);
    }
}
