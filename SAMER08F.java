import java.io.IOException;

public class Main {

	public static int squares(int x){
		if(x ==1){
		return 1;
		       }

		else{
		       return (int) (squares(x-1) + Math.pow(x, 2));    
		       }
		       }
	


	public static void main(String[] args) throws NumberFormatException, IOException {
		java.io.BufferedReader r = new java.io.BufferedReader (new java.io.InputStreamReader (System.in));
	       String s;
	       int a;
	       while (!(s=r.readLine()).startsWith("0")){
	    	   a= Integer.parseInt(s);
	           
	            System.out.println(squares(a));
	           
	           
	       }

	}

}





   