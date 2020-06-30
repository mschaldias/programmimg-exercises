public class Fibonacci {


	public static int fibonacci(int n, int a0,int a1,int i) {

		
		if ( n <=1) {

			return a0;
		}
		
		else if ( i == n - 2) {

			
			return a0 + a1;
		}

		int a = a0 + a1;
		a0 = a1;
		a1 = a; 		 
		i++;
		return fibonacci(n,a0,a1,i);
		

	}

	public static void main(String args[]) {

		int i = 0;
		int a0 = 1;
		int a1 = 1;
		int f = fibonacci(7,a0,a1,i);
		System.out.print(f);
	}
}