import java.util.*;
import java.math.BigDecimal;
class Solution {
    public int solution(int n) {
        double tmp = Math.sqrt(n);
        return (BigDecimal.valueOf(tmp).multiply(BigDecimal.valueOf(tmp)))
            .compareTo(BigDecimal.valueOf(n)) == 0 ? 1 : 2;
    }
}