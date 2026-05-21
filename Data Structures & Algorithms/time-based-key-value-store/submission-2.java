
class TimeMap {
    private Map<String, List<Pair>> timeMap;

    public TimeMap() {
        this.timeMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        Pair p = new Pair(timestamp, value);
        timeMap.putIfAbsent(key, new ArrayList<>());
        timeMap.get(key).add(p);
    }
    
    public String get(String key, int timestamp) {
        List<Pair> list = timeMap.get(key);
        if(list == null){
            return "";
        }
        int start = 0;
        int end = list.size() - 1;
        String ans = "";
        while(start <= end){
            int mid = (start + end)/2;
            int midTimeStamp = list.get(mid).getKey();
            if(midTimeStamp == timestamp){
                return list.get(mid).getValue();
            }
            if(midTimeStamp < timestamp){
                ans = list.get(mid).getValue();
                start = mid + 1;
            }
            else{ 
                end = mid - 1;
            }
        }
        return ans;
    }
}

public class Pair{
    Integer timestamp; 
    String value; 

    public Pair(Integer timestamp, String value){
        this.timestamp = timestamp;
        this.value = value;
    }

    public int getKey(){
        return timestamp;
    }

    public String getValue(){
        return value;
    }
}
