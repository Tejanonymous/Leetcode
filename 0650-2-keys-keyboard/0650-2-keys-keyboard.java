class Solution {
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false; 
        }
        if (number <= 3) {
            return true;   // 2 and 3 are prime
        }
        if (number % 2 == 0 || number % 3 == 0) {
            return false; 
        }

        // Check divisibility with numbers of the form 6k ± 1
        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }
    
    public int minSteps(int n) {
        if (n <= 1) {
            return 0; // Base case: 0 steps needed for 0 or 1
        }
        if (isPrime(n)) {
            return n;
        }
        
        
        
        
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return i + minSteps(n / i);
                
            }
        }
        
        return 0;
    }
}
