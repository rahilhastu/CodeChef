import java.util.*;
class SnakeCoup {
    
    static int fences2(String[] matrix, int n)
    {
        boolean hori=matrix[0].indexOf('*')>=0&&matrix[1].indexOf('*')>=0;     
        System.out.println(hori);
        int f=hori?1:0;
        System.out.println(f);
        boolean prod[]=new boolean[]{false,false};
        for (int i=0; i<n; i++)  {
            for (int k=0; k<2;k++) {
                if (matrix[k].charAt(i)=='*') {
                    if (prod[k]) {
                        f++;
                        prod[0]=prod[1]=false;
                        break;
                    }
                }
            }
            for (int k=0; k<2;k++)
                if (matrix[k].charAt(i)=='*')
                    prod[k]=true; 
        }
        return f;
    }
    
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {      
        int T=sc.nextInt();     
        for (int i=0; i<T; i++) {
            int n=sc.nextInt(); 
            String[] matrix=new String[2];
            matrix[0]=sc.next();
            matrix[1]=sc.next();
            System.out.println(fences2(matrix,n));
    }
}
}