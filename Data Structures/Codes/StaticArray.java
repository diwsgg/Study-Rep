
public class Main {
    public static void main(String[] args) {
        int  index = -1;
        //WE will create an array of integers and print its size

        System.out.println("Enter the size of the array: ");
        //Ask to the user to enter the size of the array
        int size = Integer.parseInt(System.console().readLine());

        //Now we create the array with the size entered by the user
        int[] array = new int[size];

        //Now we can fill the array in one class and search in another class
        //But we need a menu to be show always until the user wanted to exit so for the first time we can do
        String flag = "y";
        do{
            System.out.println("Options with the array: \n");
            System.out.println("1. Fill the array");
            System.out.println("2. Search an element\n");
            
            int option = Integer.parseInt(System.console().readLine());

            switch (option) {
                case 1:
                    fillArray(array);
                    break;
            
                case 2:
                    System.out.println("Type the element to find");
                    int element = Integer.parseInt(System.console().readLine());

                    int temp = findElement(array, element, index);
                    if (temp!=-1){
                        System.out.println("The index of the element is: " + temp);
                    }else{
                        System.out.println("Element is not on the array");
                    }

                    break;
            }
            //Ask if wanterd to continue
            System.out.println("Continue or exit: [Y, N]");
            flag = System.console().readLine();
        }while(flag.equals("y") || flag.equals("Y"));
        System.out.println("Later");
    }


    //Method to fill the array with values
    public static void fillArray(int[] array) {
        //Check if array is null
        if(array == null) {
            System.out.println("The array is full");
            return;
        }else{

            System.out.println("Enter the elements of the array: ");
            for (int i=0; i < array.length; i++) {
                System.out.println("Element: "+ (i+1));
                array[i] = Integer.parseInt(System.console().readLine());
            }
        }
    }

    //Method to find an element in the array
    public static int findElement(int[] array, int element, int index) {
        //Check if is not empty
        if(array == null ){
            System.out.println("Array is empty");  
        }else{
            //Binary Search, need to have the array order

            //Order the array first
            java.util.Arrays.sort(array);

            int mid=0, low=0, high=array.length;
            while(low<=high){
                mid=(low+high)/2;
                if(array[mid]== element){
                    return index=mid;
                }else if (array[mid]<element){
                    low = mid+1;
                }else if (array[mid]>element) {
                    high = mid-1;
                }
            }
        }
        return index;
    }
}

