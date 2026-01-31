package Domain;

public class Log {
    public int rid;
    public int from;
    public int to;
    public int amount;

    public Log(int rid, int from, int to, int amount){
        this.rid = rid;
        this.from = from;
        this.to = to;
        this.amount = amount;
    }
}
