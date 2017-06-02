import java.util.*;
import java.util.AbstractMap.SimpleEntry;
import static java.lang.System.out;
class SnMax {
    int matrix[][];
    int maxV;
    SnMax(int matrix[][], int maxxx)
    {
        List<Map.Entry<Integer, Integer>> maxEntry=new ArrayList<>();
        for (int i=0; i<matrix.length; i++)
            for (int j=0; j<matrix[i].length; j++) {
                if ( matrix[i][j]==maxxx)
                    maxEntry.add(new SimpleEntry<Integer,Integer>(i,j));
            }
        this.matrix=matrix;
        maxV=maxxx;
        out.println(scan(maxEntry));
    }
    void change(int i, int j, List<Map.Entry<Integer, Integer>> newEntry)
    {
        if (i<0 || j<0 || i>=matrix.length || j>=matrix[0].length)
            return;
        if(matrix[i][j]>=maxV)
            return;
        matrix[i][j]=maxV;
        newEntry.add(new SimpleEntry<Integer,Integer>(i,j));
    }
    int scan(List<Map.Entry<Integer, Integer>> entry)
    {
        List<Map.Entry<Integer, Integer>> newEntry=new ArrayList<>();
        for (Map.Entry<Integer, Integer> e: entry) {
            int i=e.getKey();
            int j=e.getValue();
            change(i-1, j-1, newEntry);
            change(i-1, j, newEntry);
            change(i-1, j+1, newEntry);
            change(i, j-1, newEntry);
            change(i, j+1, newEntry);
            change(i+1, j-1, newEntry);
            change(i+1, j, newEntry);
            change(i+1, j+1, newEntry);
        }
        if ( newEntry.isEmpty())
            return 0;
        else {
            return 1+scan(newEntry);
        }
    }
    static int fillMatrix(int [][] matrix, Scanner reader) 
    {
        int maxxx=0; 
        for (int i=0; i<matrix.length; i++)
            for (int j=0; j<matrix[i].length; j++) {
                matrix[i][j]=reader.nextInt();
                if ( matrix[i][j]>maxxx)
                    maxxx=matrix[i][j];
            }
        return maxxx;
    }
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] a)
    {      
        int T=sc.nextInt();
        for (int i=0; i<T; i++) {
            int n=sc.nextInt();     
            int maxxx=sc.nextInt();
            int matrix[][]=new int[n][maxxx];
            int mx=fillMatrix(matrix, sc);
            new SnMax(matrix, mx);
        }
    }
}