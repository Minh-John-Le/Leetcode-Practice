class Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] result = new int[triangle.size() + 1];
        
        // intialize the array
        for (int i = 0; i < result.length; i++)
        {
            result[i] =(int) Math.pow(10,4);
        }
        
        result[0] = triangle.get(0).get(0);
        
        for (int i = 1; i < triangle.size(); i++)
        {
            List<Integer> currentList = triangle.get(i);
            
            for (int j = currentList.size() - 1; j > 0; j--)
            {
                result[j] = Math.min(currentList.get(j) + result[j - 1], currentList.get(j) + result[j]);
            }
            result[0] = result[0] + currentList.get(0);
        }
        
        Arrays.sort(result);
        return result[0];
        
    }
}

/*
This is similiar to single source shortest path 

RunTime o(G) G is the grapgh size. Other word is the number of element in the triangle since
we iterate thorugh all of them

*/
